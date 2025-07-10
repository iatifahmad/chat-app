from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chat/<str:last_name>/", views.chat_view, name="chat_view"),
    path("chat/", views.chat_list_view, name="chat_list"),
]