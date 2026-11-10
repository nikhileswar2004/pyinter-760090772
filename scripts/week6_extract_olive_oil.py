from pathlib import Path
import click
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if (str(PROJECT_ROOT) not in sys.path):
    sys.path.insert(0, str(PROJECT_ROOT))

from src.database import run_query


@click.command()
@click.option("--database", required=True)
@click.option("--query-file", required=True)
@click.option("--snapshot-file", required=True)
def main(database, query_file, snapshot_file):
    database = Path(database)
    query_file = Path(query_file)
    snapshot_file = Path(snapshot_file)
    # TODO:
    # Read the SQL query from query_file.
    #
    # Hint: Path objects have a read_text() method that was used in the
    # penguin example.
    # Hint 2: In previous weeks you did this with hard coded paths in the script
    query = # TODO
    # TODO:
    # Run the query against the database and store the result in a
    # pandas DataFrame.
    #
    # Hint: The run_query() function takes two arguments:
    #   1. The database path
    #   2. The SQL query text
    #
    # Look back at the penguin example if you are unsure or previous weeks
    df = # TODO
    print(df.head())
    df.to_csv(snapshot_file)


if __name__ == "__main__":
    main()
