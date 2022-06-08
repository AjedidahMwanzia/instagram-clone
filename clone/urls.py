from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns=[
  path('search/', views.search_results, name='search_results'),
  path('', views.home, name='home'),
  path('post/<image_id>',views.single_image,name='singleimage'),
  path('user/<user_id>', views.profile, name='profile'),
  path('user/add/image', views.add_image, name='addimage'),
  path('user/update/profile', views.update_profile, name='updateprofile'),
  path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
  path('follow/<to_follow>', views.follow, name='follow'),
  path('profile/<username>/', views.user_profile, name='user_profile'),
  path('post/<image_id>/like',views.like_image,name='likeimage'),
  

]