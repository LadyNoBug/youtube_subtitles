from django.urls import path

from . import views
from .models import Subtitle

# rest
from django.urls import include, path
from rest_framework import routers

# rest
router = routers.DefaultRouter()
router.register(r'subtitles', views.SubtitleViewSet)

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]