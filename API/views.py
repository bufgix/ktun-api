from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Announcement, register_all_announcements
from .serializers import AnnouncementSerializer

class AnnouncementView(APIView):
    def get(self, response):
        register_all_announcements()
        announcements = Announcement.objects.all()
        serializer = AnnouncementSerializer(announcements, many=True)

        return Response(serializer.data)

