from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render, redirect
from .forms import BookRecommendationForm

def submit_recommendation(request):
    if request.method == 'POST':
        form = BookRecommendationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recommendation_list')
    else:
        form = BookRecommendationForm()
    return render(request, 'submit_recommendation.html', {'form': form})


from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
