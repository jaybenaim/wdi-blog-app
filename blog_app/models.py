from django.db import models 


class Topic(models.Model): 
    name_of_topic = models.CharField(max_length=255, null=False)
    
    def __str__(self): 
        return f'{self.name_of_topic}'

class Article(models.Model): 
    title = models.CharField(max_length=255, null=False)
    body = models.TextField() 
    draft = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=255, null=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self): 
        return f'{self.title}'

