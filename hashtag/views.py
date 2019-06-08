from .models import Hashtag
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Create your views here.
def hashtag_list(request):
    hashtags = Hashtag.objects.all()
    return render(request, 'hashtag/hashtag_list.html', {'hashtags': hashtags})

def hashtag_art(request):
    hashtags = Hashtag.objects.all()
    return render(request, 'hashtag/art.html', {'hashtags': hashtags})

def hashtag_mood(request):
    hashtags = Hashtag.objects.all()
    return render(request, 'hashtag/mood.html', {'hashtags': hashtags})

def hashtag_tech(request):
    hashtags = Hashtag.objects.all()
    return render(request, 'hashtag/tech.html', {'hashtags': hashtags})

def hashtag_food(request):
    hashtags = Hashtag.objects.all()
    return render(request, 'hashtag/food.html', {'hashtags': hashtags})

def hashtag_fashion(request):
    hashtags = Hashtag.objects.all()
    return render(request, 'hashtag/fashion.html', {'hashtags': hashtags})

def hashtag_wildlife(request):
    hashtags = Hashtag.objects.all()
    return render(request, 'hashtag/wildlife.html', {'hashtags': hashtags})
