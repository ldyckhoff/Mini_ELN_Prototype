from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from typing import Any

import streamlit as st
from pydantic import ValidationError

from eln.experiment_models import Experiment, GenericProcessStep, Sample
from eln.schema_document import (
    MetadataSchemaDocument,
    ParameterDefinition,
    ProcessDefinition,
)
from eln.storage import (
    APP_DIR,
    copy_uploaded_file,
    delete_experiment_folder,
    experiment_folder,
    list_experiments,
    load_config,
    load_experiment,
    save_config,
    save_experiment,
)
from eln.ui_helpers import render_parameter_input, status_label


st.set_page_config(page_title="Pilot ELN", layout="wide")

CONFIG = load_config()
DATA_DIR = Path(CONFIG.experiment_data_dir)

OFFICIAL_SCHEMA_PATH = APP_DIR / "schemas" / "official" / "processes.yaml"
PROPOSED_SCHEMA_PATH = APP_DIR / "schemas" / "proposed" / "student_extensions.yaml"


def load_schema() -> MetadataSchemaDocument:
    official = MetadataSchemaDocument.from_yaml_file(
        OFFICIAL_SCHEMA_PATH,
        source_label="official",
        bootstrap_from_python_module="generated_process_classes",
    )
    proposed = MetadataSchemaDocument.from_yaml_file(
        PROPOSED_SCHEMA_PATH,
        source_label="proposed",
        create_if_missing=True,
    )
    return official.merge_with(proposed)


def new_experiment() -> None:
    st.session_state.experiment = Experiment(schema_version=st.session_state.schema.version)
    st.session_state.loaded_experiment_id = None
    st.session_state.selected_step_id = None
    st.session_state.selected_sample_id = None


def select_step(step_id: str | None) -> None:
    st.session_state.selected_step_id = step_id
    st.session_state.selected_sample_id = None


def select_sample(sample_id: str | None) -> None:
    st.session_state.selected_sample_id = sample_id
    st.session_state.selected_step_id = None


def back_to_overview() -> None:
    st.session_state.selected_step_id = None
    st.session_state.selected_sample_id = None


def reload_schema() -> None:
    st.session_state.schema = load_schema()


def save_current_experiment() -> None:
    exp = st.session_state.experiment
    exp.updated_at = datetime.now()
    path = save_experiment(exp, DATA_DIR)
    st.session_state.loaded_experiment_id = exp.id
    st.session_state.last_message = f"Saved experiment to: {path}"


def add_schema_feedback(
    step: GenericProcessStep,
    feedback_type: str,
    item_id: str,
    reason: str | None,
) -> None:
    step.schema_feedback.append(
        {
            "type": feedback_type,
            "item_id": item_id,
            "reason": reason or "",
            "status": "proposed",
            "created_at": datetime.now().isoformat(timespec="seconds"),
        }
    )


def steps_for_sample(sample_id: str) -> list[GenericProcessStep]:
    return [step for step in exp.process_steps if sample_id in step.sample_ids]


def step_process_help(step: GenericProcessStep) -> str | None:
    process = schema_doc.get_process(step.process_id)
    if not process:
        return None
    return process.definition


