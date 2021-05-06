#i created this urls.py file firs
# copied the 1st line from main url
#imported view from all "."


from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add',views.add, name='add')
]