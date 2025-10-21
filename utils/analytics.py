import pandas as pd

def analyze_logs():
    df = pd.read_json("chat_logs.jsonl", lines=True)
    return df.groupby(df['timestamp'].str[:10])['latency'].mean().reset_index()
