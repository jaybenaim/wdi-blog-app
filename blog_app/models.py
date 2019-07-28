from django.db import models 

class Article(models.Model): 
    title = models.CharField(max_length=255, null=False)
    body = models.TextField() 
    draft = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255, null=False)
