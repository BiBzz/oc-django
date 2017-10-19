from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.CharField(max_length=42)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Date de parution')
    category = models.ForeignKey('Category')

    def __str__(self):
        """Méthode facilitant la reconnaissance et le traitement de cet objet"""
        return self.title 

class Category(models.Model):
    label = models.CharField(max_length=30)

    def __str__(self):
        return self.label
