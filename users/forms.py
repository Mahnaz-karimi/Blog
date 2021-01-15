from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm): # bruge crationform og tilføje en ny felt
    email = forms.EmailField() # adder en felt for at adde emil

    class Meta: # meta classe giv os en nested namespace for configurations in i en plads
        # så vil bruge den class i vores views for at hav email felt også
        model = User # bruge vi user class fordi hver gang form bliver validate en ny user bliver oprettet
        fields = ['username', 'email', 'password1', 'password2']