from django.contrib import admin
from . import models

# @admin.register(models.Profile_User)
# class Profile_UserAdmin(admin.ModelAdmin):
#     list_filter = ['sexo']
#     search_fields = ['nome']
#     list_display = ['nome', 'sobrenome', 'user_photo', 'sexo', 'email', 'tel', 'endereco', 'localidade', 'obs']
#     list_per_page = 8