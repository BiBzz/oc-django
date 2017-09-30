from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=42)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Date de parution')

    def __str__(self):
        """Méthode facilitant la reconnaissance et le traitement de cet objet"""
        return self.title 
