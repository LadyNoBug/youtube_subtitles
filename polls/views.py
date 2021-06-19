from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# import ..
from youtube.youtube_transcript_api import YouTubeTranscriptApi


def index(request):
    # str = 'haha'
    url = 'https://www.youtube.com/watch?v=ad9St_ryyBo'
    video_id = url.split("v=")[1]
    subtitle_list = YouTubeTranscriptApi.get_transcript(video_id)
    
    
    res = ''
    for s in subtitle_list:
        res += s['text'] + ' '
    return HttpResponse(res)