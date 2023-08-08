from django.urls import path

from .views import *

urlpatterns = [
    path('', start_page, name='start_page'),
    path('main', BeNoteMain.as_view(), name='main'),
    path('main/newnote', New_note, name='newnote'),
    path('main/notes', notes, name='notes'),
    path('login',Login_user.as_view(), name='login'),
    path('registration', UserRegister.as_view(), name='registration'),
    path('logout', Logout.as_view(), name='logout'),
    path('main/check_note/<int:post_id>', Check_note, name='check_note'),
    path('main/basket', Basket, name='basket'),
    path('delete_note/<int:post_id>', delete_note, name='delete_note'),
    path('main/basket/check_trash_note/<int:post_id>', Check_trash_note, name ='check_trash_note'),
    path('basket/delete_trash_note/<int:post_id>', delete_trash_note, name='delete_trash_note'),
    path('basket/clear_basket', clear_basket, name='clear_basket'),
    path('main/tasks', tasks, name='tasks'),
    path('tasks/complete_task/<int:task_id>', complete_task, name='complete_task'),
]