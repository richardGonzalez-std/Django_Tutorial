from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name ="index"),
    path('richard',views.name, name="richard"),
    path('<str:name>',views.greet,name="name")
]