from pathlib import Path

import pandas as pd


RAW_PATH = Path("data/raw/events.csv")
OUT_PATH = Path("data/clean/events.csv")

VALID_EVENT_TYPES = {"click", "scroll", "view", "purchase", "login"}


def main() -> None:
    df = pd.read_csv(RAW_PATH)

    df = df.dropna(subset=["user_id", "timestamp", "event_type", "duration_seconds"])

    for column in ["user_id", "timestamp", "event_type", "duration_seconds"]:
        df = df[df[column].astype(str).str.strip() != ""]

    df["event_type"] = df["event_type"].astype(str).str.strip().str.lower()
    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
    df = df[df["duration_seconds"] > 0]
    df["duration_seconds"] = df["duration_seconds"].astype(int)


    timestamps = pd.to_datetime(df["timestamp"], errors="coerce", format="mixed")
    df = df[timestamps.notna()].copy()
    df["timestamp"] = timestamps[timestamps.notna()].dt.strftime("%Y-%m-%dT%H:%M:%S")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)


if __name__ == "__main__":
    main()
