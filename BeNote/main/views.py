from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import logout, login
from datetime import datetime

menu = [{'title': 'Мои заметки', 'url': 'notes', 'logo_url': 'notes.png'},
        {'title': 'Добавить заметку', 'url': 'newnote', 'logo_url': 'penсil.png'},
        {'title': 'Корзина', 'url': 'basket', 'logo_url': 'basket.png'},
        {'title': 'Задачи', 'url': 'tasks', 'logo_url': 'clock.png'},
        #{'title': 'Блокноты', 'url': 'notepads'},
]

def get_time():
    now = datetime.now().strftime("%H:%M:%S").split(':')
    s = int(now[0]) * 60 + int(now[1])
    if 360 < s < 720:
        return 'morning'
    elif 720 <= s < 1140:
        return 'day'
    else:
        return 'evening'



from .models import *

class BeNoteMain(ListView):
    model = Content
    template_name = 'main/base.html'
    context_object_name = 'content'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['time'] = get_time()
        context['title'] = 'Добавить записку'
        return context


# class New_note(CreateView):
#     # def get_user_id(self):
#     #     user_id = self.request.user.id
#     #     return user_id
#
#     form_class = Add_newnote_form
#     template_name = 'main/newnote.html'
#     success_url = reverse_lazy('main')
#     def  get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         context['title'] = 'Добавить записку'
#         return context

def New_note(request):
    user_id = str(request.user.id)
    if request.method == 'POST':
        form = Add_newnote_form(request.POST, request.FILES, initial={'user_id': user_id})
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = Add_newnote_form(initial={'user_id': user_id})
    return render(request, "main/newnote.html", context={'form': form, 'menu': menu, 'title': "Добавить заметку"})


def notes(request):
    content = Content.objects.filter(user_id=request.user.id)
    return render(request, 'main/notes.html', {'menu': menu, 'title': 'Мои заметки', 'content': content})

class Login_user(LoginView):
    form_class = Login_form
    template_name = "main/login.html"
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Войти'
        return context
    def get_success_url(self):
        return reverse_lazy('main')


class UserRegister(CreateView):
    form_class = Registration_form
    template_name = 'main/registration.html'
    #success_url = reverse_lazy('login')
    def  get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавить записку'
        return context
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


def Basket(request):
    content = Basket_model.objects.filter(user_id=request.user.id)
    return render(request, 'main/basket.html', {'menu': menu, 'title': 'Корзина', 'content': content})



def Check_note(request, post_id):
    note = get_object_or_404(Content, id=post_id)
    return render(request, 'main/check_note.html', {'note': note, 'menu': menu})

def delete_note(request, post_id):
    trash = Content.objects.get(id=post_id)
    Basket_model.objects.create(title=trash.title, text=trash.text, user_id=trash.user_id, time_create=trash.time_create, last_time_update=trash.last_time_update)
    trash.delete()
    return redirect('notes')

# def tasks(request):
#     return render(request, 'main/tacks.html', {'menu': menu, 'title': 'Мои заметки'})
#
# def notepads(request):
#     return render(request, 'main/tacks.html', {'menu': menu, 'title': 'Мои заметки'})

def Check_trash_note(request, post_id):
    note = get_object_or_404(Basket_model, id=post_id)
    return render(request, 'main/check_trash_note.html', {'note': note, 'menu': menu})

class Logout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('main')

def delete_trash_note(request, post_id):
    Basket_model.objects.get(id=post_id).delete()
    return redirect('basket')


def clear_basket(request):
    content = Basket_model.objects.filter(user_id=request.user.id)
    for c in content:
        c.delete()
    return redirect('basket')


def tasks(request):
    tasks = Tasks_model.objects.filter(user_id=request.user.id)
    user_id = str(request.user.id)
    if request.method == 'POST':
        form = Task_form(request.POST, request.FILES, initial={'user_id': user_id})
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = Task_form(initial={'user_id': user_id})
    return render(request, 'main/tasks.html', {'menu': menu, 'tasks': tasks, 'form': form, 'title': 'Задачи'})



def complete_task(requests, task_id):
    Tasks_model.objects.get(id=task_id).delete()
    return redirect('tasks')

def start_page(request):
    return render(request, 'main/start_page.html')