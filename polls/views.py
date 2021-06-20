from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from youtube.youtube_transcript_api import YouTubeTranscriptApi
from rest_framework.response import Response

# rest api
from rest_framework import viewsets
from .serializers import SubtitleSerializer
from .models import Subtitle

import requests

class SubtitleViewSet(viewsets.ModelViewSet):
    queryset = Subtitle.objects.all() #.order_by('name') # should be ordered by date
    serializer_class = SubtitleSerializer

    # class Meta:
    #     model = Subtitle
    #     fields = '__all__'

    """
    Create a model instance.
    """
    def create(self, request, *args, **kwargs):
         # youtube_url = 'https://www.youtube.com/watch?v=ad9St_ryyBo'
        youtube_url = request.POST.get('youtube_url')

        try:
            video_id = self.get_video_id(youtube_url)
            if video_id:
                subtitles = self.get_subtitles(video_id)
            else:
                # if we want to return a string ---
                # return Response('video id not found')
                response = HttpResponse('video id not found', content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'attachment; filename="video_id_not_found.txt"'
                return response # return a file
        except Exception:
            return Response('Could not retrieve a transcript for the video. This is most likely caused by - Subtitles are disabled for this video')

        Subtitle.objects.create(
            video_id=video_id,
            youtube_url=youtube_url,
            subtitles=subtitles
        )

        # generate the file
        response = HttpResponse(subtitles, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="subtitles.txt"'

        return response
        # return Response(subtitles)


    def get_video_id(self, youtube_url):
        if not youtube_url:
            return None
        return youtube_url.split("v=")[1]

    def get_subtitles(self, video_id):
        subtitle_list = YouTubeTranscriptApi.get_transcript(video_id)
        res = ''
        for s in subtitle_list:
            res += s['text'] + ' '
        return res
