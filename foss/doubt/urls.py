from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('',views.index,name='index'),
    path('social/',include('social_django.urls', namespace='social')),
    path('ask/',views.ask_question.as_view(),name='ask_question'),
    path('login/',LoginView.as_view(template_name='login/login.html'),name='login'),
    path('logout/',views.log_me_out,name='logout'),
    path('my-ques/',views.my_question,name='my_question'),
    path('question/<id>',views.view_question,name='view_question'),
    path('all/',views.all_question.as_view(),name='question'),
    path('register/',views.Register.as_view(),name='register'),
    path('profile/',views.ViewProfile.as_view(),name='view_profile'),
    path('edit/',views.EditProfile.as_view(),name='edit_profile'),
]
