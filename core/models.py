from django.db import models
from django.utils import timezone

# Create your models here.

class Voice(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False, unique=True, verbose_name='Тип голоса')

    def to_json(self):
        return {'id': self.id, 'name': self.name}

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'voice_type'
        verbose_name = 'Тип голоса'
        verbose_name_plural = 'Типы голоса'

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False, unique=False, verbose_name='Имя')
    sec_name = models.CharField(max_length=50, blank=True, null=True, unique=False, verbose_name='Фамилия')
    voice = models.ForeignKey('Voice', on_delete=models.CASCADE, to_field='id', db_column='voice_id')
    age = models.PositiveIntegerField(default=0, verbose_name='Возраст')
    date_register = models.DateField(default=timezone.now)

    @property
    def full_name(self):
        return self.__str__()

    def __str__(self):
        if self.sec_name:
            return f'{self.sec_name} {self.name}'
        return self.name

    class Meta:
        db_table = 'person'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

