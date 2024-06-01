from django.contrib import admin
from django.urls import path
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index,name='index',),
    # book/id
    path('book/<int:book_id>', views.detail, name='detail'),
]