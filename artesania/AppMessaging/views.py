from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Message
from AppLogin.models import Avatar
from AppLogin.views import obtenerAvatar
from AppLogin.forms import AvatarForm
from django.db.models import Q

# Create your views here.

@login_required
def inbox(request):
    users_with_messages = User.objects.filter(
        Q(mensaje_enviado__destinatario=request.user) | Q(mensaje_recibido__remitente=request.user)
    ).distinct()

    no_messages_message = "Usted aún no tiene mensajes" if not users_with_messages else ""

    return render(request, 'AppMessaging/inbox.html', {'users_with_messages': users_with_messages, 'no_messages_message': no_messages_message, "avatar": obtenerAvatar(request)})




@login_required
def compose(request):
    if request.method == 'POST':
        destinatario_username = request.POST.get('destinatario')
        
        try:
            destinatario = User.objects.get(username=destinatario_username)
        except User.DoesNotExist:
            # El usuario destinatario no existe, puedes mostrar un mensaje de error
            error_message = "El usuario destinatario no existe."
            return render(request, 'AppMessaging/compose.html', {"avatar": obtenerAvatar(request), "error_message": error_message})
        
        contenido = request.POST.get('contenido')
        message = Message(remitente=request.user, destinatario=destinatario, contenido=contenido)
        message.save()
        return redirect('profile')
    
    return render(request, 'AppMessaging/compose.html', {"avatar": obtenerAvatar(request)})

@login_required
def chat(request, user_id):
    user_to = get_object_or_404(User, id=user_id)

   
    messages = Message.objects.filter(
        (Q(remitente=request.user, destinatario=user_to) | Q(remitente=user_to, destinatario=request.user))
    ).order_by('tiempo')

    return render(request, 'AppMessaging/chat.html', {'user_to': user_to, 'messages': messages, "avatar": obtenerAvatar(request)})

