from django.contrib import admin
from .models import Student
from accounts.models import User

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'student_id', 'department', 'semester', 'status')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(role='STUDENT')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
