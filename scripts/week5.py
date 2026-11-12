
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.database import run_query  # noqa: E402
from src.olive_oil_plotting import (  # noqa: E402
    plot_fatty_acid_pairs,
    plot_fatty_acid_boxplot,
)
from src.olive_oil_summaries import (  # noqa: E402
    summarise_olive_oil,
)

# Read the SQL query
query = Path("sql/olive_oil.sql").read_text()

# Extract olive oil data from the database
df = run_query("data/inter.duckdb", query)

# Check that data has loaded
print(df.head())

# Save the extracted data
df.to_csv("artefacts/olive_oil.csv", index=False)

# Display available columns
print(df.columns)

# Generate the pairwise scatterplot matrix
plot_fatty_acid_pairs(
    df,
    "artefacts/olive_oil_pairwise_scatter.png"
)

# Generate the additional fatty acid box plot
plot_fatty_acid_boxplot(
    df,
    "artefacts/olive_oil_fatty_acids_boxplot.png"
)

# Generate summary statistics
summary_stats = summarise_olive_oil(df)

# Save summary statistics as HTML
with open("artefacts/olive_oil_summary.html", "w") as f:
    f.write(summary_stats.to_html())
