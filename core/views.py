from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from .models import Guia, Experiencia


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['guias'] = Guia.objects.filter(ativo=True)

        # Verificar se o usuário está logado economiza consultas ao banco de dados, pois assim as experiências serão exibidas somente se essa condição for verdadeira
        if self.request.user.is_authenticated:
            experiencias = Experiencia.objects.filter(ativo=True)
            context['experiencias'] = experiencias
            context['experiencias_json'] = [
                {
                    'nome': experiencia.nome,
                    'descricao': experiencia.descricao,
                    'foto': experiencia.foto.url if experiencia.foto else '',
                    'tag': 'Experiência'
                }
                for experiencia in experiencias
            ]
        else:
            context['experiencias'] = []
            context['experiencias_json'] = []

        return context


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    erro = None

    if request.method == 'POST':
        email = request.POST.get('email', '').strip().lower()
        senha = request.POST.get('senha', '')

        usuario = authenticate(
            request,
            username=email,
            password=senha
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('home')
        else:
            erro = 'E-mail ou senha incorretos.'

    return render(request, 'register/login.html', {
        'erro': erro
    })


def cadastro_view(request):
  if request.user.is_authenticated:
    return redirect('home')

  if request.method == 'POST':
    nome = request.POST.get('nome', '').strip()
    email = request.POST.get('email', '').strip().lower()
    telefone = request.POST.get('telefone', '').strip()
    senha = request.POST.get('senha', '')

    erro = None

    if not nome or not email or not senha or not telefone:
      erro = 'Preencha todos os campos.'
    elif User.objects.filter(email=email).exists():
      erro = (
          'Este e-mail já está cadastrado. Tente fazer login ou use outro e-mail.'
      )
    else:
      # Cria o usuário
      usuario = User.objects.create_user(
          username=email, email=email, first_name=nome, password=senha
      )

      # Faz o login automático do usuário recém-cadastrado
      login(request, usuario)

      # Redireciona uma única vez para a home
      return redirect('home')

    # Se houver erro de validação, renderiza a página de volta com os dados preenchidos
    return render(
        request,
        'register/cadastro.html',
        {'erro': erro, 'nome': nome, 'email': email, 'telefone': telefone},
    )

  return render(request, 'register/cadastro.html')

  return render(request, 'register/cadastro.html')
def logout_view(request):
    logout(request)
    return redirect('home')