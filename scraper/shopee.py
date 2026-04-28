import requests

def scrape_shopee(keyword):
    try:
        url = f"https://shopee.co.id/api/v4/search/search_items?keyword={keyword}"
        res = requests.get(url).json()

        items = res.get("items", [])
        results = []

        for item in items[:5]:
            data = item["item_basic"]
            results.append({
                "nama": data["name"],
                "terjual": data["historical_sold"],
                "harga": data["price"] / 100000
            })

        return results
    except:
        return []
