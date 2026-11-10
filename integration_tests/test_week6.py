from pathlib import Path
import subprocess


def test_week6_pipeline(tmp_path):
    snapshot_file = tmp_path / "penguins.csv"
    boxplot_file = tmp_path / "penguins_box.png"

    subprocess.run(
        [
            "python",
            "scripts/week6.py",
            "--database",
            "data/inter.duckdb",
            "--query-file",
            "sql/penguin_body_mass.sql",
            "--snapshot-file",
            str(snapshot_file),
            "--boxplot-file",
            str(boxplot_file),
        ],
        check=True,
    )

    assert snapshot_file.exists()
    assert boxplot_file.exists()
