from rest_framework import serializers
from .models import JournalEntry

class JournalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEntry
        fields = [
            'id',
            'text',
            'mood',
            'mood_score',
            'tags',
            'category',
            'created_at',
            'updated_at'
        ]