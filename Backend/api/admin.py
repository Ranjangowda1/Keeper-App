from django.contrib import admin
from .models import Note

@admin.register(Note)
class Noteadmin(admin.ModelAdmin):
    list_display=['id','title','content','created_at','author']

# Register your models here.
