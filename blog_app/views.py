from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from datetime import datetime 
from blog_app.models import * 
from django import forms 

def home(request): 
    all_articles = Article.objects.all() # .order_by("-published_date") 
    
    return render(request, 'index.html',  {
        'articles': all_articles, 
        'topics': Topic.objects.all(), 
    })


def root(request): 
    return HttpResponseRedirect('home')


def post_show(request, id): 
    article = Article.objects.get(pk=id)
    form = CommentForm() 
     
    context = { 
        'article': article, 
        'comments': Comment.objects.filter(article=article),
        'form': form, 
        'topics': Topic.objects.all() 
    } 
    return render(request, 'post.html', context) 


def create_comment(request): 
    params = request.POST 
    article_id = params["article"]
    article = Article.objects.get(pk=article_id)

    comment = Comment() 
    comment.name = params['name']
    comment.message = params['message']
    comment.article = article
    comment.save() 

    return HttpResponseRedirect('/')


def new_article(request): 
    form = ArticleForm() 
    topic = TopicForm()
    context =  { 
        'form': form,
        'message': "Create a comment", 
        'action': 'article/create', 
        'topic': topic, 
    }

    return render(request, 'new_article.html', context)

def create_article(request): 
    form = ArticleForm(request.POST)
    topic = TopicForm(request.POST)
    context = { 
        'form': form,
        'topic': topic
    }
    
    if form.is_valid(): 
        form.save() 
        topic = TopicForm(request.POST) 
        topic.save() 
    
        return HttpResponseRedirect('/', context)
    else: 
        form = ArticleForm(request.POST)
        topic = TopicForm(request.POST)
    context = { 
        'form': form,
        'topic': topic
    }
    
    return render(request, 'new_article.html', context) 

    


