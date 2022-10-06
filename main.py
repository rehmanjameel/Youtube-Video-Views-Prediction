import os
# API client library
import googleapiclient.discovery
import seaborn as sb
import matplotlib.pyplot as plt

# API information
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = 'AIzaSyCHQIhXSoa0z6EuRLvHerRhQIy_OdMpMd4'
import pandas as pd

# API client
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, developerKey=DEVELOPER_KEY)
# Cats query
same_beef_song = youtube.search().list(
    part="id,snippet",
    type='video',
    # regionCode="US",
    # order="relevance",
    q="Same beef",
    maxResults=1,
    fields="items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
).execute()
response = same_beef_song
print("hye1 ", response)
# Dogs query
so_high_song = youtube.search().list(
    part="id,snippet",
    type='video',
    # regionCode="US",
    # order="relevance",
    q="SO High",
    maxResults=1,
    fields="items(id(videoId),snippet(publishedAt,channelId,channelTitle,title,description))"
).execute()

response = so_high_song
print("hye ", response)
# Dictionary to store cats video data
same_beef = {
    'id': [],
    'duration': [],
    'views': [],
    'likes': [],
    'title': [],
    'tags': [],
    'publishedAt': []
    # 'dislikes': [],
    # 'favorites': [],
    # 'comments': []
}
# Dictionary to store dogs video data
so_high = {
    'id': [],
    'duration': [],
    'views': [],
    'likes': [],
    'title': [],
    'tags': [],
    'publishedAt': []
    # 'dislikes': [],
    # 'favorites': [],
    # 'comments': []
}
# For loop to obtain the information of each cats video
for item in same_beef_song['items']:
    # Getting the id
    print("items ", item)
    vidId = item['id']['videoId']
    # Getting stats of the video
    r = youtube.videos().list(
        part="statistics,contentDetails,snippet",
        id=vidId,
        fields="items(statistics,snippet," + \
               "contentDetails(duration))"
    ).execute()
    print("Same Beef ", r)
    # We will only consider videos which contains all properties we need.
    # If a property is missing, then it will not appear as dictionary key,
    # this is why we need a try/catch block
    try:
        duration = r['items'][0]['contentDetails']['duration']
        views = r['items'][0]['statistics']['viewCount']
        likes = r['items'][0]['statistics']['likeCount']
        title = r['items'][0]['snippet']['title']
        tags = len(r['items'][0]['snippet']['tags'])
        published_at = r['items'][0]['snippet']['publishedAt']
        # dislikes = r['items'][0]['statistics']['dislikeCount']
        # favorites = r['items'][0]['statistics']['favoriteCount']
        # comments = r['items'][0]['statistics']['commentCount']
        same_beef['id'].append(vidId)
        same_beef['duration'].append(duration)
        same_beef['views'].append(views)
        same_beef['likes'].append(likes)
        same_beef['title'].append(title)
        same_beef['tags'].append(tags)
        same_beef['publishedAt'].append(published_at)
        # same_beef['dislikes'].append(dislikes)
        # same_beef['favorites'].append(favorites)
        # same_beef['comments'].append(comments)
    except:
        print("views error")

# For loop to obtain the information of each dogs video
for item in so_high_song['items']:
    print("items1 ", item)

    vidId = item['id']['videoId']
    r = youtube.videos().list(
        part="statistics,contentDetails,snippet",
        id=vidId,
        fields="items(statistics,snippet," + \
               "contentDetails(duration))"
    ).execute()
    print("So High ", r)
    try:
        duration = r['items'][0]['contentDetails']['duration']
        views = r['items'][0]['statistics']['viewCount']
        likes = r['items'][0]['statistics']['likeCount']
        title = r['items'][0]['snippet']['title']
        tags = len(r['items'][0]['snippet']['tags'])
        published_at = r['items'][0]['snippet']['publishedAt']
        # dislikes = r['items'][0]['statistics']['dislikeCount']
        # favorites = r['items'][0]['statistics']['favoriteCount']
        # comments = r['items'][0]['statistics']['commentCount']
        so_high['id'].append(vidId)
        so_high['duration'].append(duration)
        so_high['views'].append(views)
        so_high['likes'].append(likes)
        so_high['title'].append(title)
        so_high['tags'].append(tags)
        so_high['publishedAt'].append(published_at)
        # so_high['dislikes'].append(dislikes)
        # so_high['favorites'].append(favorites)
        # so_high['comments'].append(comments)
    except:
        pass

df = pd.DataFrame(data=same_beef).to_csv("same_beef.csv", index=False)
df1 = pd.DataFrame(data=so_high).to_csv("so_high.csv", index=False)

# chart = sb.distplot(a=df[""], hist=True, kde=False, rug=False)
# chart.set(xlabel='Number of tags Used', ylabel='Occurrences')

df_highest_views = df.nlargest(1, 'views')
