from django.urls import path

from VCareUApp import views
app_name='VCareUApp'
urlpatterns=[
    path('',views.allDept,name='allDept'),
    path('<slug:d_slug>/',views.allDept,name='doctors_department'),
    path('<slug:d_slug>/<slug:doc_slug>/', views.DocDetail, name='DocDetail')

]