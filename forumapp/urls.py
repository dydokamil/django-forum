from django.urls import path

from forumapp import views

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    )
]