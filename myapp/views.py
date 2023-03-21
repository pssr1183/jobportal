from django.shortcuts import render,redirect
from .forms import Students,UserRegForm
from . import models
from django.views.generic import TemplateView,ListView
# Create your views here.
def show(request):
    form=Students(request.POST or None)
    if request.method=="POST":
        if form.is_valid:
            name=form['name'].value()
            roll_no=form['roll_no'].value()
            student=models.Student(name=name,roll_no=roll_no)
            student.save()
    else:
        form = Students()

    return render(request,'index.html',{'form':form})
# def display(request):
#     students=models.Student.objects.all()
#     return render(request,'display.html',{'students':students})
class disView(TemplateView):
    template_name='display.html'
    students=models.Student.objects.all()
    extra_context={'students':students}
class TempList(ListView):
    model=models.Student
    context_object_name='students'
    template_name='display.html'

def register(request):
    if request.method=='POST':
        form=UserRegForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)
            user.is_staff = form.cleaned_data['user_type'] == 'admin'
            user.is_superuser = form.cleaned_data['user_type'] == 'superuser'
            user.is_active = form.cleaned_data['is_active']
            user.save()
            return redirect('home')
    else:
        form = UserRegForm()
    return render(request, 'register.html', {'form': form})