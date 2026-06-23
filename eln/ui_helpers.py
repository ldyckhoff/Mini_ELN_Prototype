from __future__ import annotations

from datetime import date
from typing import Any

import streamlit as st

from .schema_document import ParameterDefinition, ProcessDefinition


def status_label(item: ProcessDefinition | ParameterDefinition | None) -> str:
    if item is None:
        return ""
    marker = " [proposed]" if item.status == "proposed" else ""
    return f"{item.label}{marker}"


def render_parameter_input(
    parameter: ParameterDefinition,
    current_value: Any = None,
    key: str | None = None,
) -> Any:
    label = status_label(parameter)
    if parameter.unit:
        label = f"{label} ({parameter.unit})"
    help_text = parameter.description

    if parameter.type == "number":
        value = float(current_value) if current_value not in (None, "") else 0.0
        return st.number_input(label, value=value, help=help_text, key=key)

    if parameter.type == "integer":
        value = int(current_value) if current_value not in (None, "") else 0
        return st.number_input(label, value=value, step=1, help=help_text, key=key)

    if parameter.type == "boolean":
        return st.checkbox(label, value=bool(current_value), help=help_text, key=key)

    if parameter.type == "enum":
        options = parameter.allowed_values or []
        if not options:
            return st.text_input(label, value=str(current_value or ""), help=help_text, key=key)
        selected_index = options.index(current_value) if current_value in options else 0
        return st.selectbox(label, options, index=selected_index, help=help_text, key=key)

    if parameter.type == "date":
        value = current_value or date.today()
        return st.date_input(label, value=value, help=help_text, key=key)

    if parameter.type == "datetime":
        return st.text_input(
            label,
            value=str(current_value or ""),
            help=help_text or "Use ISO format, for example 2026-06-22 14:30.",
            key=key,
        )

    return st.text_input(label, value=str(current_value or ""), help=help_text, key=key)

