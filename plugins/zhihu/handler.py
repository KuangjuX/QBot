import requests

async def req_top_topic():
    url = "https://www.zhihu.com/api/v4/search/top_search"
    user_agent = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6"
    headers = {
        "User-Agent": user_agent
    }
    try:
        resp = requests.get(url=url, headers=headers)
        if resp.status_code == 200:
            return resp.json()["top_search"]["words"]

    except ConnectionError as e:
        print("[Error] " + e )
        return None