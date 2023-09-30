

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .serializers import EventoSerializer
from .models import Evento
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, SessionAuthentication]

    # Método para criar um evento
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Método para atualizar um evento
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # Método para excluir um evento
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
class LoginView(View):
    template_name = './login.component.html'

    def post(self, request, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']

        user = authenticate(request, username=username, password=password)
               
        if user is not None:
            login(request, user)
            return redirect('pagina_inicial')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

        return render(request, self.template_name)