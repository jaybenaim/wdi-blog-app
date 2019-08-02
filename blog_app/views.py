from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render
from datetime import datetime 
from blog_app.models import * 

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
    form = CommentForm() 
    context = { 
        'article': article, 
        'comments': Comment.objects.all(),
        'form': form
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

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


# def new(request): 
#     form = CommentForm() 
#     context =  { 
#         'form': form,
#         'message': "Create a comment", 
#         'action': '/comments/create' 
#     }

#     return render(request, 'form.html', context)