import os
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import googleapiclient.discovery

# API information
api_service_name = "youtube"
api_version = "v3"
# DEVELOPER_KEY = 'AIzaSyCzpUUEsO_UoSPaBtKRy-qL4283rvAPvao'
DEVELOPER_KEY = 'AIzaSyCHQIhXSoa0z6EuRLvHerRhQIy_OdMpMd4'

# API client
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)

def get_video_details(youtube, video_list):
    stats_list = []

    for i in range(0, len(video_list), 50):
        request = youtube.videos().list(
            part="snippet,statistics,contentDetails",
            id=video_list[i:i+50]
        )

        data = request.execute()

        for video in data['items']:
            title = video['snippet']['title']
            published_at = video['snippet']['publishedAt']
            views = video['statistics'].get('viewCount', 0)
            likes = video['statistics'].get('likeCount', 0)

            stat_dictionary = dict(
                title=title,
                published_at=published_at,
                views=views,
                likes=likes
            )

            stats_list.append(stat_dictionary)

    return stats_list


video_list = get_video_details(youtube, playlist_id)
