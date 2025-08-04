from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Optional: auto-login after signup
            return redirect('home')  # Change 'home' to your desired page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def custom_logout_view(request):
    messages.success(request, "You’ve been logged out.")
    return redirect('login')

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')



