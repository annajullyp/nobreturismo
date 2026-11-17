from django.contrib import admin
from .models import Guia, Experiencia


@admin.register(Guia)
class GuiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_editable = ('ativo',)
    search_fields = ('nome', 'descricao')
    list_filter = ('ativo',)

@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_editable = ('ativo',)
    search_fields = ('nome', 'descricao')
    list_filter = ('ativo',)