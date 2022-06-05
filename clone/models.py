from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete = models.CASCADE)
    image=models.ImageField(default='DEFAULT VALUE',blank=True,null=True)
    caption = models.TextField()
    created_on=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

    def save_image(self):
        self.save()

    class Meta:
        ordering = ['-created_on',]