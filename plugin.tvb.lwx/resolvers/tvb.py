import requests


INEWS_URL = "https://inews-api.tvb.com/news/checkout/live/hd/ott_NEVT2_h264?profile=safari"
NEWS_URL = "https://inews-api.tvb.com/news/checkout/live/hd/ott_I-NEWS_h264?profile=safari"
FINANCE_URL = "https://inews-api.tvb.com/news/checkout/live/hd/ott_I-FINA_h264?profile=safari"


def get_tokenized_link(channel: str) -> dict:
    urls = {
        'news': NEWS_URL,
        'finance': FINANCE_URL,
        'inews': INEWS_URL,
    }

    url = urls[channel]

    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()['content']['url']['hd']
