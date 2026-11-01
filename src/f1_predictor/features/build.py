import pandas as pd

def add_podium_target(df: pd.DataFrame) -> pd.DataFrame:
    # Position é o rótulo histórico, nunca uma variável preditora.
    out = df.copy()
    position = pd.to_numeric(out["Position"], errors="coerce")
    out["podium"] = position.between(1, 3).astype("int8")
    return out
