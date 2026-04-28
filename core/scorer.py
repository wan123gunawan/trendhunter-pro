def calculate_score(series):
    growth = series.iloc[-1] - series.iloc[0]
    spike = series.max()
    stability = series.mean()

    score = (growth * 0.5) + (spike * 0.3) + (stability * 0.2)
    return round(score, 2)
