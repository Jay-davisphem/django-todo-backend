from django.contrib import admin
from .models import Todo

# Register your models here.

admin.site.site_header = 'WannaDo Admin'
admin.site.site_title = 'WannaDo-api'


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')


admin.site.register(Todo, TodoAdmin)
