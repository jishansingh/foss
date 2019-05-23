from django.shortcuts import render,redirect,get_object_or_404
from .models import Question,Reply,UserProfile
from .forms import ReplyForm
from django.views import View
from django.views.generic import TemplateView
from .forms import ReplyForm,ProfileForm
from django.contrib.auth import login,authenticate

# Create your views here.
def index(request):
    if request.user.is_authentcated():
        request.user.user_profile.

def my_question(request):
    if request.user.is_authenticated():
        context={'question':request.user.user_profile.my_questions}
        return render(request,'doubt/my_question.html',context)
    else:
        return redirect('login')

class Question(View):
        def get(self,request,id):
                template_name='doubt/all_question.html'
                question=Question.objects.all().filter()
def view_question(request,id):
        question=get_object_or_404(Question,id=id)
        if request.user.is_authenticated():
                if request.method=='POST':
                        form=ReplyForm(request.POST)
                        form=form.save(commit=False)
                        form.user=request.user
                        form.save()
                        rep=question.reply
                        rep.add(form)
                        question.save()
        form=ReplyForm()
        context={'question':question,'form':form}
        return render(request,'doubt/question.html',context)

class Register(View):
        template_name='register/register.html'
        def get(self,request):
                form=UserCreationForm()
                profile_form=ProfileForm()
                context={'form':form,'profile_form':profile_form}
                return render(request,template_name,context)
        def post(self,request)
                form=UserCreationForm(request.POST)
                profile_form=ProfileForm(request.POST,request.FILES)
                if form.is_valid():
                        form=form.save(commit=False)
                        profile_form=profile_form.save(commit=False)
                        username=form.cleaned_data('username')
                        password=form.cleaned_data('password1')
                        form.save()
                        user=authenticate(username=username,password=password)
                        if user:
                                login(request,user)
                                profile_form.user=user
                                profile_form.save()
                                return redirect('profile')
                else:
                        return redirect('register')

class ViewProfile(View):
        template_name='login/profile.html'
        def get(self,request):
                context={'profile':profile}
                return render(request,template_name,context)

class EditProfile(View):
        template_name='login/editprofile.html'
        def get(self,request):
                form=ProfileForm(instance=request.user.user_profile)
                context={'form':form}
                return render(request,template_name,context)
        def post(self,request):
                form=ProfileForm(request.POST,instance=request.user.user_profile)
                if form.is_valid():
                        form.save()
                        return redirect('edit_profile')







                




