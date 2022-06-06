from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Image(models.Model):
    author=models.ForeignKey('auth.User',on_delete = models.CASCADE)
    image=models.ImageField(default='DEFAULT VALUE',blank=True,null=True)
    caption = models.TextField()
    created_on=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()
    
    @classmethod
    def search_image(cls, search_term):
        post = cls.objects.filter(name__icontains=search_term).all()
        return post

    class Meta:
        ordering = ['-created_on',]
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to = 'pictures/')
    bio=models.TextField()
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    user_name=models.CharField(max_length=20,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.bio
    def save_profile(self):
        self.save()

    # update profile
    def update_profile(self, name):
        self.name = name
        self.save()

     # delete profile from database
    def delete_profile(self):
        self.delete()
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    @classmethod
    def search_profiles(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term).all()
        return profiles
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    content=models.TextField(null=True)
    
    def __str__(self):
        return self.image
    def save_comments(self):
        self.save()

    # update comments
    def update_comments(self, name):
        self.name = name
        self.save()

     # delete comments from database
    def delete_comments(self):
        self.delete()
class Likes(models.Model):
    image = models.ForeignKey(Image,related_name='like_count', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.image
    def save_likes(self):
        self.save()

    # update like
    def update_likes(self, name):
        self.name = name
        self.save()

     # delete like from database
    def delete_likes(self):
        self.delete()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'image'], name="unique_like"),
        ]
class AddImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image','caption','author']
class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_photo']
class CommentForm(ModelForm):
    class Meta:
        model=Comments
        fields=['content']
        widgets= {
            'content':forms.Textarea(attrs={'rows':2,})
        }



