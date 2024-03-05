from django.urls import path
from .views import *
from django.views.generic.base import RedirectView
urlpatterns = [
    path('profile_view/',profileView, name='profile_view'),
    path('profile_update/',profileUpdate,name='profile_update'),
    path('user_chat_list-/',user_chat_list, name='user_chat_list'),
    path('send-message/<int:recipient_id>/',send_message, name='send_message'),
    path('notification/',Notification,name='notification'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
#     path('inbox/', inbox, name='inbox'),
]


