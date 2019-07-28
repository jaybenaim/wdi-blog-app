from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from datetime import datetime 
from blog_app.models import Article

def home(request): 
    date = datetime.now().date()
    article = Article.objects.get(pk=1)
    
    context = {
        'date': date, 
    'articles': article 

    } 
    response = render(request, 'index.html',  context)
    return HttpResponse(response) 


