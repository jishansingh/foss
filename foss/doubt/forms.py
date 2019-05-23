from django import forms
from .models import Reply,Question,UserProfile
class ReplyForm(forms.ModelForm):
    class Meta:
        model=Reply
        fields=('content','anonymous',)
class AskQuestion(forms.ModelForm):
    class Meta:
        model=Question
        fields=('question','content','category')
class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('photo','email','roll_no')





