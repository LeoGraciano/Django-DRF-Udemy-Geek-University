from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'url', 'criacao', 'atualizacao', 'ativo')


@admin.register(models.Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('curso', 'nome', 'email', 'avaliacao',
                    'criacao', 'atualizacao', 'ativo')
