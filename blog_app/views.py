from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime 
from blog_app.models import * 
from django import forms 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate
from django.urls import reverse 



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

    return redirect(reverse('post_details', args=[article.id]))

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


@login_required 
def edit_article(request, id): 
    article = get_object_or_404(Article, id=id)
    if request.method == 'GET': 
        form = ArticleForm(instance=article)
        context = {'form': form, 'article': article}
        return render(request, 'edit_article.html', context) 

    elif request.method == 'POST': 
        form = ArticleForm(request.POST, instance=article) 
        if form.is_valid():
            update_article = form.save() 
            return redirect(reverse('post_details', args=[article.id]))
        else: 
            context = {'form': form, 'article': article}
            return render(request, 'edit_article.html', context)

@login_required 
def delete_article(request, id): 
    article = get_object_or_404(Article, id=id)
    article.delete() 
    return redirect('/')

@login_required 
def edit_comment(request, id): 
    comment = get_object_or_404(Comment, id=id)
    if request.method == 'GET': 
        form = CommentForm(instance=comment) 
        context = { 
            'form': form,
            'comment': comment, 
        }
        return redirect(reverse('edit_comment', args=[comment.id]))
    else: 
        context = { 'form': form, 'comment': comment}
        return render(request, 'edit_comment', context)

@login_required
def delete_comment(request, id): 
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect(reverse('post_details', args=[comment.article.id]))

