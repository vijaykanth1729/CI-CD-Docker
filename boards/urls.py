from django.urls import path
from .views import *
app_name = 'boards'
urlpatterns = [
    path('boards/', board_home, name='board-home'),
    path('boards/<int:pk>/', board_topic, name='board-topic'),
    path('boards/<int:pk>/new/', new_topic, name='new-topic'),
]
