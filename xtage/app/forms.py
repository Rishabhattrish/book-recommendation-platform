# forms.py
from django import forms
from .models import BookRecommendation

class BookRecommendationForm(forms.ModelForm):
    class Meta:
        model = BookRecommendation
        fields = ['title', 'author', 'description', 'cover_image', 'rating']
