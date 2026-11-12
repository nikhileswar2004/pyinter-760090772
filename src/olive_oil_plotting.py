
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


FATTY_ACIDS = [
    "palmitic",
    "palmitoleic",
    "stearic",
    "oleic",
    "linoleic",
    "linolenic",
    "arachidic",
    "eicosenoic",
    "other"
]


def plot_fatty_acid_pairs(df, output_file):
    """
    Create a pairwise scatterplot matrix for fatty acid measurements.
    """
    scatter_matrix(
        df[FATTY_ACIDS],
        figsize=(15, 15),
        diagonal="hist",
        alpha=0.7
    )

    plt.suptitle(
        "Pairwise Relationships Between Fatty Acids in Italian Olive Oil",
        y=1.02
    )
    plt.tight_layout()
    plt.savefig(output_file, bbox_inches="tight")
    plt.close()


def plot_fatty_acid_boxplot(df, output_file):
    """
    Create box plots comparing the distributions of fatty acids.
    """
    df[FATTY_ACIDS].plot(
        kind="box",
        figsize=(12, 7),
        rot=45
    )

    plt.title("Distribution of Fatty Acids in Italian Olive Oil")
    plt.xlabel("Fatty Acid")
    plt.ylabel("Measurement")
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
