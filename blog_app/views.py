from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from datetime import datetime 
from blog_app.models import Article

def home(request): 
    date = datetime.now().date()
    heading = Article.objects.get(pk=1).title
    body = Article.objects.get(pk=1).body
    
    all_articles = Article.objects.all() 
    
    context = {
        'date': date, 
    'heading': heading, 
    'articles': all_articles, 
    'body': body
    } 
    response = render(request, 'index.html',  context)
    return HttpResponse(response) 


