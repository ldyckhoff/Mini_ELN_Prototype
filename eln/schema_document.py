from __future__ import annotations

import importlib
import ast
import inspect
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, Field, create_model

from .ids import slugify


ParameterType = Literal["string", "number", "integer", "boolean", "date", "datetime", "enum"]
SchemaStatus = Literal["official", "proposed", "deprecated"]


class ParameterDefinition(BaseModel):
    id: str = Field(min_length=1)
    label: str = Field(min_length=1)
    type: ParameterType = "string"
    required: bool = False
    description: str | None = None
    unit: str | None = None
    allowed_values: list[str] | None = None
    example_values: list[Any] = Field(default_factory=list)
    status: SchemaStatus = "official"
    reason: str | None = None
    source_schema: str | None = None


class ProcessDefinition(BaseModel):
    id: str = Field(min_length=1)
    label: str = Field(min_length=1)
    category_id: str | None = None
    category_label: str | None = None
    hierarchy: list[str] = Field(default_factory=list)
    definition: str | None = None
    synonyms: list[str] = Field(default_factory=list)
    parameters: list[ParameterDefinition] = Field(default_factory=list)
    status: SchemaStatus = "official"
    proposed_by: str | None = None
    reason: str | None = None
    source_schema: str | None = None


class MetadataSchema(BaseModel):
    version: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    processes: list[ProcessDefinition] = Field(default_factory=list)


