from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import registerForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account has been created')
            return redirect('login')

    else: 
        form = registerForm()
    return render(request,'food/register.html',{'form':form})

@login_required #A decorator. Makes login required. If not, 404
def profilePage(request):
    return render(request,'profile.html',{})