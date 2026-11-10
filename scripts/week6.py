from pathlib import Path
import click
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if (str(PROJECT_ROOT) not in sys.path):
    sys.path.insert(0, str(PROJECT_ROOT))

from src.database import run_query
from src.penguin_plotting import ( # noqa:  E402
    plot_body_mass_boxplot)


@click.command()
@click.option("--database", required=True)
@click.option("--query-file", required=True)
@click.option("--snapshot-file", required=True)
@click.option("--boxplot-file", required=True)
def main(database, query_file, snapshot_file, boxplot_file):
    database = Path(database)
    query_file = Path(query_file)
    snapshot_file = Path(snapshot_file)
    boxplot_file = Path(boxplot_file)
    query = query_file.read_text()
    df = run_query(database, query)
    print(df.head())
    df.to_csv(snapshot_file)
    plot_body_mass_boxplot(df, boxplot_file)


if __name__ == "__main__":
    main()
