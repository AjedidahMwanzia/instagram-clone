from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

urlpatterns=[
  path('search/', views.search_results, name='search_results'),
  path('', views.home, name='home'),
  path('new/', views.post_create,name="post_create"),
  
  path('post/<image_id>',views.post_detail,name='post_detail'),
  path('post/<image_id>/like',views.like_image,name='likeimage'),
  path('user_profile/<username>/', views.user_profile, name='user_profile'),
  path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
  path('follow/<to_follow>', views.follow, name='follow'),
  path('register/',views.register,name = 'register'),
  path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name = 'login'),
  path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name = 'logout'),
  path('profile/',views.profile,name = 'profile'),
  path('update/',views.update,name = 'update'),
]