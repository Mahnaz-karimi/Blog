from django.shortcuts import render
from django.http import HttpResponse
posts = [
    {
        'author': 'Sam',
        'title': 'rapport 1',
        'content': 'First post content',
        'date_posted': 'Sep 7, 2020'
    },
    {
        'author': 'M k',
        'title': 'Reppot Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'repport/home.html', context)


def about(request):
    return render(request, 'repport/about.html', {'title': 'About'})