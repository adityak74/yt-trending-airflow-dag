from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import json

BASE_URL = 'http://www.youtube.com'

def get_youtube_trending_api():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    path_to_chromedriver = os.path.join(os.getcwd(), 'airflow', 'dags', 'src', 'chromedriver') # change path as needed
    browser = webdriver.Chrome(executable_path = path_to_chromedriver, options=chrome_options)

    url = 'https://www.youtube.com/feed/trending'
    browser.get(url)
    browser.implicitly_wait(30)

    soup = BeautifulSoup(browser.page_source, features="html.parser")

    all_videos = soup.find_all('ytd-video-renderer')
    all_videos_scraped = []
    for video in all_videos:
        video_a = video.find('a', 'yt-simple-endpoint style-scope ytd-video-renderer')
        video_link = video_a['href']
        video_title = video_a['title']
        video_channel_data = video.find('yt-formatted-string', 'style-scope ytd-channel-name complex-string')
        video_channel_a = video_channel_data.find('a', 'yt-simple-endpoint style-scope yt-formatted-string')
        video_channel_name = video_channel_a.text
        video_channel_link = video_channel_a['href']

        video_views = video.find_all('span', 'style-scope ytd-video-meta-block')[0].text

        all_videos_scraped.append({
            'title': video_title,
            'link':  BASE_URL + video_link,
            'channel': {
                'name': video_channel_name,
                'link': BASE_URL + video_channel_link
            },
            'views': video_views
        })

    browser.close()

    return json.dumps(all_videos_scraped)
