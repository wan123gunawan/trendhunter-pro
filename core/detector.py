def detect_explosion(series):
    growth = series.iloc[-1] - series.iloc[-7]

    if growth > 30:
        return "🚀 MELEDAK"
    elif growth > 10:
        return "🔥 NAIK"
    else:
        return "😴 BIASA"