def render_add_parameter_form(
    process: ProcessDefinition,
    form_key: str,
    step: GenericProcessStep | None = None,
) -> None:
    with st.form(form_key):
        parameter_label = st.text_input("Parameter label")
        parameter_id = st.text_input("Parameter ID")
        parameter_type = st.selectbox(
            "Type",
            ["string", "number", "integer", "boolean", "date", "datetime", "enum"],
            key=f"{form_key}_type",
        )
        unit = st.text_input("Unit")
        required = st.checkbox("Required")
        description = st.text_area("Description", height=80)
        example_value = st.text_input("Example value")
        reason = st.text_area("Why is this needed?", height=80)

        if st.form_submit_button("Save proposed parameter"):
            try:
                parameter = ParameterDefinition(
                    id=parameter_id.strip(),
                    label=parameter_label.strip(),
                    type=parameter_type,
                    unit=unit or None,
                    required=required,
                    description=description or None,
                    example_values=[example_value] if example_value else [],
                    status="proposed",
                    reason=reason or None,
                )
                schema_doc.add_proposed_parameter(
                    PROPOSED_SCHEMA_PATH,
                    process.id,
                    process.label,
                    parameter,
                )
                if step:
                    step.parameters.setdefault(parameter.id, None)
                    step.used_proposed_schema_items.append(f"parameter:{parameter.id}")
                    add_schema_feedback(step, "missing_parameter", parameter.id, reason)
                reload_schema()
                st.session_state.last_message = (
                    f"Saved proposed schema extension to: {PROPOSED_SCHEMA_PATH}"
                )
                st.rerun()
            except (ValidationError, ValueError) as exc:
                st.error(str(exc))


if "schema" not in st.session_state:
    reload_schema()

if "experiment" not in st.session_state:
    new_experiment()

if "loaded_experiment_id" not in st.session_state:
    st.session_state.loaded_experiment_id = None

if "selected_step_id" not in st.session_state:
    st.session_state.selected_step_id = None

if "selected_sample_id" not in st.session_state:
    st.session_state.selected_sample_id = None

if "last_message" not in st.session_state:
    st.session_state.last_message = None


schema_doc: MetadataSchemaDocument = st.session_state.schema
exp: Experiment = st.session_state.experiment


# Sidebar: files and workflow
st.sidebar.title("Pilot ELN")
st.sidebar.caption("Local experiment documentation")

if st.sidebar.button("New experiment"):
    new_experiment()
    st.rerun()

experiment_options = list_experiments(DATA_DIR)
if experiment_options:
    labels = {
        item["id"]: f"{item['name']} ({item['id']})" for item in experiment_options
    }
    selected_file_id = st.sidebar.selectbox(
        "Load experiment",
        [""] + [item["id"] for item in experiment_options],
        format_func=lambda item_id: "Select experiment" if item_id == "" else labels[item_id],
    )
    if selected_file_id and st.sidebar.button("Load selected"):
        st.session_state.experiment = load_experiment(DATA_DIR, selected_file_id)
        st.session_state.loaded_experiment_id = selected_file_id
        st.session_state.selected_step_id = None
        st.session_state.selected_sample_id = None
        st.session_state.last_message = f"Loaded experiment: {selected_file_id}"
        st.rerun()

st.sidebar.divider()
st.sidebar.markdown(f"**Experiment:** {exp.name or '(unnamed)'}")
st.sidebar.caption(exp.id)

with st.sidebar.expander("Samples", expanded=True):
    if not exp.samples:
        st.caption("No samples yet")
    for sample in exp.samples:
        if st.button(sample.name or sample.id, key=f"select_sample_{sample.id}"):
            select_sample(sample.id)
            st.rerun()

with st.sidebar.expander("Workflow", expanded=True):
    if not exp.process_steps:
        st.caption("No process steps yet")
    for index, step in enumerate(exp.process_steps, start=1):
        marker = " [proposed]" if step.schema_status == "proposed" else ""
        if st.button(
            f"{index}. {step.name}{marker}",
            key=f"select_{step.id}",
            help=step_process_help(step),
        ):
            select_step(step.id)
            st.rerun()

st.sidebar.divider()
if st.sidebar.button("Save experiment"):
    save_current_experiment()

if st.session_state.loaded_experiment_id:
    confirm_delete = st.sidebar.checkbox("Confirm permanent delete")
    if st.sidebar.button("Delete experiment", disabled=not confirm_delete):
        delete_experiment_folder(DATA_DIR, st.session_state.loaded_experiment_id)
        new_experiment()
        st.session_state.last_message = "Deleted experiment."
        st.rerun()


st.title("Pilot ELN")
if st.session_state.last_message:
    st.success(st.session_state.last_message)

page = st.tabs(["Experiment", "Schema browser", "Settings"])


