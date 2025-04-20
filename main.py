import requests
from bs4 import BeautifulSoup

def download_pinterest_video(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # نبحث عن الفيديوهات داخل الوسوم
    for tag in soup.find_all("video"):
        video_url = tag.get("src")
        if video_url:
            print(f"جارٍ تحميل الفيديو من: {video_url}")
            video_data = requests.get(video_url, headers=headers).content

            with open("pinterest_video.mp4", "wb") as f:
                f.write(video_data)
                print("تم حفظ الفيديو باسم pinterest_video.mp4")
            return

    print("لم يتم العثور على فيديو في الرابط!")

# مثال تشغيل
if __name__ == "__main__":
    link = input("أدخل رابط فيديو Pinterest: ")
    download_pinterest_video(link)