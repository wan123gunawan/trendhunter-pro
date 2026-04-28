from pytrends.request import TrendReq

pytrends = TrendReq(hl='id-ID', tz=360)

def get_trend(keyword):
    pytrends.build_payload([keyword], timeframe='today 3-m')
    data = pytrends.interest_over_time()
    return data
