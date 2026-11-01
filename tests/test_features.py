import pandas as pd
from f1_predictor.features.build import add_podium_target

def test_add_podium_target():
    df = pd.DataFrame({"Position": [1, 2, 3, 4, None]})
    assert add_podium_target(df)["podium"].tolist() == [1, 1, 1, 0, 0]
