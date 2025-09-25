from rest_framework import viewsets, permissions
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"detail": "Journal entry deleted successfully"},
            status=status.HTTP_200_OK
        )

class JournalEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JournalEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return JournalEntry.objects.filter(user=self.request.user)