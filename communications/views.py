from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    send_mail('Hola de parte de Joaquin',
              'Hola este es un mensaje enviado con ayuda de DJango', 
              'joaquin_aqb@hotmail.com',
              ['vigig85187@linacit.com'],
              fail_silently=False)

    return render(request, 'communications/index.html')