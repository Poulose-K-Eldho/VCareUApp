from django.urls import path
from. import views
app_name="FormApp"
urlpatterns=[
    path('',views.Form,name='Form'),
    path('submit/', views.Submit, name='Submit'),

]