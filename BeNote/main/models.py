from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=60, verbose_name="")
    text = models.TextField(blank=True, verbose_name="")
    user_id = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    last_time_update = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")



class Basket_model(models.Model):
    title = models.CharField(max_length=60, verbose_name="Название записки")
    text = models.TextField(blank=True, verbose_name="Текст записки")
    user_id = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    last_time_update = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")
    date_delete = models.DateTimeField(auto_now_add=True, verbose_name="Дата удаления")

class Tasks_model(models.Model):
    text = models.CharField(max_length=110, verbose_name="Задача")
    user_id = models.CharField(max_length=255)
