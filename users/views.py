from django.shortcuts import render, redirect
from django.contrib import messages
#from .forms import UserCreationForm  # django har en indbygget form for registration
#from django.contrib.auth.forms import UserCreationForm # django har en indbygget form for registration
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} has been createt!') # f string som formatere string
            return redirect('login') # hvis formen er valid så vil redirect den til sidst til url pattern for repport blog
    else:
        form = UserRegisterForm() # create a form som vi vil sende til vores template
    return render(request, 'users/register.html', {'form': form}) # sender form som a variable
#for at style tamplaten og nemt at bruge. den hjælper os med at put simple tags in tamplaten

@login_required # login side vil krævs brugeren har logget ind  for at vise profile side. en decorator adder en funktion til en ekstierne funktion
def profile(request):
    return render(request, 'users/profile.html')