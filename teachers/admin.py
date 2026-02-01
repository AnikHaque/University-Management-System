from django.contrib import admin
from .models import Teacher
from accounts.models import User

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'designation', 'department')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(role='TEACHER')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
