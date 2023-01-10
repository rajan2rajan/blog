from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    imagefields = models.FileField(upload_to= 'images/')
    describe = HTMLField()
    date = models.DateField()