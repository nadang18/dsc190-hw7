from pathlib import Path

import pandas as pd


IN_PATH = Path("data/clean/events.csv")
OUT_PATH = Path("data/transformed/events.csv")


def main() -> None:
    df = pd.read_csv(IN_PATH)
    df["date"] = pd.to_datetime(df["timestamp"]).dt.strftime("%Y-%m-%d")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)


if __name__ == "__main__":
    main()
