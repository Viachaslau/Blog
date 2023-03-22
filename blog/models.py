from django.db import models
from django.urls import reverse
from datetime import datetime
from django.core.validators import MinLengthValidator
from django.template.defaultfilters import slugify

# Create your models here.

class Author(models.Model):
    first_name =  models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts')
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True)
    data = models.DateField(default=datetime.now)
    slug = models.SlugField(
        default="", blank=True, null=False, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.id}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    

    def get_absolute_url(self):
        return reverse("post-detail-page", args={self.slug})

class Comment(models.Model):
    user_name =  models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", default=True)

