from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'STUDENT'   # default role
            user.save()
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard(request):
    user = request.user

    if user.role == 'ADMIN':
        return render(request, 'dashboard/admin_dashboard.html')
    elif user.role == 'TEACHER':
        return render(request, 'dashboard/teacher_dashboard.html')
    else:
        return render(request, 'dashboard/student_dashboard.html')
