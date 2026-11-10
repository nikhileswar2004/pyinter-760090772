from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if (str(PROJECT_ROOT) not in sys.path):
    sys.path.insert(0, str(PROJECT_ROOT))

from src.database import run_query # noqa:  E402
from src.olive_oil_plotting import ( # noqa:  E402
    plot_fatty_acid_pairs)
from src.olive_oil_summaries import ( # noqa:  E402
    summarise_olive_oil)

query = Path("sql/olive_oil.sql").read_text()
df = run_query("data/inter.duckdb", query)
# Check we have loaded data
print(df.head())
df.to_csv("artefacts/olive_oil.csv")
# Get all column names
print(df.columns)

plot_fatty_acid_pairs(df, "artefacts/olive_oil_pairwise_scatter")

summary_stats = summarise_olive_oil(df)
with open("artefacts/olive_oil_summary.html", "w") as f:
    f.write(summary_stats.to_html())