with page[0]:
    if st.session_state.selected_step_id is None and st.session_state.selected_sample_id is None:
        st.subheader("Experiment overview")

        col_a, col_b, col_c = st.columns(3)
        with col_a:
            exp.name = st.text_input("Experiment name", exp.name)
            exp.project = st.text_input("Project", exp.project or "")
        with col_b:
            exp.operator = st.text_input("Operator", exp.operator or "")
            exp.experiment_date = st.date_input(
                "Experiment date",
                exp.experiment_date or date.today(),
            )
        with col_c:
            exp.objective = st.text_area("Objective", exp.objective or "", height=124)

        st.divider()
        sample_col, step_col = st.columns([1, 2])

        with sample_col:
            st.subheader("Samples")
            with st.form("add_sample"):
                sample_name = st.text_input("Sample name")
                material = st.text_input("Material")
                notes = st.text_area("Notes", height=80)
                if st.form_submit_button("Add sample"):
                    if sample_name.strip():
                        exp.samples.append(
                            Sample(name=sample_name.strip(), material=material, notes=notes)
                        )
                    else:
                        st.warning("Please provide a sample name.")

            if exp.samples:
                sample_rows = []
                for sample in exp.samples:
                    related_steps = steps_for_sample(sample.id)
                    sample_rows.append(
                        {
                            "sample": sample.name,
                            "material": sample.material or "",
                            "used in steps": ", ".join(step.name for step in related_steps),
                            "number of steps": len(related_steps),
                        }
                    )
                st.dataframe(sample_rows, hide_index=True, width="stretch")

                st.markdown("**Open samples and linked steps**")
                for sample in exp.samples:
                    related_steps = steps_for_sample(sample.id)
                    label = f"{sample.name} ({len(related_steps)} linked steps)"
                    with st.expander(label):
                        if st.button("Edit sample", key=f"edit_sample_{sample.id}"):
                            select_sample(sample.id)
                            st.rerun()
                        if related_steps:
                            st.caption("Linked process steps")
                            for step in related_steps:
                                if st.button(
                                    step.name,
                                    key=f"sample_{sample.id}_step_{step.id}",
                                    help=step_process_help(step),
                                ):
                                    select_step(step.id)
                                    st.rerun()
                        else:
                            st.caption("This sample is not linked to any process step yet.")

        with step_col:
            st.subheader("Add process step")
            process_search = st.text_input("Search process")
            processes = schema_doc.search_processes(process_search)
            if not processes:
                st.warning("No matching process found.")
            else:
                process_id = st.selectbox(
                    "Process",
                    [process.id for process in processes],
                    format_func=lambda pid: status_label(schema_doc.get_process(pid)),
                )
                selected_process = schema_doc.get_process(process_id)
                if selected_process:
                    if selected_process.definition:
                        st.caption(selected_process.definition)
                    if selected_process.synonyms:
                        st.caption("Synonyms: " + ", ".join(selected_process.synonyms))
                    with st.form("add_process_step"):
                        default_name = selected_process.label
                        step_name = st.text_input("Step name", default_name)
                        sample_ids = st.multiselect(
                            "Applies to samples",
                            [sample.id for sample in exp.samples],
                            format_func=lambda sid: next(
                                (sample.name for sample in exp.samples if sample.id == sid),
                                sid,
                            ),
                        )
                        predecessor_ids = st.multiselect(
                            "Preceded by workflow steps",
                            [step.id for step in exp.process_steps],
                            format_func=lambda sid: next(
                                (step.name for step in exp.process_steps if step.id == sid),
                                sid,
                            ),
                        )
                        values: dict[str, Any] = {}
                        for parameter in selected_process.parameters:
                            values[parameter.id] = render_parameter_input(
                                parameter,
                                key=f"new_{selected_process.id}_{parameter.id}",
                            )
                        notes = st.text_area("Notes", height=90)
                        if st.form_submit_button("Add step"):
                            warnings = schema_doc.validate_process_parameters(
                                selected_process.id,
                                values,
                            )
                            new_step = GenericProcessStep(
                                name=step_name or selected_process.label,
                                process_id=selected_process.id,
                                process_label=selected_process.label,
                                schema_status=selected_process.status,
                                sample_ids=sample_ids,
                                predecessor_step_ids=predecessor_ids,
                                parameters=values,
                                notes=notes,
                                schema_version=schema_doc.version,
                            )
                            new_step.used_proposed_schema_items = schema_doc.used_proposed_items(
                                selected_process.id,
                                values,
                            )
                            exp.process_steps.append(new_step)
                            exp.updated_at = datetime.now()
                            if warnings:
                                st.warning("\n".join(warnings))
                            st.success("Added process step.")

            with st.expander("Add new process to proposed schema"):
                with st.form("add_new_process"):
                    process_label = st.text_input("Process label")
                    process_id = st.text_input("Process ID")
                    category_id = st.text_input("Category")
                    definition = st.text_area("Definition", height=80)
                    reason = st.text_area("Why is this needed?", height=80)
                    common_or_specific = st.radio(
                        "Scope",
                        ["common process", "specific to this experiment"],
                        horizontal=True,
                    )
                    p_label = st.text_input("Initial parameter label")
                    p_id = st.text_input("Initial parameter ID")
                    p_type = st.selectbox(
                        "Initial parameter type",
                        ["string", "number", "integer", "boolean", "date", "datetime", "enum"],
                    )
                    p_unit = st.text_input("Initial parameter unit")
                    p_description = st.text_input("Initial parameter description")
                    if st.form_submit_button("Save proposed process"):
                        try:
                            parameter = None
                            if p_label.strip() and p_id.strip():
                                parameter = ParameterDefinition(
                                    id=p_id.strip(),
                                    label=p_label.strip(),
                                    type=p_type,
                                    unit=p_unit or None,
                                    description=p_description or None,
                                    status="proposed",
                                    reason=reason,
                                )
                            process = ProcessDefinition(
                                id=process_id.strip(),
                                label=process_label.strip(),
                                category_id=category_id.strip() or None,
                                definition=definition or None,
                                parameters=[parameter] if parameter else [],
                                status="proposed",
                                reason=f"{reason}\nScope: {common_or_specific}".strip(),
                            )
                            proposed = MetadataSchemaDocument.from_yaml_file(
                                PROPOSED_SCHEMA_PATH,
                                source_label="proposed",
                                create_if_missing=True,
                            )
                            proposed.upsert_process(process)
                            proposed.to_yaml_file(PROPOSED_SCHEMA_PATH)
                            reload_schema()
                            st.session_state.last_message = (
                                f"Saved proposed schema extension to: {PROPOSED_SCHEMA_PATH}"
                            )
                            st.rerun()
                        except ValidationError as exc:
                            st.error(str(exc))

            if processes:
                with st.expander("Add attribute to existing process"):
                    target_process_id = st.selectbox(
                        "Existing process",
                        [process.id for process in processes],
                        format_func=lambda pid: status_label(schema_doc.get_process(pid)),
                        key="add_attribute_process_id",
                    )
                    target_process = schema_doc.get_process(target_process_id)
                    if target_process:
                        if target_process.definition:
                            st.caption(target_process.definition)
                        render_add_parameter_form(
                            target_process,
                            form_key=f"overview_add_parameter_{target_process.id}",
                        )

        st.divider()
        st.subheader("Workflow")
        if exp.process_steps:
            workflow_rows = []
            sample_names = {sample.id: sample.name for sample in exp.samples}
            step_names = {step.id: step.name for step in exp.process_steps}
            for index, step in enumerate(exp.process_steps, start=1):
                workflow_rows.append(
                    {
                        "order": index,
                        "name": step.name,
                        "process": step.process_label,
                        "status": step.schema_status,
                        "samples": ", ".join(sample_names.get(sid, sid) for sid in step.sample_ids),
                        "predecessors": ", ".join(
                            step_names.get(sid, sid) for sid in step.predecessor_step_ids
                        ),
                    }
                )
            st.dataframe(workflow_rows, hide_index=True, width="stretch")
        else:
            st.caption("No workflow steps yet.")

    elif st.session_state.selected_sample_id is not None:
        sample = next(
            item for item in exp.samples if item.id == st.session_state.selected_sample_id
        )
        st.subheader(f"Sample: {sample.name}")

        if st.button("Back to overview"):
            back_to_overview()
            st.rerun()

        col_left, col_right = st.columns([2, 1])
        with col_left:
            sample.name = st.text_input("Sample name", sample.name)
            sample.material = st.text_input("Material", sample.material or "")
            sample.notes = st.text_area("Notes", sample.notes or "", height=140)

        with col_right:
            st.markdown("**Linked process steps**")
            related_steps = steps_for_sample(sample.id)
            if related_steps:
                for step in related_steps:
                    if st.button(
                        step.name,
                        key=f"sample_detail_step_{step.id}",
                        help=step_process_help(step),
                    ):
                        select_step(step.id)
                        st.rerun()
            else:
                st.caption("This sample is not linked to any process step yet.")

            st.divider()
            if st.button("Delete sample"):
                for step in exp.process_steps:
                    step.sample_ids = [sid for sid in step.sample_ids if sid != sample.id]
                exp.samples.remove(sample)
                back_to_overview()
                st.rerun()

    else:
        step = next(
            item for item in exp.process_steps if item.id == st.session_state.selected_step_id
        )
        process = schema_doc.get_process(step.process_id)
        st.subheader(f"Process step: {step.name}")
        if process and process.definition:
            st.caption(process.definition)
        if process and process.status == "proposed":
            st.info("This step uses a proposed process definition.")

        if st.button("Back to overview"):
            back_to_overview()
            st.rerun()

        col_left, col_right = st.columns([2, 1])
        with col_left:
            step.name = st.text_input("Step name", step.name)
            step.sample_ids = st.multiselect(
                "Linked samples",
                [sample.id for sample in exp.samples],
                default=step.sample_ids,
                format_func=lambda sid: next(
                    (sample.name for sample in exp.samples if sample.id == sid),
                    sid,
                ),
            )
            step.predecessor_step_ids = st.multiselect(
                "Preceded by workflow steps",
                [other.id for other in exp.process_steps if other.id != step.id],
                default=step.predecessor_step_ids,
                format_func=lambda sid: next(
                    (other.name for other in exp.process_steps if other.id == sid),
                    sid,
                ),
            )
            if process:
                st.markdown("**Parameters**")
                for parameter in process.parameters:
                    current_value = step.parameters.get(parameter.id)
                    step.parameters[parameter.id] = render_parameter_input(
                        parameter,
                        current_value,
                        key=f"edit_{step.id}_{parameter.id}",
                    )

                    if parameter.type == "enum":
                        with st.expander(f"Add missing allowed value for {parameter.label}"):
                            new_value = st.text_input(
                                "Allowed value",
                                key=f"enum_value_{step.id}_{parameter.id}",
                            )
                            value_reason = st.text_area(
                                "Why is this value needed?",
                                key=f"enum_reason_{step.id}_{parameter.id}",
                                height=80,
                            )
                            if st.button(
                                "Save allowed value proposal",
                                key=f"enum_save_{step.id}_{parameter.id}",
                            ):
                                try:
                                    schema_doc.add_proposed_allowed_value(
                                        PROPOSED_SCHEMA_PATH,
                                        process.id,
                                        parameter.id,
                                        new_value,
                                        value_reason,
                                    )
                                    add_schema_feedback(
                                        step,
                                        "missing_allowed_value",
                                        f"{parameter.id}:{new_value}",
                                        value_reason,
                                    )
                                    reload_schema()
                                    st.session_state.last_message = (
                                        f"Saved proposed schema extension to: {PROPOSED_SCHEMA_PATH}"
                                    )
                                    st.rerun()
                                except ValueError as exc:
                                    st.error(str(exc))

            step.notes = st.text_area("Notes", step.notes or "", height=140)

        with col_right:
            st.markdown("**Attachments**")
            uploaded_files = st.file_uploader(
                "Upload files",
                accept_multiple_files=True,
                key=f"files_{step.id}",
            )
            if uploaded_files and st.button("Store uploaded files"):
                folder = experiment_folder(DATA_DIR, exp)
                for uploaded_file in uploaded_files:
                    attachment = copy_uploaded_file(folder, uploaded_file)
                    step.attachments.append(attachment)
                st.success(f"Stored files in: {folder / 'attachments'}")

            for attachment in step.attachments:
                st.caption(f"{attachment.original_name} -> {attachment.stored_path}")

            st.divider()
            st.markdown("**Order**")
            step_index = exp.process_steps.index(step)
            move_col_a, move_col_b = st.columns(2)
            with move_col_a:
                if st.button("Move up", disabled=step_index == 0):
                    exp.process_steps[step_index - 1], exp.process_steps[step_index] = (
                        exp.process_steps[step_index],
                        exp.process_steps[step_index - 1],
                    )
                    st.rerun()
            with move_col_b:
                if st.button(
                    "Move down",
                    disabled=step_index == len(exp.process_steps) - 1,
                ):
                    exp.process_steps[step_index + 1], exp.process_steps[step_index] = (
                        exp.process_steps[step_index],
                        exp.process_steps[step_index + 1],
                    )
                    st.rerun()

            if st.button("Delete step"):
                exp.process_steps.remove(step)
                select_step(None)
                st.rerun()

        st.divider()
        with st.expander("Schema not sufficient? Add missing parameter"):
            if process:
                render_add_parameter_form(
                    process,
                    form_key=f"missing_parameter_{step.id}",
                    step=step,
                )
            else:
                st.error("Process definition not found.")

        warnings = schema_doc.validate_process_parameters(step.process_id, step.parameters)
        if warnings:
            st.warning("\n".join(warnings))

    with st.expander("Raw experiment JSON"):
        st.json(exp.model_dump(mode="json", exclude_none=True))


