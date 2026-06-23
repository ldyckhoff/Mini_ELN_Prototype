from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from .experiment_models import Attachment, Experiment
from .ids import slugify


APP_DIR = Path(__file__).resolve().parents[1]
CONFIG_PATH = APP_DIR / "config" / "local_config.json"


class LocalConfig(BaseModel):
    experiment_data_dir: str = str(APP_DIR / "experiments")


def load_config() -> LocalConfig:
    if not CONFIG_PATH.exists():
        config = LocalConfig()
        save_config(config)
        return config

    with CONFIG_PATH.open("r", encoding="utf-8") as handle:
        config = LocalConfig.model_validate(json.load(handle))

    Path(config.experiment_data_dir).mkdir(parents=True, exist_ok=True)
    return config


def save_config(config: LocalConfig) -> Path:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    Path(config.experiment_data_dir).mkdir(parents=True, exist_ok=True)
    with CONFIG_PATH.open("w", encoding="utf-8") as handle:
        json.dump(config.model_dump(mode="json"), handle, indent=2)
    return CONFIG_PATH


def experiment_folder(data_dir: Path, experiment: Experiment) -> Path:
    folder = data_dir / experiment.folder_name
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "attachments").mkdir(exist_ok=True)
    return folder


def save_experiment(experiment: Experiment, data_dir: Path) -> Path:
    folder = experiment_folder(data_dir, experiment)
    path = folder / "experiment.json"
    with path.open("w", encoding="utf-8") as handle:
        json.dump(experiment.model_dump(mode="json", exclude_none=True), handle, indent=2)
    return path


def load_experiment(data_dir: Path, experiment_id: str) -> Experiment:
    path = data_dir / experiment_id / "experiment.json"
    with path.open("r", encoding="utf-8") as handle:
        return Experiment.model_validate(json.load(handle))


def list_experiments(data_dir: Path) -> list[dict[str, Any]]:
    data_dir.mkdir(parents=True, exist_ok=True)
    experiments: list[dict[str, Any]] = []
    for path in sorted(data_dir.glob("*/experiment.json")):
        try:
            with path.open("r", encoding="utf-8") as handle:
                data = json.load(handle)
            experiments.append(
                {
                    "id": data.get("id", path.parent.name),
                    "name": data.get("name") or "(unnamed)",
                    "path": str(path),
                    "updated_at": data.get("updated_at", ""),
                }
            )
        except (OSError, json.JSONDecodeError):
            continue
    return sorted(experiments, key=lambda item: item["updated_at"], reverse=True)


def delete_experiment_folder(data_dir: Path, experiment_id: str) -> None:
    folder = data_dir / experiment_id
    if folder.exists() and folder.is_dir():
        shutil.rmtree(folder)


def copy_uploaded_file(experiment_dir: Path, uploaded_file) -> Attachment:
    attachment_dir = experiment_dir / "attachments"
    attachment_dir.mkdir(parents=True, exist_ok=True)
    target_name = f"{slugify(Path(uploaded_file.name).stem)}{Path(uploaded_file.name).suffix}"
    target = attachment_dir / target_name
    counter = 1
    while target.exists():
        target = attachment_dir / f"{slugify(Path(uploaded_file.name).stem)}_{counter}{Path(uploaded_file.name).suffix}"
        counter += 1

    with target.open("wb") as handle:
        handle.write(uploaded_file.getbuffer())

    return Attachment(
        original_name=uploaded_file.name,
        stored_path=str(target.relative_to(experiment_dir)),
    )

