import urllib.request
import json

if __name__ == '__main__':

    API_URL = "https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk"
    post_data = {
        "apikey" : "XXXXXXXXXXXXXXXXXXXXXXXXXX",
        "query" : "‚±‚ñ‚Î‚ñ‚í",
                }

    encoded_post_data = urllib.parse.urlencode(post_data).encode(encoding='utf-8')
    page_text = ""

    with urllib.request.urlopen(url=API_URL, data=encoded_post_data) as page:
        for line in page.readlines():
            page_text = page_text + line.decode('utf-8')
    data = json.loads(page_text)
    print(data["results"])
