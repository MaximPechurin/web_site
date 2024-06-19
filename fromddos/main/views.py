from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout





def home_page(request):
    return render(request, 'main/home.html')

def about_page(request):
    return render(request, 'main/about.html')

def smart_page(request):
    return render(request, 'main/smart.html')

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('main/home.html')
            else:
                return render(request, 'registration/register.html', {'form': form, 'error':'Не удалось авторизоваться'})
        else:
            form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})