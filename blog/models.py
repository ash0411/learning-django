from django.db import models
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=120)
    content = models.TextField()
    active= models.BooleanField(default=True)
    light_novel = 'ln'
    novel = 'nv'
    research_paper = 'rp'
    TYPE_OF_NOVEL_CHOICES = [
        (light_novel,'light_novel'),
        (novel,'novel'),
        (research_paper,'research_paper'),
    ]
    type_of_novel = models.CharField(
        max_length = 2,
        choices = TYPE_OF_NOVEL_CHOICES,
        default =novel,
    )
    publish_date = models.DateField(auto_now=False,auto_now_add=False)
    email = models.EmailField(max_length=50)
    def get_absolute_url(self):
        return reverse("article-detail",kwargs={"id": self.id})
