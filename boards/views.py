from django.shortcuts import render, get_object_or_404, redirect
from .models import Board, Topic, Post
from django.http import Http404
from django.contrib.auth.models  import User
from django.core.mail import send_mail
from django.conf import settings
def board_home(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards':boards})

def board_topic(request,pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'boards/topic.html', {'board':board})

def new_topic(request, pk):
    board = get_object_or_404(Board,pk=pk)
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=request.user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=request.user
        )
        send_mail(
                  'New Topic Arrived',
                  'Thanks for creating new topic',
                  settings.EMAIL_HOST_USER,
                  #['tebosek526@kespear.com'],
                  [topic.starter.email],  # takes current user email
                  fail_silently=False
                  )

        return redirect('boards:board-topic', pk=board.pk)  # TODO: redirect to the created topic page
    return render(request, 'boards/new_topic.html', {'board':board})