class MetadataSchemaDocument:
    """A readable object wrapper around YAML schema data and Pydantic models."""

    def __init__(
        self,
        data: dict[str, Any] | None = None,
        source_label: str = "memory",
        path: Path | None = None,
    ) -> None:
        self.path = path
        self.source_label = source_label
        self.raw: dict[str, Any] = data or {"version": datetime.now().strftime("%Y-%m-%d"), "processes": []}
        self.model = MetadataSchema.model_validate(self.raw)
        self._mark_source(source_label)
        self.raw = self.model.model_dump(mode="json", exclude_none=True)

    @property
    def version(self) -> str:
        return self.model.version

    @classmethod
    def empty(cls, source_label: str = "memory") -> "MetadataSchemaDocument":
        return cls(source_label=source_label)

    @classmethod
    def from_yaml_file(
        cls,
        path: Path,
        source_label: str,
        create_if_missing: bool = False,
        bootstrap_from_python_module: str | None = None,
    ) -> "MetadataSchemaDocument":
        if path.exists():
            data = load_yaml(path)
            return cls(data, source_label=source_label, path=path)

        if bootstrap_from_python_module:
            document = cls.from_python_classes(
                bootstrap_from_python_module,
                source_label=source_label,
            )
            document.to_yaml_file(path)
            return document

        if create_if_missing:
            document = cls.empty(source_label=source_label)
            document.to_yaml_file(path)
            return document

        return cls.empty(source_label=source_label)

    @classmethod
    def from_python_classes(
        cls,
        module_name: str,
        source_label: str = "official",
    ) -> "MetadataSchemaDocument":
        try:
            module = importlib.import_module(module_name)
        except Exception:
            source_file = Path(__file__).resolve().parents[1] / f"{module_name}.py"
            return cls.from_python_source_file(source_file, source_label)

        base_cls = getattr(module, "BaseModel")
        processes: list[ProcessDefinition] = []

        for _, process_cls in inspect.getmembers(module, inspect.isclass):
            if process_cls is base_cls:
                continue
            if not issubclass(process_cls, base_cls):
                continue
            if process_cls.__module__ != module.__name__:
                continue

            fields = getattr(process_cls, "model_fields", {})
            if not fields:
                continue

            base_names = [
                base.__name__
                for base in process_cls.__bases__
                if base.__name__ not in {"ProcessBase", "BaseModel"}
            ]
            category_label = base_names[0] if base_names else None
            category_id = class_name_to_process_id(category_label.replace("Process", "")) if category_label else None
            definition, synonyms = parse_process_docstring(inspect.getdoc(process_cls))
            parameters: list[ParameterDefinition] = []
            process_id = class_name_to_process_id(process_cls.__name__)
            process_label = camel_to_words(process_cls.__name__)

            for field_name, field_info in fields.items():
                extra = field_info.json_schema_extra or {}
                description = field_info.description
                if field_name == "process_identifier":
                    if field_info.default not in (None, "", ...):
                        process_id = slugify(str(field_info.default))
                    continue
                if field_name == "process_name":
                    if field_info.default not in (None, "", ...):
                        process_label = str(field_info.default)
                    continue
                if extra.get("source") == "definition":
                    definition = description or definition
                    synonyms = list(extra.get("synonyms") or [])
                    continue
                if extra.get("source") in {"preferred_name", "parent_process_name"}:
                    continue

                required_value = extra.get("required", "optional")
                parameters.append(
                    ParameterDefinition(
                        id=field_name,
                        label=field_name.replace("_", " ").title(),
                        type=infer_parameter_type(field_info.annotation),
                        required=required_value in {"required", "usually_required"},
                        description=description,
                        example_values=list(extra.get("example_values") or []),
                        status=source_label,
                        source_schema=source_label,
                    )
                )

            processes.append(
                ProcessDefinition(
                    id=process_id,
                    label=process_label,
                    category_id=category_id,
                    category_label=camel_to_words(category_label.replace("Process", "")) if category_label else None,
                    hierarchy=[*base_names, process_cls.__name__],
                    definition=definition,
                    synonyms=synonyms,
                    parameters=parameters,
                    status=source_label,
                    source_schema=source_label,
                )
            )

        document = cls(
            {
                "version": datetime.now().strftime("%Y-%m-%d"),
                "processes": [process.model_dump(mode="json", exclude_none=True) for process in processes],
            },
            source_label=source_label,
        )
        document.validate_unique_ids()
        return document

    @classmethod
    def from_python_source_file(
        cls,
        path: Path,
        source_label: str = "official",
    ) -> "MetadataSchemaDocument":
        """Export schema from generated Python source without importing it."""
        tree = ast.parse(path.read_text(encoding="utf-8"))
        processes: list[ProcessDefinition] = []

        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue

            fields = class_fields_from_ast(node)
            if not fields:
                continue

            base_names = [base_name_from_ast(base) for base in node.bases]
            base_names = [
                name for name in base_names if name and name not in {"ProcessBase", "BaseModel"}
            ]
            category_label = base_names[0] if base_names else None
            category_id = (
                class_name_to_process_id(category_label.replace("Process", ""))
                if category_label
                else None
            )
            definition, synonyms = parse_process_docstring(ast.get_docstring(node))
            parameters: list[ParameterDefinition] = []
            process_id = class_name_to_process_id(node.name)
            process_label = camel_to_words(node.name)

            for field_name, field_info in fields.items():
                extra = field_info.get("json_schema_extra") or {}
                description = field_info.get("description")
                if field_name == "process_identifier":
                    if field_info.get("default") not in (None, ""):
                        process_id = slugify(str(field_info["default"]))
                    continue
                if field_name == "process_name":
                    if field_info.get("default") not in (None, ""):
                        process_label = str(field_info["default"])
                    continue
                if extra.get("source") == "definition":
                    definition = description or definition
                    synonyms = list(extra.get("synonyms") or [])
                    continue
                if extra.get("source") in {"preferred_name", "parent_process_name"}:
                    continue

                required_value = extra.get("required", "optional")
                parameters.append(
                    ParameterDefinition(
                        id=field_name,
                        label=field_name.replace("_", " ").title(),
                        type=infer_parameter_type(field_info.get("annotation", "str")),
                        required=required_value in {"required", "usually_required"},
                        description=description,
                        example_values=list(extra.get("example_values") or []),
                        status=source_label,
                        source_schema=source_label,
                    )
                )

            processes.append(
                ProcessDefinition(
                    id=process_id,
                    label=process_label,
                    category_id=category_id,
                    category_label=camel_to_words(category_label.replace("Process", ""))
                    if category_label
                    else None,
                    hierarchy=[*base_names, node.name],
                    definition=definition,
                    synonyms=synonyms,
                    parameters=parameters,
                    status=source_label,
                    source_schema=source_label,
                )
            )

        document = cls(
            {
                "version": datetime.now().strftime("%Y-%m-%d"),
                "processes": [process.model_dump(mode="json", exclude_none=True) for process in processes],
            },
            source_label=source_label,
        )
        document.validate_unique_ids()
        return document

    def to_yaml_file(self, path: Path | None = None) -> Path:
        target = path or self.path
        if target is None:
            raise ValueError("No YAML target path was provided.")
        save_yaml(target, self.raw)
        self.path = target
        return target

    def merge_with(self, other: "MetadataSchemaDocument") -> "MetadataSchemaDocument":
        processes: dict[str, ProcessDefinition] = {
            process.id: process.model_copy(deep=True) for process in self.model.processes
        }

        for proposed_process in other.model.processes:
            if proposed_process.id not in processes:
                processes[proposed_process.id] = proposed_process.model_copy(deep=True)
                continue

            existing = processes[proposed_process.id]
            existing.parameters = merge_parameters(existing.parameters, proposed_process.parameters)
            if proposed_process.reason and not existing.reason:
                existing.reason = proposed_process.reason
            if proposed_process.definition and not existing.definition:
                existing.definition = proposed_process.definition

        merged = MetadataSchema(
            version=f"{self.version}+{other.version}",
            processes=sorted(processes.values(), key=lambda item: item.label.lower()),
        )
        return MetadataSchemaDocument(merged.model_dump(mode="json", exclude_none=True), "merged")

    def get_process(self, process_id: str) -> ProcessDefinition | None:
        return next((process for process in self.model.processes if process.id == process_id), None)

    def search_processes(self, text: str | None = None) -> list[ProcessDefinition]:
        if not text:
            return self.model.processes
        needle = text.lower().strip()
        return [
            process
            for process in self.model.processes
            if needle in process.id.lower()
            or needle in process.label.lower()
            or needle in (process.category_id or "").lower()
            or any(needle in synonym.lower() for synonym in process.synonyms)
        ]

    def upsert_process(self, process: ProcessDefinition) -> None:
        process.status = "proposed"
        process.source_schema = "proposed"
        for parameter in process.parameters:
            parameter.status = "proposed"
            parameter.source_schema = "proposed"

        existing = self.get_process(process.id)
        if existing:
            existing.label = process.label or existing.label
            existing.category_id = process.category_id or existing.category_id
            existing.definition = process.definition or existing.definition
            existing.reason = process.reason or existing.reason
            existing.parameters = merge_parameters(existing.parameters, process.parameters)
        else:
            self.model.processes.append(process)
        self.raw = self.model.model_dump(mode="json", exclude_none=True)
        self.validate_unique_ids()

    def add_proposed_parameter(
        self,
        proposed_schema_path: Path,
        process_id: str,
        process_label: str,
        parameter: ParameterDefinition,
    ) -> Path:
        proposed = MetadataSchemaDocument.from_yaml_file(
            proposed_schema_path,
            source_label="proposed",
            create_if_missing=True,
        )
        process = proposed.get_process(process_id)
        if process is None:
            process = ProcessDefinition(
                id=process_id,
                label=process_label,
                status="proposed",
                source_schema="proposed",
            )
            proposed.model.processes.append(process)

        parameter.status = "proposed"
        parameter.source_schema = "proposed"
        process.parameters = merge_parameters(process.parameters, [parameter])
        proposed.raw = proposed.model.model_dump(mode="json", exclude_none=True)
        proposed.validate_unique_ids()
        return proposed.to_yaml_file(proposed_schema_path)

    def add_proposed_allowed_value(
        self,
        proposed_schema_path: Path,
        process_id: str,
        parameter_id: str,
        value: str,
        reason: str | None,
    ) -> Path:
        if not value.strip():
            raise ValueError("Allowed value must not be empty.")

        process = self.get_process(process_id)
        if process is None:
            raise ValueError(f"Unknown process: {process_id}")
        parameter = next((item for item in process.parameters if item.id == parameter_id), None)
        if parameter is None:
            raise ValueError(f"Unknown parameter: {parameter_id}")

        proposed_parameter = parameter.model_copy(deep=True)
        proposed_parameter.status = "proposed"
        proposed_parameter.source_schema = "proposed"
        proposed_parameter.reason = reason
        values = list(proposed_parameter.allowed_values or [])
        if value not in values:
            values.append(value)
        proposed_parameter.allowed_values = values
        return self.add_proposed_parameter(
            proposed_schema_path,
            process_id,
            process.label,
            proposed_parameter,
        )

    def pydantic_model_for_process(self, process_id: str):
        process = self.get_process(process_id)
        if process is None:
            raise ValueError(f"Unknown process: {process_id}")
        fields: dict[str, tuple[Any, Any]] = {}
        for parameter in process.parameters:
            python_type = python_type_for_parameter(parameter)
            default = ... if parameter.required else None
            fields[parameter.id] = (python_type, default)
        return create_model(f"{slugify(process.id).title().replace('_', '')}Parameters", **fields)

    def validate_process_parameters(self, process_id: str, values: dict[str, Any]) -> list[str]:
        process = self.get_process(process_id)
        if process is None:
            return [f"Unknown process ID: {process_id}"]

        warnings: list[str] = []
        model = self.pydantic_model_for_process(process_id)
        relevant_values = {
            key: value
            for key, value in values.items()
            if any(parameter.id == key for parameter in process.parameters)
        }
        try:
            model.model_validate(relevant_values)
        except Exception as exc:
            warnings.append(f"Validation warning: {exc}")

        for parameter in process.parameters:
            value = values.get(parameter.id)
            if parameter.required and value in (None, "", []):
                warnings.append(f"Missing recommended field: {parameter.label}")
            if parameter.type == "enum" and value:
                allowed = parameter.allowed_values or []
                if allowed and value not in allowed:
                    warnings.append(f"{parameter.label} is not in the allowed values.")
        return warnings

    def used_proposed_items(self, process_id: str, values: dict[str, Any]) -> list[str]:
        process = self.get_process(process_id)
        if process is None:
            return []
        used: list[str] = []
        if process.status == "proposed":
            used.append(f"process:{process.id}")
        for parameter in process.parameters:
            if values.get(parameter.id) in (None, "", []):
                continue
            if parameter.status == "proposed":
                used.append(f"parameter:{parameter.id}")
        return sorted(set(used))

    def validate_unique_ids(self) -> None:
        process_ids = [process.id for process in self.model.processes]
        duplicate_processes = duplicates(process_ids)
        if duplicate_processes:
            raise ValueError(f"Duplicate process IDs: {', '.join(duplicate_processes)}")

        for process in self.model.processes:
            parameter_ids = [parameter.id for parameter in process.parameters]
            duplicate_parameters = duplicates(parameter_ids)
            if duplicate_parameters:
                raise ValueError(
                    f"Duplicate parameter IDs in {process.id}: {', '.join(duplicate_parameters)}"
                )

    def _mark_source(self, source_label: str) -> None:
        if source_label == "merged":
            return
        for process in self.model.processes:
            process.source_schema = process.source_schema or source_label
            process.status = process.status or source_label
            for parameter in process.parameters:
                parameter.source_schema = parameter.source_schema or source_label
                parameter.status = parameter.status or source_label


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    return data


