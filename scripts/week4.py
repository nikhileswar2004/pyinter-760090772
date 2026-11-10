from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if (str(PROJECT_ROOT) not in sys.path):
    sys.path.insert(0, str(PROJECT_ROOT))

from src.database import run_query # noqa:  E402
from src.penguin_plotting import ( # noqa:  E402
    plot_body_mass_histogram, plot_body_mass_boxplot)


query = Path("sql/penguin_body_mass.sql").read_text()
df = run_query("data/inter.duckdb", query)
# Check we have loaded data
print(df.head())
df.to_csv("artefacts/penguins.csv")
# Produce a summary
# Move this code to a testable function and import it
summary = (df.groupby("sex")["body_mass_g"].agg(count="count",
                                                mean="mean",
                                                std="std",
                                                minimum="min",
                                                maximum="max"))
# Write the summary to file
with open("artefacts/body_mass_summary.txt", "w") as f:
    f.write(summary.to_string())
# Plot the body mass histogram
plot_body_mass_histogram(df, "artefacts/penguins_mass.png")
# Plot the body mass boxplot
plot_body_mass_boxplot(df, "artefacts/penguins_mass_by_sex.png")
