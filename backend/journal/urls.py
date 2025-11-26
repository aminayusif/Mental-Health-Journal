
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JournalEntryViewSet, PredictSentimentAPI

router = DefaultRouter()
router.register(r'entries', JournalEntryViewSet, basename='journalentry')

urlpatterns = [
    path('', include(router.urls)),
    path("predict/sentiment/", PredictSentimentAPI.as_view()),
]