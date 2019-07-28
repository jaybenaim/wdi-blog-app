from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from datetime import datetime 
from blog_app.models import Article

def home(request): 
    date = datetime.now().date()
    heading = Article.objects.order_by("published_date")[0].title
    body = Article.objects.order_by("published_date")[0].body
    draft = Article.objects.order_by("published_date")[0].draft
    author = Article.objects.order_by("published_date")[0].author
    all_articles = Article.objects.all() 
    
   
    context = {
        'date': date, 
    'heading': heading, 
    'articles': all_articles, 
    'body': body,
    'draft': draft, 
    'author': author, 
    } 
    response = render(request, 'index.html',  context)
    return HttpResponse(response) 


def root(request): 
    return HttpResponseRedirect('home')
