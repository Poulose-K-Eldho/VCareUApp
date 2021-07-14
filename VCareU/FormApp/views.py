from django.shortcuts import render,redirect

# Create your views here.
def Form(request):
    if request.method== "POST":
        return redirect('FormApp:Submit')
    return render(request,'form.html')
def Submit(request):
    return render(request,'submit.html')
