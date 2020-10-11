from django.urls import path, include
from bookmarks import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'bookmark', views.BookmarkList)

urlpatterns = [
    path('', include(router.urls))
]
