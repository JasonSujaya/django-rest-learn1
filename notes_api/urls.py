from django.urls import path, include
from rest_framework.routers import DefaultRouter

from notes_api import views


router = DefaultRouter()
router.register('notes', views.NoteViews, base_name='notes')


urlpatterns = [
    path('', include(router.urls))
]