def save_yaml(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(data, handle, sort_keys=False, allow_unicode=True)


def merge_parameters(
    base_parameters: list[ParameterDefinition],
    proposed_parameters: list[ParameterDefinition],
) -> list[ParameterDefinition]:
    merged = {parameter.id: parameter.model_copy(deep=True) for parameter in base_parameters}
    for parameter in proposed_parameters:
        if parameter.id in merged:
            existing = merged[parameter.id]
            if parameter.allowed_values:
                values = list(existing.allowed_values or [])
                for value in parameter.allowed_values:
                    if value not in values:
                        values.append(value)
                existing.allowed_values = values
            if parameter.status == "proposed":
                existing.status = "proposed"
            existing.reason = parameter.reason or existing.reason
            existing.source_schema = parameter.source_schema or existing.source_schema
        else:
            merged[parameter.id] = parameter.model_copy(deep=True)
    return list(merged.values())


def infer_parameter_type(annotation: Any) -> ParameterType:
    text = str(annotation).lower()
    if "bool" in text:
        return "boolean"
    if "int" in text:
        return "integer"
    if "float" in text or "decimal" in text:
        return "number"
    if "datetime" in text:
        return "datetime"
    if "date" in text:
        return "date"
    return "string"


def python_type_for_parameter(parameter: ParameterDefinition) -> Any:
    if parameter.type == "number":
        return float | None
    if parameter.type == "integer":
        return int | None
    if parameter.type == "boolean":
        return bool | None
    return str | None


def class_name_to_process_id(name: str) -> str:
    return slugify(camel_to_words(name))


def camel_to_words(name: str | None) -> str:
    if not name:
        return ""
    return re.sub(r"(?<!^)(?=[A-Z])", " ", name).strip()


def duplicates(values: list[str]) -> list[str]:
    seen = set()
    repeated = set()
    for value in values:
        if value in seen:
            repeated.add(value)
        seen.add(value)
    return sorted(repeated)


def class_fields_from_ast(node: ast.ClassDef) -> dict[str, dict[str, Any]]:
    fields: dict[str, dict[str, Any]] = {}
    for statement in node.body:
        if not isinstance(statement, ast.AnnAssign):
            continue
        if not isinstance(statement.target, ast.Name):
            continue

        field_data: dict[str, Any] = {
            "annotation": ast.unparse(statement.annotation),
            "default": None,
            "description": None,
            "json_schema_extra": {},
        }
        if isinstance(statement.value, ast.Call) and call_name(statement.value) == "Field":
            if statement.value.args:
                field_data["default"] = literal_or_none(statement.value.args[0])
            for keyword in statement.value.keywords:
                if keyword.arg in {"default", "description", "json_schema_extra"}:
                    field_data[keyword.arg] = literal_or_none(keyword.value)
        fields[statement.target.id] = field_data
    return fields


def base_name_from_ast(node: ast.expr) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        return node.attr
    return None


def call_name(node: ast.Call) -> str:
    if isinstance(node.func, ast.Name):
        return node.func.id
    if isinstance(node.func, ast.Attribute):
        return node.func.attr
    return ""


def literal_or_none(node: ast.AST) -> Any:
    try:
        return ast.literal_eval(node)
    except Exception:
        return None


def parse_process_docstring(docstring: str | None) -> tuple[str | None, list[str]]:
    if not docstring:
        return None, []

    definition_lines: list[str] = []
    synonyms: list[str] = []
    for raw_line in docstring.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.lower().startswith("synonyms:"):
            synonym_text = line.split(":", 1)[1]
            synonyms = [item.strip() for item in synonym_text.split(",") if item.strip()]
        else:
            definition_lines.append(line)

    return " ".join(definition_lines) or None, synonyms
