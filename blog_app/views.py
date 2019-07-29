from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from datetime import datetime 
from blog_app.models import Article, Topic

def home(request): 
    date = datetime.now().date()
    all_articles = Article.objects.order_by("-published_date") 
    
   
    context = {
        'date': date, 
        'articles': all_articles, 
        'topics': Topic.objects.all(), 
    } 
    response = render(request, 'index.html',  context)
    return HttpResponse(response) 


def root(request): 
    return HttpResponseRedirect('home')



def post_show(request, id): 
    article = Article.objects.get(pk=id)
    context = { 
        'article': article 
    } 
    return render(request, 'post.html', context) 
