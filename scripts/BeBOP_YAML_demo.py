"""Python version of BeBOP_YAML_demo.R.

Requires: pandas, PyYAML.
"""

from pathlib import Path
import re

import pandas as pd
import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def yaml_front_matter(file_path: Path) -> dict:
    """Read YAML front matter from a markdown file."""
    text = file_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, flags=re.DOTALL)
    if match is None:
        raise ValueError(f"No YAML front matter found in {file_path}")
    front_matter = yaml.safe_load(match.group(1)) or {}
    if not isinstance(front_matter, dict):
        raise ValueError(f"YAML front matter in {file_path} must be a mapping")
    return front_matter


def metadata_to_frame(file_path: Path) -> pd.DataFrame:
    metadata = yaml_front_matter(file_path)
    metadata["file_path"] = str(file_path)
    frame = pd.DataFrame([metadata])
    return frame.astype(str)


def main() -> None:
    first_file = PROJECT_ROOT / "examples" / "NOAA-PMEL-OME_eDNA_Collection_Protocol_Sterivex_PeristalticPump.md"
    second_file = PROJECT_ROOT / "examples" / "AOML_eDNA_Sampling_Protocol_Sterivex_Beads.md"
    output_file = PROJECT_ROOT / "examples" / "BeBOP_protocol_metadata_test.csv"

    df = metadata_to_frame(first_file)
    df2 = metadata_to_frame(second_file)
    df_comb = df.merge(df2, how="outer")
    df_comb.to_csv(output_file, index=False)


if __name__ == "__main__":
    main()