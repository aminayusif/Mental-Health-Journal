"""Models for JournalEntry and Reminder for a mental health journal app."""

from django.db import models
from django.contrib.auth import get_user_model

class JournalEntry(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='journal_entries')
    text = models.TextField()
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('anxious', 'Anxious'),
        ('angry', 'Angry'),
        ('neutral', 'Neutral'),
    ]
    mood = models.CharField(max_length=50, choices=MOOD_CHOICES)
    from django.core.validators import MinValueValidator, MaxValueValidator

    mood_score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    tags = models.JSONField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.created_at.date()}"