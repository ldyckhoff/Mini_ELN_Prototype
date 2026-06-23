from __future__ import annotations

import sys
from pathlib import Path


APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from eln.schema_document import MetadataSchemaDocument  # noqa: E402


def main() -> None:
    target = APP_DIR / "schemas" / "official" / "processes.yaml"
    document = MetadataSchemaDocument.from_python_classes(
        "generated_process_classes",
        source_label="official",
    )
    document.to_yaml_file(target)
    print(f"Exported official schema to: {target}")
    print(f"Processes: {len(document.model.processes)}")


if __name__ == "__main__":
    main()

