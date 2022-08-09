from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns=[
    path('tinymce/', include('tinymce.urls')),
    path('', views.index,name='index'),
    path('blog/', views.blog,name='blog'),
    path('post/<id>/', views.post,name='post'),
    path('search/',views.search,name='search')
]