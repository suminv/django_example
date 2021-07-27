from app_users.models import Profile
from app_users.forms import AuthForm, RegisterForm 
from django.shortcuts import render, redirect
from django.http import  HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView


class AnotherLoginView(LoginView):
    """
    Используем встроенный функционал для LOGIN.
    """
    template_name = 'app_users/login.html'


class AnotherLogoutView(LogoutView):
    """
    используем встроенный функционал для LOGOUT. И перенаправляем на главную страницу.   
    """
    # template_name = 'app_users/logout.html'
    next_page = '/'



def register_view(request):
    """
    Регистрация пользователя. 
    Проверяем валидность формы, сохраняем пользователя и устанавливаем ему пароль.
    
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')

    else:
        form = UserCreationForm()
        
        return render(request, 'app_users/register.html', {'form': form})

def another_register_view(request):
    """
    Регистрация пользователя. 
    Проверяем валидность формы, сохраняем пользователя и устанавливаем ему пароль.
    
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')

    else:
        form = RegisterForm()
    return render(request, 'app_users/register.html', {'form': form})





def login_view(request):
    """
    Для POST запроса пытаемся аутентифицировать пользователя.
    Для остальных запросов отображем страничку логина
    """
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user.is_active:
                login(request, user)
                return HttpResponse('Вы успешно вошли в систему.')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написания логина и пароля!')

    else:  
        auth_form = AuthForm() 
        context = {
            'form': auth_form,
        }

    return render(request, 'app_users/login.html', context=context)


def logout_view(request):
    logout(request)
    return HttpResponse('Вы вышли из под своей учетной записи.')