with page[1]:
    st.subheader("Schema browser")
    schema_search = st.text_input("Search schema", key="schema_search")
    for process in schema_doc.search_processes(schema_search):
        with st.expander(status_label(process)):
            st.write(process.definition or "No definition available.")
            st.caption(f"ID: {process.id} | Category: {process.category_id or '-'}")
            if process.synonyms:
                st.caption("Synonyms: " + ", ".join(process.synonyms))
            rows = []
            for parameter in process.parameters:
                rows.append(
                    {
                        "parameter": status_label(parameter),
                        "id": parameter.id,
                        "type": parameter.type,
                        "unit": parameter.unit or "",
                        "required": parameter.required,
                        "description": parameter.description or "",
                    }
                )
            if rows:
                st.dataframe(rows, hide_index=True, width="stretch")
            else:
                st.caption("No parameters defined.")

            with st.expander("Add proposed attribute to this process"):
                render_add_parameter_form(
                    process,
                    form_key=f"schema_browser_add_parameter_{process.id}",
                )


with page[2]:
    st.subheader("Settings")
    st.caption("Settings are stored locally and should not be committed to Git.")
    new_data_dir = st.text_input("Experiment output directory", str(DATA_DIR))
    if st.button("Save settings"):
        CONFIG.experiment_data_dir = new_data_dir
        save_config(CONFIG)
        st.session_state.last_message = f"Saved local config to: {APP_DIR / 'config' / 'local_config.json'}"
        st.rerun()

    st.divider()
    st.write(f"Official schema: `{OFFICIAL_SCHEMA_PATH}`")
    st.write(f"Proposed schema: `{PROPOSED_SCHEMA_PATH}`")
    st.write(f"Merged schema version: `{schema_doc.version}`")
