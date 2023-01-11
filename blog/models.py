from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    imagefields = models.FileField(upload_to= 'images/')
    describe = RichTextField()
    date = models.DateField()