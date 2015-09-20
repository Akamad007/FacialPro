#!/usr/bin/python

from apiclient.discovery import build
from optparse import OptionParser

# Set DEVELOPER_KEY to the "API key" value from the "Access" tab of the
# Google APIs Console http://code.google.com/apis/console#access
# Please ensure that you have enabled the YouTube Data API for your project.
from FacialPro.settings import YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,DEVELOPER_KEY

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)
  
    search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.maxResults
  ).execute()

    videos = []
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            
            videos.append(search_result["id"]["videoId"])
    return videos
   

def youTubeSearch(query,count):
    parser = OptionParser()
    parser.add_option("--q", dest="q", help="Search term",
        default=query)
    parser.add_option("--max-results", dest="maxResults",
        help="Max results", default=count)
    (options, args) = parser.parse_args()
    
    return youtube_search(options)