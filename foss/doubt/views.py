from django.shortcuts import render,redirect,get_object_or_404
from .models import Question,Reply,UserProfile
from .forms import ReplyForm
from django.views import View
from django.views.generic import TemplateView
from .forms import ReplyForm,ProfileForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
        pass

def my_question(request):
        if request.user.is_authenticated():
                context={'question':request.user.user_profile.my_questions}
                return render(request,'doubt/my_question.html',context)
        else:
                return redirect('login')
def log_me_out(request):
        logout(request)
        return redirect('login')
class Question(View):
        def get(self,request,id):
                template_name='doubt/all_question.html'
                question=Question.objects.all().filter()
                context={'question':question}
                return render(request,template_name,context)

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
        
        def get(self,request):
                template_name='register/register.html'
                form=UserCreationForm()
                profile_form=ProfileForm()
                context={'form':form,'profile_form':profile_form}
                return render(request,template_name,context)
        def post(self,request):
                template_name='register/register.html'
                form=UserCreationForm(request.POST)
                profile=ProfileForm(request.POST,request.FILES)
                if form.is_valid():
                        #profile_form=profile_form.save(commit=False)
                        username=form.cleaned_data['username']
                        password=form.cleaned_data['password1']
                        form=form.save(commit=False)
                        form=form.save()
                        user=authenticate(username=username,password=password)
                        if user:
                                login(request,user)
                                profile=profile.save(commit=False)
                                print(profile)
                                print(form)
                                profile.user=user
                                print(profile)
                                profile.save()
                                return redirect('view_profile')
                else:
                        return redirect('register')

class ViewProfile(View):
        
        def get(self,request):
                template_name='login/profile.html'
                profile=request.user.user_profile
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







                




