
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import User
from .models import Message

def index(request):
    return render(request, "chat/index.html")

@login_required
def chat_list_view(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, "chat/chat_list.html", {"users": users})

@login_required
def chat_view(request, last_name):
    other_user = get_object_or_404(User, last_name=last_name)
    return render(request, "chat/chat_room.html", {"other_user": other_user})