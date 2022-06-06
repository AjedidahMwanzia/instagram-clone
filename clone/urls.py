from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path

urlpatterns=[
  path('search/', views.search_results, name='search_results'),
  path('', views.home, name='home'),
  path('user/<user_id>', views.profile, name='profile'),
  path('user/add/image', views.add_image, name='addimage'),
  path('user/update/profile', views.update_profile, name='updateprofile'),
  path('post/<image_id>',views.post_detail,name='post_detail'),
  path('post/<image_id>/like',views.like_image,name='likeimage')
  
]