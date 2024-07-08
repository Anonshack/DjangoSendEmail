from django.core.mail import send_mail
from django.shortcuts import render
from .forms import EmailForm


def home(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']
            send_mail(subject, message, 'anonshack48@gmail.com', [recipient])
            return render(request, 'success.html')
    else:
        form = EmailForm()
    return render(request, 'home.html', {'form': form})
