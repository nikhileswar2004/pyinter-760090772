import pandas as pd
from src.penguin_summaries import summarise_body_mass


def test_summarise_body_mass():
    df = pd.DataFrame(
        {
            "sex": ["male", "male", "female"],
            "body_mass_g": [4000, 5000, 3000],
        }
    )
    result = summarise_body_mass(df)

    assert result.loc["male", "count"] == 2
    assert result.loc["male", "mean"] == 4500

    assert result.loc["female", "count"] == 1
    assert result.loc["female", "mean"] == 3000

    assert result.loc["male", "minimum"] == 4000
    assert result.loc["male", "maximum"] == 5000
