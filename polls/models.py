from django.db import models

from youtube.youtube_transcript_api import YouTubeTranscriptApi

# Create your models here.
class Subtitle(models.Model):
    # video_id = models.CharField(max_length=100)
    youtube_url = models.CharField(max_length=1000, default='')
    subtitles = models.CharField(max_length=100000) # enough ?

    def __str__(self):
        return self.video_id

    def parse_video_id(self, youtube_url):
        url = 'https://www.youtube.com/watch?v=ad9St_ryyBo'
        video_id = youtube_url.split("v=")[1]
        # self.update(video_id=video_id)
        return video_id

    def get_subtitles(self, video_id):
        subtitle_list = YouTubeTranscriptApi.get_transcript(video_id)
        subtitles = ''
        for s in subtitle_list:
            subtitles += s['text'] + ' '
        return subtitles