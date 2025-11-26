from rest_framework import viewsets, permissions
from .models import JournalEntry
from .serializers import JournalEntrySerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .ml_integration.predictor import predict_sentiment
from rest_framework.views import APIView


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
    
@api_view(['POST'])
def analyze_sentiment(request):
    text = request.data.get('text', '')
    if not text:
        return Response(
            {"error": "No text provided"},
            status=status.HTTP_400_BAD_REQUEST
        )

    sentiment = predict_sentiment(text)
    return Response(
        {"sentiment": sentiment},
        status=status.HTTP_200_OK
    )

class PredictSentimentAPI(APIView):
    def post(self, request):
        text = request.data.get("text", "")

        prediction = predict_sentiment(text)

        if prediction == "MODEL_NOT_READY":
            return Response({
                "status": "error",
                "message": "ML model not trained yet. Please train the model first."
            }, status=200)

        return Response({"prediction": prediction})