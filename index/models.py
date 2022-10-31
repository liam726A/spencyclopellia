from email.policy import default
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    name_ja = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#303967")
    explanation = models.TextField(default="None")
    
    def __str__(self):
        return self.name

class Topic(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=100)
    name_ja = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#303967")
    explanation = models.TextField(default="None")
    
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    color = models.CharField(max_length=7, default="#303967")
    page_hp = models.CharField(max_length=200)
    page_doc = models.CharField(max_length=200)
    page_github = models.CharField(max_length=200)
    explanation = models.TextField(default="None")
    
    def __str__(self):
        return self.name

class Library(models.Model):
    language = models.ManyToManyField(Language)
    name = models.CharField(max_length=100)
    text = models.TextField()
    color = models.CharField(max_length=7, default="#303967")
    page_hp = models.CharField(max_length=200)
    page_doc = models.CharField(max_length=200)
    page_github = models.CharField(max_length=200)
    explanation = models.TextField(default="None")
    
    def __str__(self):
        return self.name

class Spell(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#303967")
    category = models.ManyToManyField(Category)
    language = models.ManyToManyField(Language)
    language_name = models.CharField(max_length=100, default="language_name")
    library_name = models.CharField(max_length=100, default="library_name")
    library_hp = models.CharField(max_length=100, default="library_hp")
    library_github = models.CharField(max_length=100, default="library_github")
    forwhat = models.TextField(default="None")
    forwhat_ja = models.TextField(default="None")
    example_in = models.TextField(default="None")
    example_out = models.TextField(default="None")
    reference = models.TextField(default="None")
    explanation = models.TextField(default="None")
    
    def __str__(self):
        return self.name