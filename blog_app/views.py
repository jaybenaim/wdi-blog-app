from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime 
from blog_app.models import * 
from django import forms 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate


def root(request): 
    return redirect('home/')
    
def home(request): 
    all_articles = Article.objects.all() # .order_by("-published_date") 
    return render(request, 'index.html',  {
        'articles': all_articles, 
        'topics': Topic.objects.all(), 
    })

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

def signup(request):
    form = UserCreationForm() 
    context =  {'form': form} 
    return render(request, 'registration/signup.html', context)

def signup_create(request): 
    form = UserCreationForm(request.POST)
    if form.is_valid(): 
        new_user = form.save()
        login(request, new_user)
        return redirect('/')
    else: 
        return render(request, 'registration/signup.html', {'form': form})

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

@login_required 
def create_comment(request): 
    params = request.POST 
    article_id = params["article"]
    article = Article.objects.get(pk=article_id)

    comment = Comment() 
    comment.name = params['name']
    comment.message = params['message']
    comment.article = article
    comment.save() 

    return redirect('/')

@login_required 
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

@login_required 
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

    


