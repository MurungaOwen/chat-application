from django.urls import path
from . import views

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('chat/<int:user_id>/', views.chat_detail, name='chat_detail'),
]
