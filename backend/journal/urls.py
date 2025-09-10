from django.urls import path
from .views import JournalEntryList, JournalEntryDetail

urlpatterns = [
    path('entries/', JournalEntryList.as_view(), name='journal-entry-list'),
    path('entries/<int:pk>/', JournalEntryDetail.as_view(), name='journal-entry-detail'),
]