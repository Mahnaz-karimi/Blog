from django.shortcuts import render
from django.http import HttpResponse

from .models import Post # . menes directory to the models. importe Post class

def home(request):
    context = {
        #'posts': posts # istedet for dommy data vi hente data fra database i det næste linje
        'posts': Post.objects.all()
    }
    return render(request, 'repport/home.html', context)


def about(request):
    return render(request, 'repport/about.html', {'title': 'About'})

'''
posts = [
    {
        'author': 'Sam',
        'title': 'rapport 1',
        'content': 'First post content',
        'date_posted': 'Sep 7, 2020'
    }
]
'''