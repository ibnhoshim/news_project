from django.utils import timezone
from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = News.Status.Published)

class Categories(models.Model):
    name = models.CharField(max_length=15)
    
    def __str__(self):
        return self.name

class News(models.Model):
    
    class Status(models.TextChoices):
        Draft = "DF", "Draft"
        Published = "PB", "Published"
        
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to="news/images", blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete = models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)
    
    objects  = models.Manager() #default Manager
    published = PublishedManager()
    
    class Meta:
        ordering = ["-publish_time"]
        
    def __str__(self):
        return self.title
    
