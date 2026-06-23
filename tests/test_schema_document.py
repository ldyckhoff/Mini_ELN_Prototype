from pathlib import Path

import pytest

from eln.schema_document import (
    MetadataSchemaDocument,
    ParameterDefinition,
    ProcessDefinition,
    load_yaml,
)


def test_load_and_merge_schema_layers(tmp_path: Path) -> None:
    official_path = tmp_path / "official.yaml"
    proposed_path = tmp_path / "proposed.yaml"

    official = MetadataSchemaDocument(
        {
            "version": "official-test",
            "processes": [
                {
                    "id": "annealing",
                    "label": "Annealing",
                    "parameters": [{"id": "temperature", "label": "Temperature"}],
                }
            ],
        },
        source_label="official",
    )
    official.to_yaml_file(official_path)

    proposed = MetadataSchemaDocument(
        {
            "version": "proposed-test",
            "processes": [
                {
                    "id": "annealing",
                    "label": "Annealing",
                    "parameters": [
                        {
                            "id": "ramp_rate",
                            "label": "Ramp rate",
                            "status": "proposed",
                        }
                    ],
                }
            ],
        },
        source_label="proposed",
    )
    proposed.to_yaml_file(proposed_path)

    merged = MetadataSchemaDocument.from_yaml_file(
        official_path,
        "official",
    ).merge_with(MetadataSchemaDocument.from_yaml_file(proposed_path, "proposed"))

    annealing = merged.get_process("annealing")
    assert annealing is not None
    assert {parameter.id for parameter in annealing.parameters} == {"temperature", "ramp_rate"}


def test_duplicate_process_ids_raise_error() -> None:
    document = MetadataSchemaDocument(
        {
            "processes": [
                {"id": "same", "label": "One"},
                {"id": "same", "label": "Two"},
            ]
        }
    )

    with pytest.raises(ValueError, match="Duplicate process IDs"):
        document.validate_unique_ids()


def test_duplicate_parameter_ids_raise_error() -> None:
    document = MetadataSchemaDocument(
        {
            "processes": [
                {
                    "id": "process",
                    "label": "Process",
                    "parameters": [
                        {"id": "same", "label": "One"},
                        {"id": "same", "label": "Two"},
                    ],
                }
            ]
        }
    )

    with pytest.raises(ValueError, match="Duplicate parameter IDs"):
        document.validate_unique_ids()


def test_save_proposed_parameter(tmp_path: Path) -> None:
    path = tmp_path / "student_extensions.yaml"
    document = MetadataSchemaDocument.empty("proposed")
    parameter = ParameterDefinition(
        id="ramp_rate",
        label="Ramp rate",
        type="number",
        status="proposed",
    )

    document.add_proposed_parameter(path, "annealing", "Annealing", parameter)
    data = load_yaml(path)

    assert data["processes"][0]["id"] == "annealing"
    assert data["processes"][0]["parameters"][0]["id"] == "ramp_rate"


def test_save_proposed_process(tmp_path: Path) -> None:
    path = tmp_path / "student_extensions.yaml"
    document = MetadataSchemaDocument.empty("proposed")
    document.upsert_process(
        ProcessDefinition(
            id="plasma_treatment",
            label="Plasma treatment",
            status="proposed",
            parameters=[ParameterDefinition(id="gas", label="Gas")],
        )
    )
    document.to_yaml_file(path)

    data = load_yaml(path)
    assert data["processes"][0]["id"] == "plasma_treatment"


def test_validate_experiment_values_against_schema() -> None:
    document = MetadataSchemaDocument(
        {
            "processes": [
                {
                    "id": "annealing",
                    "label": "Annealing",
                    "parameters": [
                        {
                            "id": "temperature",
                            "label": "Temperature",
                            "type": "number",
                            "required": True,
                        }
                    ],
                }
            ]
        }
    )

    warnings = document.validate_process_parameters("annealing", {"temperature": ""})
    assert warnings

