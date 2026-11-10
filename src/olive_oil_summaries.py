def summarise_olive_oil(df):
    """
    Calculate summary statistics for fatty acid data.

    Parameters
    ----------
    df : pandas.DataFrame
        A DataFrame containing the olive oil data.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the following summary
        statistics for each fatty acid:

        - count: number of non-missing observations
        - mean: average oil content
        - std: standard deviation of oil content
        - min: smallest oil content
        - max: largest oil content

    Examples
    --------
    >>> summary = summarise_olive_oil(df)
    """
    fatty_acids = ["palmitic", "palmitoleic", "stearic", "oleic"]
    return (df[fatty_acids].agg(["count", "mean", "std", "min", "max"]))
