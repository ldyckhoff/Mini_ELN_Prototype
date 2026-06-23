# Pilot ELN

This is a small Streamlit ELN for documenting experiments while testing a metadata schema.

## Install

From `MetaData_App`:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```powershell
streamlit run app.py
```

On Windows, you can also use the helper launcher:

```powershell
.\run_app.ps1
```

If you see `No module named yaml`, the active Python environment is missing `PyYAML`. Install the dependencies from this folder:

```powershell
python -m pip install -r requirements.txt
```

On first run, the app creates:

- `config/local_config.json` for local settings.
- `experiments/` for local experiment folders.
- `schemas/official/processes.yaml` from `generated_process_classes.py` if it does not exist.
- `schemas/proposed/student_extensions.yaml` for proposed schema additions.

## Data Layout

Each experiment is saved in its own folder:

```text
experiments/
  exp_abc123def0/
    experiment.json
    attachments/
      image_or_instrument_file.ext
```

The experiment JSON stores experiment IDs, sample IDs, process step IDs, timestamps, linked samples, workflow predecessors, schema version, and proposed schema usage.

## Local Settings

Use the Settings tab to change the experiment output directory. The setting is written to:

```text
config/local_config.json
```

This file is local machine configuration and should not be committed.

## Schema Files

Official schema:

```text
schemas/official/processes.yaml
```

Proposed student extensions:

```text
schemas/proposed/student_extensions.yaml
```

The official schema is generated from `generated_process_classes.py` and should be treated as read-only in the app. Proposed processes, parameters, and enum values are saved to `student_extensions.yaml` and are usable immediately.

To regenerate the official YAML:

```powershell
python scripts/export_schema_to_yaml.py
```

## What To Commit

Commit:

- App source code.
- `schemas/proposed/student_extensions.yaml` when proposals should be reviewed.
- `schemas/official/processes.yaml` if the generated official schema should be versioned.

Do not commit:

- Local experiment data unless intentionally exporting anonymized examples.
- `config/local_config.json`.
- Local databases or temporary files.
