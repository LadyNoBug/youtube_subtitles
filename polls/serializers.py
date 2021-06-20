from rest_framework import serializers

from .models import Subtitle

class SubtitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subtitle
        fields = ('id', 'youtube_url') # video_id , 'subtitles'