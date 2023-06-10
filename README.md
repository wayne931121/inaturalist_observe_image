# inaturalist_observe_image
將圖片進行上傳，你將會知道他是什麼品種(需要個人認證資料)。 Upload Image RAW, You Can Know What Species Is.(User Auth Data Is Required)

## 影片:<br>
[操作範例](https://drive.google.com/file/d/1HNQ4vhQ4oRoXTUrX3vZus1_WxbURRUAS/view?usp=sharing) <br>
[取得個人認證資訊](https://drive.google.com/file/d/1wO8a6X6ZAdeABOSLM298VO0HGr9LFNoo/view?usp=sharing)
```cmd
C:\> python iNaturalist-Authorization.py
請輸入帳號(please input account): ???
請輸入密碼(please input password): ???
Authorization: ???
```

## 提醒:<br>
記得將server.py裡面的第25行換成自己的認證資料，這個資料可能有期限，等期限到了後須重新再取得一次。<br>
https://github.com/wayne931121/inaturalist_observe_image/blob/main/server.py#L25 <br>
<img src="https://github.com/wayne931121/inaturalist_observe_image/assets/75261164/f0f7eb4a-51d4-4de4-af62-7a41bd2f44c6" width=490>
