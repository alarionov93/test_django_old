from django.db import models
from django.utils import timezone
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


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


class Snippet(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey('Person', related_name='snippets', default=1, on_delete=models.CASCADE)
    highlighted = models.TextField(blank=True, null=True, unique=False)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['created']

