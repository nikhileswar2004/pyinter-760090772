
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.database import run_query  # noqa: E402
from src.penguin_plotting import (  # noqa: E402
    plot_body_mass_histogram,
    plot_body_mass_boxplot,
)
from src.penguin_summaries import summarise_body_mass  # noqa: E402


# Read the SQL query
query = Path("sql/penguin_body_mass.sql").read_text()

# Extract penguin data from the database
df = run_query("data/inter.duckdb", query)

# Check that data has been loaded
print(df.head())

# Save the extracted data
df.to_csv("artefacts/penguins.csv", index=False)

# Generate summary statistics using the reusable function
summary = summarise_body_mass(df)

# Print the summary
print(summary)

# Write the summary to a file
with open("artefacts/body_mass_summary.txt", "w") as f:
    f.write(summary.to_string())

# Plot the body mass histogram
plot_body_mass_histogram(df, "artefacts/penguins_mass.png")

# Plot the body mass boxplot
plot_body_mass_boxplot(df, "artefacts/penguins_mass_by_sex.png")
