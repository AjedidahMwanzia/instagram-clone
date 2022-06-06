from django.contrib import admin
from .models import Image,Profile,Likes,Subscribers, Comment, Follow
# Register your models here.
admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Likes)
admin.site.register(Comments)
admin.site.register(Subscribers)
admin.site.register(Follow)