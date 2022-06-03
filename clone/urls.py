from django.urls import path,include
from .views import (
    PostListView
)
app_name = 'clone'
urlpatterns=[
    
    path('', PostListView.as_view(),name="post_list"),

]