from django.shortcuts import render
from django.core.mail import send_mail

def correo_enviado(request):
    if request.method == 'POST':
        asunto = request.POST.get('asunto')
        contenido = request.POST.get('contenido')
        send_mail(asunto,
                contenido, 
                'postmaster@sandboxac77903abffd480c867a989ad214c4b1.mailgun.org',
                ['vigig85187@linacit.com'],
                fail_silently=False)

        return render(request, 'communications/correo_enviado.html')

    return render(request, 'communications/crear_correo.html')


def crear_correo(request):
    return render(request, 'communications/crear_correo.html')