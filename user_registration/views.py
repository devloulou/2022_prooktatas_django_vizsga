from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from my_blog.settings import EMAIL_HOST_USER

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # email küldés helye
            subject = "Regisztrált user"
            message = f"{username} regisztált az oldaladra"
            try:
                send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently=False)
            except:
                pass
            messages.success(request, f"Your account has been created You are able to login!")
            return redirect('login')
    else:
        form = UserRegisterForm()  
    return render(request, 'user_registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
                            request.POST, 
                            request.FILES, 
                            instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account hase been updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
        
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'user_registration/profile.html', context)