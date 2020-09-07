from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import login as auth_login
from django.core.mail import send_mail
from django.conf import settings

def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = form.save()
            auth_login(request, user)
            send_mail(
                'DjangoApp',
                'Thanks for registering to our site, you can have a fun from now',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )

            return redirect('boards:board-home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})
