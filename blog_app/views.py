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
        'comments': Comment.objects.filter(article_id=id),
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

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def new_article(request): 
    form = ArticleForm() 
    topic = TopicForm()
    context =  { 
        'form': form,
        'message': "Create a comment", 
        'action': 'article/create', 
        'topic': topic 
    }

    return render(request, 'new_article.html', context)

def create_article(request): 
    form = ArticleForm(request.POST) 
    form.save() 
    topic = TopicForm(request.POST) 
    topic.save() 

    return HttpResponseRedirect('/')

# def new_topic(request):
#     form = TopicForm() 
    
#     context = { 
#         'topic_form': form 
#     }
#     return render(request, 'new_article', context)


# def create_topic(request): 
#     form = TopicForm(request.POST)
#     article_id = request.POST["article"]
#     article = Article.objects.get(pk=article_id)
#     form.article = article
#     form.save() 

#     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


