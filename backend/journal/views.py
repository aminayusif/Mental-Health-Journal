from rest_framework import viewsets, permissions
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from rest_framework import generics


# Removed unused JournalEntryList and JournalEntryDetail classes

class JournalEntryViewSet(viewsets.ModelViewSet):
    #queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        # Only return entries for the logged-in user
        return JournalEntry.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign user when creating a journal entry
        serializer.save(user=self.request.user)

class JournalEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)