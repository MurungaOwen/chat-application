from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Q
from .models import PrivateChat, Message

@login_required
def inbox(request):
    # Get all chats where user is either user1 or user2
    chats = PrivateChat.objects.filter(user1=request.user) | PrivateChat.objects.filter(user2=request.user)
    return render(request, 'chat/inbox.html', {'chats': chats})

@login_required
def chat_detail(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    # Get or create chat between current user and selected user
    chat = PrivateChat.objects.filter(
        (Q(user1=request.user, user2=other_user) |
         Q(user1=other_user, user2=request.user))
    ).first()
    
    if not chat:
        chat = PrivateChat.objects.create(user1=request.user, user2=other_user)
    
    messages = chat.private_messages.all()
    return render(request, 'chat/chat_detail.html', {
        'chat': chat,
        'messages': messages,
        'other_user': other_user
    })
