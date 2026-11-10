def summarise_body_mass(df):
    """
    Calculate summary statistics for penguin body mass grouped by sex.

    Parameters
    ----------
    df : pandas.DataFrame
        A DataFrame containing at least the columns 'sex' and
        'body_mass_g'.

    Returns
    -------
    pandas.DataFrame
        A DataFrame indexed by sex containing the following summary
        statistics for body mass:

        - count: number of non-missing observations
        - mean: average body mass
        - std: standard deviation of body mass
        - minimum: smallest body mass
        - maximum: largest body mass

    Examples
    --------
    >>> summary = summarise_body_mass(df)
    >>> print(summary.loc["male", "mean"])
    """
    pass
