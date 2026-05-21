import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import pandas as pd
    return mo, pd, plt


@app.cell
def _(pd):
    events = pd.read_csv("data/features/events.csv")
    events
    return (events,)


@app.cell
def _(events, plt):
    fig, ax = plt.subplots()
    ax.hist(events["duration_minutes"], bins=20, edgecolor="black")
    ax.set_xlabel("Duration (minutes)")
    ax.set_ylabel("Event count")
    ax.set_title("Distribution of Event Durations")
    fig
    return ax, fig


if __name__ == "__main__":
    app.run()
