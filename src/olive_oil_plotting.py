from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


def plot_fatty_acid_pairs(df, output_file):
    """
    Create a pairwise scatterplot matrix for fatty acid measurements.

    Parameters
    ----------
    df : pandas.DataFrame
        Olive oil data containing fatty acid measurements.

    output_file : str
        Path to the image file to be created.
    """
    fatty_acids = ["palmitic", "palmitoleic", "stearic", "oleic"]
    scatter_matrix(df[fatty_acids], figsize=(12, 12), diagonal="hist", alpha=0.7)
    plt.suptitle("TODO")
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
