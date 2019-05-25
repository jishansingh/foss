from django import forms
from .models import Reply,Question,UserProfile
from django.contrib.auth.models import User
class ReplyForm(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control','placeholder':'what do you think??'}))
    anonymous=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'onoffswitch','id': 'myonoffswitch'}))
    class Meta:
        model=Reply
        fields=('content','anonymous',)
class AskQuestion(forms.ModelForm):
    question=forms.CharField(widget=forms.TextInput(attrs={'class' : 'input100','placeholder':'Short note on Question'}))
    content=forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control','placeholder':'Details of Question'}))
    class Meta:
        model=Question
        fields=('question','content','category')
class ProfileForm(forms.ModelForm):
    photo=forms.ImageField(widget=forms.FileInput(attrs={'class':'container'}))
    class Meta:
        model=UserProfile
        fields=('photo','email','roll_no')
        widgets = {
            'roll_no': forms.TextInput(attrs={'class': 'input100'}),
            'email': forms.EmailInput(attrs={'class': 'input100'}),
        }
class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input100','placeholder':'Type your username'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'input100','placeholder':'Type your password'}))
    class Meta:
        model=User
        fields=('username','password',)






