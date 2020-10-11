from bookmarks.models import Bookmark
from bookmarks.serializers import BookmarkSerializer
from rest_framework import viewsets


class BookmarkList(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
