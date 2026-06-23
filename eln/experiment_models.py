from __future__ import annotations

from datetime import date, datetime
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field

from .ids import make_id


class Attachment(BaseModel):
    id: str = Field(default_factory=lambda: make_id("file"))
    original_name: str
    stored_path: str
    description: str | None = None
    attached_at: datetime = Field(default_factory=datetime.now)


class Sample(BaseModel):
    id: str = Field(default_factory=lambda: make_id("sample"))
    name: str
    material: str | None = None
    notes: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)


class GenericProcessStep(BaseModel):
    id: str = Field(default_factory=lambda: make_id("step"))
    name: str
    process_id: str
    process_label: str
    schema_status: Literal["official", "proposed", "deprecated"] = "official"
    sample_ids: list[str] = Field(default_factory=list)
    predecessor_step_ids: list[str] = Field(default_factory=list)
    parameters: dict[str, Any] = Field(default_factory=dict)
    notes: str | None = None
    attachments: list[Attachment] = Field(default_factory=list)
    schema_feedback: list[dict[str, Any]] = Field(default_factory=list)
    used_proposed_schema_items: list[str] = Field(default_factory=list)
    schema_version: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class Experiment(BaseModel):
    id: str = Field(default_factory=lambda: make_id("exp"))
    name: str = ""
    project: str | None = None
    objective: str | None = None
    operator: str | None = None
    experiment_date: date | None = Field(default_factory=date.today)
    samples: list[Sample] = Field(default_factory=list)
    process_steps: list[GenericProcessStep] = Field(default_factory=list)
    attachments: list[Attachment] = Field(default_factory=list)
    schema_version: str | None = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @property
    def folder_name(self) -> str:
        return self.id

    def relative_file_path(self) -> Path:
        return Path(self.folder_name) / "experiment.json"

