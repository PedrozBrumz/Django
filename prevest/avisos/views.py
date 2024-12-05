from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CustomUserCreationForm
from .models import Aviso

# Create your views here.


def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('avisos')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    avisos = Aviso.objects.all() if request.user.is_authenticated and request.user.is_teacher else []
    return render(request, 'home.html', {'avisos': avisos})

@login_required
@user_passes_test(lambda u: u.is_coordinator)
def post_aviso(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:  # Certifique-se de que os campos não estão vazios
            Aviso.objects.create(title=title, content=content, author=request.user)
            return redirect('avisos')
    
    return render(request, 'post_aviso.html')
    
def avisos(request):
    avisos = Aviso.objects.all().order_by('-created_at')
    return render(request, 'avisos.html', {'avisos': avisos})