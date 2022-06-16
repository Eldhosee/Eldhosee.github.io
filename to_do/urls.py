from django.urls import URLPattern, path
from to_do import views

urlpatterns=[
    path('',views.index,name='index'),
    path('delete/<str:pk>',views.delete,name="delete"),

]