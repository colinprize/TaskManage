from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "is_completed",
        "id",
    )
