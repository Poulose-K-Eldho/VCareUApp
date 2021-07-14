from django.shortcuts import render,get_object_or_404
from .models import Department,Doctor
from django.core.paginator import Paginator,InvalidPage,EmptyPage
# Create your views here.
def allDept(request,d_slug=None):
    d_page=None
    doctors=None
    if d_slug!=None:
        d_page=get_object_or_404(Department,slug=d_slug)
        doctors=Doctor.objects.filter(department=d_page,available=True)
    else:
        doctors=Doctor.objects.all().filter(available=True)
    paginator=Paginator(doctors,3)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        doctors=paginator.page(page)
    except(EmptyPage,InvalidPage):
        doctors=paginator.page(paginator.num_pages)

    return render(request,'department.html',{'department':d_page,'doctors':doctors})
def DocDetail(request,d_slug,doc_slug):
    try:
        doctor=Doctor.objects.get(department__slug=d_slug,slug=doc_slug)
    except Exception as e:
        raise e
    return render(request,'doctor.html',{'doctor':doctor})
