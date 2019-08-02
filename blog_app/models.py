from django.db import models 
from django.forms import ModelForm 
from django.core import  validators
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date 
from django import forms 



def validate_body(value): 
    if len(value) < 2: 
        raise ValidationError(
            ('You need to enter a body.'), params={'value': value})


class Topic(models.Model): 
    name_of_topic = models.CharField(max_length=255, null=True)
    article = models.ManyToManyField('Article', related_name="article_topics")
    
    def __str__(self): 
        return f'{self.name_of_topic}'

 
class Article(models.Model): 
    title = models.CharField(max_length=255, null=False)
    body = models.TextField() 
    draft = models.BooleanField(default=True)
    published_date = models.DateField() 
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

class DateInput(forms.DateInput):
    input_type = 'date'

class ArticleForm(ModelForm): 
    class Meta: 
        model = Article 
        fields = ['title', 'body', 'draft', 'author', 'published_date']
        widgets = { 
            'published_date': DateInput(), 
        }

    def clean(self): 
        cleaned_data = super().clean() 
        body = cleaned_data.get('body')

        if len(body) < 2: 
            self.add_error('body', 'Body must be more than 2 characters long.')

        draft = cleaned_data.get('draft')
        published_date = cleaned_data.get('published_date')
        today = date.today() 
        if draft: 
            if published_date < today: 
                self.add_error('published_date', 'The date must be in the future for a draft')

            elif published_date > today:
                self.add_error('published_date', 'The published date cannot be in the future')
            else: 
                self.add_error('published_date', 'Something went wrong')
            

            


class TopicForm(ModelForm): 
    class Meta: 
        model = Topic 
        fields = ['name_of_topic']
