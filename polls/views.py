from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# import ..
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
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # youtube_url = request.POST.get('youtube_url')
        youtube_url = 'https://www.youtube.com/watch?v=ad9St_ryyBo'
        print(youtube_url)
        video_id, subtitles = self.get_subtitles(youtube_url)

        ### Error Handling

        # Subtitle.objects.create(
        #     video_id=video_id,
        #     subtitles=subtitles
        # )
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, headers=headers, status=status.HTTP_201_CREATED,)
        return Response(subtitles)

    def get_video_id(self, youtube_url):
        return youtube_url.split("v=")[1]

    def get_subtitles(self, youtube_url):
        video_id = self.get_video_id(youtube_url)
        subtitle_list = YouTubeTranscriptApi.get_transcript(video_id)
        res = ''
        for s in subtitle_list:
            res += s['text'] + ' '
        return video_id, res
