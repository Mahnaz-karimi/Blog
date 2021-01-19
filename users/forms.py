from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# model form giv lov til at skabe a form som vil arbejde med en database
from .models import Profile
class UserRegisterForm(UserCreationForm): # bruge crationform og tilføje en ny felt
    email = forms.EmailField() # adder en felt for at adde emil

    class Meta: # meta classe giv os en nested namespace for configurations in i en plads
        # så vil bruge den class i vores views for at hav email felt også
        model = User # bruge vi user class fordi hver gang form bliver validate en ny user bliver oprettet
        fields = ['username', 'email', 'password1', 'password2'] # user register form vil ha 4 felter for en user bliver oprettet


class UserUpdateForm(forms.ModelForm): # den form dukkes up ind i users profilens side og vil opdates username og email
    email = forms.EmailField()

    class Meta:
        model = User # det model vil vi arbjede med vil vil kaldes
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm): # den method vil opdatere image
    class Meta:
        model = Profile # den model vi bruger her er  profile model. så derfor skriver vi under 2 methode og derefter kalder vi dem under views.py for at de kan opdatere userprofile
        fields = ['image']