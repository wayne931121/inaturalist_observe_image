import requests, re
account = input("請輸入帳號(please input account):")
password = input("請輸入密碼(please input password):")
r = requests.get("https://www.inaturalist.org/")
token = re.search('<meta name="csrf-token" content="(?P<token>[^"]+)"', r.text)["token"]
cookies = '_inaturalist_session:'+r.cookies.get_dict()['_inaturalist_session']
session = requests.Session()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
           "Origin": "https://www.inaturalist.org",
           "Referer": "https://www.inaturalist.org/users/sign_in",}
payload = {"utf8": "✓",
           "authenticity_token": token,
           "user[email]": account,
           "user[password]": password,
           "user[remember_me]": "0",
           "user[remember_me]": "1"}
#req = session.post('https://api.inaturalist.org/v1/computervision/score_image', data=payload, headers=headers, files=files)
req = session.post("https://www.inaturalist.org/session", data=payload, headers=headers, cookies=r.cookies)
result = req.content.decode(encoding="utf-8")
Authorization = re.search('<meta name="inaturalist-api-token" content="(?P<token>[^"]+)"', result)["token"]
print("Authorization:",Authorization)