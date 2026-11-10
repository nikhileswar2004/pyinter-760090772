from pathlib import Path
import pandas as pd
import click
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if (str(PROJECT_ROOT) not in sys.path):
    sys.path.insert(0, str(PROJECT_ROOT))

from src.olive_oil_plotting import ( # noqa:  E402
    plot_fatty_acid_pairs)
from src.olive_oil_summaries import ( # noqa:  E402
    summarise_olive_oil)

@click.command()
@click.option("--snapshot-file", required=True)
@click.option("--scatter-file", required=True)
@click.option("--summary-file", required=True)
def main(snapshot_file, scatter_file, summary_file):
    snapshot_file = Path(snapshot_file)
    scatter_file = Path(scatter_file)
    summary_file = Path(summary_file)
@click.command()
@click.option("--snapshot-file", required=True)
@click.option("--scatter-file", required=True)
@click.option("--summary-file", required=True)
def main(snapshot_file, scatter_file, summary_file):
    snapshot_file = Path(snapshot_file)
    scatter_file = Path(scatter_file)
    summary_file = Path(summary_file)
    # Load the snapshot CSV into a pandas DataFrame.
    #
    # In previous weeks the olive oil analysis used hard-coded filenames.
    # Your task is to adapt that code so it uses the command line
    # arguments provided above.
    #
    # Steps:
    # 1. Read the snapshot file into a DataFrame.
    # 2. Create the fatty acid pairwise scatterplot and save it to
    #    scatter_file.
    # 3. Generate the summary statistics table.
    # 4. Save the summary table as HTML to summary_file.
    #
    # Hint: Most of the code you need already exists in earlier exercises.
    # Hint 2: pd.read_csv will read from a csv


if __name__ == "__main__":
    main()
