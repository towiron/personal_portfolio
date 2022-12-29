from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()
    img = models.ImageField(blank=True, upload_to='blog/images/')
    def __str__(self):
        return self.title