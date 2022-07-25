from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    author_id = models.IntegerField()
    publication_date = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title



