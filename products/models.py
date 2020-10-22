from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.storage import FileSystemStorage
User = get_user_model()

class Product(models.Model):
    title = models.TextField(max_length=255)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='media', blank=True)

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Review(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    rate = models.CharField(max_length=5)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
