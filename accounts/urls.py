from django.urls import path
from . import views
urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('reset', views.reset, name='reset_password'),
    path('edit', views.edit, name='edit'),
    path('changelogin', views.changelogin, name='changelogin')
]
