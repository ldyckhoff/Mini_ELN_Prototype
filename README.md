# Pilot ELN

Pilot ELN is a small Streamlit-based electronic lab notebook for documenting experimental fabrication workflows while testing and improving a metadata schema.

The current version is focused on fabrication steps for nanoporous metals, especially dealloying-related workflows. The included metadata schema contains preliminary process names and process parameters. Users can document experiments, link samples to process steps, attach local files, and propose missing schema attributes directly from the app.

Experimental data stays on your local computer. The app does not upload experiment records or attached files.

Note! While the app does not require knowledge in python programming, a local python installation on your local computer is required to run the app. 

## Main Features

- Create, edit, save, load, and delete local experiment records.
- Document samples and link them to process steps.
- Build ordered fabrication workflows from schema-defined processes.
- Add parameters for each process step using dynamic forms.
- Attach local files to process steps, such as images, tables, spectra, or instrument exports.
- Automatically create experiment, sample, process-step, and file IDs.
- Store each experiment in its own local folder.
- Browse the current metadata schema.
- Propose missing process parameters without editing Python code.
- Save proposed schema extensions to `schemas/proposed/student_extensions.yaml`.

## Planned features:

- Process graph visualization.
- Filtering experiments by process parameters.
- Improved schema feedback export.
- Optional AI-assisted extraction from notes or documents.

## What This App Is For

Use this app if you want to:

- Document fabrication experiments in a structured and connected way.
- Test whether the current metadata schema is useful for real lab work.
- Identify missing process parameters during daily documentation.
- Collect schema improvement suggestions from students or researchers.
- Keep experiment records local while still producing reviewable schema feedback.

This app is currently a pilot tool, not a finalized institutional ELN.

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
