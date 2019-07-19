from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from .models import Question,Reply,UserProfile
from .forms import ReplyForm
from django.views import View
from django.views.generic import TemplateView
from .forms import ReplyForm,ProfileForm,AskQuestion
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
import social_django
from .choices import CHOICE
from django.http import Http404

# Create your views here.

def index(request):
        category=[]
        for some in CHOICE:
                category.append(some)
        question=Question.objects.all().order_by('-visited')
        context={'question':question,'category':category}
        return render(request,'doubt/index.html',context)

def my_question(request):
        if request.user.is_authenticated:
                question=request.user.user_profile.my_question.all()
                print(question)
                context={'question':question,'category':CHOICE}
                return render(request,'doubt/my_question.html',context)
        else:
                return redirect('login')
def log_me_out(request):
        logout(request)
        return redirect('login')
class ask_question(View):
        def get(self,request):
                form=AskQuestion()
                context={'form':form,}
                return render(request,'doubt/ask_question.html',context)
        def post(self,request):
                if request.user.is_authenticated:
                        form=AskQuestion(request.POST)
                        if form.is_valid():
                                form=form.save(commit=False)
                                ques=form
                                form.user=request.user
                                form.save()
                                profile=request.user.user_profile
                                new=profile.my_question
                                new.add(ques)
                                profile.save()
                                return redirect('view_question' ,id=ques.id)
                else:
                        return redirect('login')


class all_question(View):
        def __init__(self):
                self.template_name='doubt/question.html'
        def get(self,request):
                question=Question.objects.all()
                context={'question':question,'category':CHOICE}
                return render(request,self.template_name,context)

def view_question(request,id):
        question=get_object_or_404(Question,id=id)
        visit=question.visited
        if request.user.is_authenticated:
                if request.user not in visit.all():
                        visit.add(request.user)
                        question.save()
                if request.method=='POST':
                        form=ReplyForm(request.POST)
                        if form.is_valid():
                                form=form.save(commit=False)
                                form.user=request.user
                                form.save()
                                rep=question.reply
                                rep.add(form)
                                question.save()
        form=ReplyForm()
        context={'question':question,'form':form,'category':CHOICE}
        return render(request,'doubt/question_view.html',context)

class Register(View):
        def __init__(self):
                self.template_name='register/register.html'
        def get(self,request):
                form=UserCreationForm()
                profile_form=ProfileForm()
                context={'form':form,'profile_form':profile_form}
                return render(request,self.template_name,context)
        def post(self,request):
                form=UserCreationForm(request.POST)
                profile=ProfileForm(request.POST,request.FILES)
                if form.is_valid():
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
        def __init__(self):
                self.template_name='login/profile.html'
        def get(self,request):
                print(request.user.social_auth.get(provider='google-oauth2'))
                profile=request.user.user_profile
                context={'profile':profile}
                return render(request,self.template_name,context)

class EditProfile(View):
        def __init__(self):
                self.template_name='login/editprofile.html'
        def get(self,request):
                form=ProfileForm(instance=request.user.user_profile)
                context={'form':form}
                return render(request,self.template_name,context)
        def post(self,request):
                form=ProfileForm(request.POST,instance=request.user.user_profile)
                if form.is_valid():
                        form.save()
                        return redirect('edit_profile')
def filter(request,slug):
        question=Question.objects.filter(category=slug).order_by('-visited')
        context={'question':question,'category':CHOICE}
        return render(request,'doubt/index.html',context)

def search(request):
        slug=(request.GET.get('slug'))
        lis=slug.split(" ")
        ans=[]
        for some in lis:
                question=Question.objects.filter(question__icontains=some).order_by('-visited')
                ans+=question
                question=Question.objects.filter(content__icontains=some).order_by('-visited')
                ans+=question
        new=[]
        for some in ans:
                if some not in new:
                        new.append(some)
        print(new)
        context={'question':new,'category':CHOICE}
        return render(request,'doubt/question.html',context)
def liked_questions(request):
        if request.user.is_authenticated:
                question=request.user.user_profile.liked.all()
                context={'question':question,'category':CHOICE}
                return render(request,'doubt/question.html',context)
        else:
                raise Http404
def like_question(request,id):
        if request.method=='POST':
                question=get_object_or_404(Question,id=id)
                user=request.user
                if user:
                        profile = user.user_profile
                        liked=profile.liked
                        print(liked.all())
                        if question not in liked.all():
                                question.likes+=1
                                liked.add(question)
                        else:
                                question.likes-=1
                                liked.remove(question)
                        profile.save()
                        question.save()
                return redirect('view_question',id=id)
        else:
                raise Http404




                




