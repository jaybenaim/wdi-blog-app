from django.db import models 
from django.forms import ModelForm 


class Topic(models.Model): 
    name_of_topic = models.CharField(max_length=255, null=True)
    article = models.ManyToManyField('Article', related_name="article_topics")
    
    def __str__(self): 
        return f'{self.name_of_topic}'

 
class Article(models.Model): 
    title = models.CharField(max_length=255, null=False)
    body = models.TextField() 
    draft = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255, null=False)
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)

    def __str__(self): 
        return f'{self.title}'


class Comment(models.Model): 
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    message = models.CharField(max_length=255)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')

    def __str__(self): 
        return f'{self.message}'


class CommentForm(ModelForm): 
    class Meta: 
        model = Comment
        fields = ['name', 'message']

class ArticleForm(ModelForm): 
    class Meta: 
        model = Article 
        fields = ['title', 'body', 'draft', 'author']

class TopicForm(ModelForm): 
    class Meta: 
        model = Topic 
        fields = ['name_of_topic']
