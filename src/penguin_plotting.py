import matplotlib.pyplot as plt


def plot_body_mass_histogram(df, output_file):
    plt.hist(df["body_mass_g"])
    plt.title("TODO")
    plt.xlabel("TODO")
    plt.ylabel("TODO")
    plt.savefig(output_file)
    plt.close()


def plot_body_mass_boxplot(df, output_file):
    male = df[df["sex"] == "male"]["body_mass_g"]
    female = df[df["sex"] == "female"]["body_mass_g"]
    plt.boxplot([female, male], tick_labels=["Female", "Male"])
    plt.title("Body mass by sex")
    plt.xlabel("Sex")
    plt.ylabel("Body mass (g)")
    plt.savefig(output_file)
    plt.close()
