from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from .models import Employee
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# # Create your views here.

# def index(request):
#     employees = Employee.objects.all()
#     return render(request,'index.html',{'employees':employees})

# def add(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         employee = Employee(name=name,email=email,address=address,phone=phone)
#         employee.save()
#         return redirect('index')
#     else:
#         return render(request,'index.html')

# def edit(request):
#     employees = Employee.objects.all()
#     return redirect(request,'index.html',{'employees':employees})

# def update(request,id):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         employee = Employee(id=id,name=name,email=email,address=address,phone=phone)
#         employee.save()
#         return redirect('index')
#     return render(request,'index.html')

# def delete(request,id):
#     employee = Employee.objects.get(id=id)
#     employee.delete()
#     return redirect('index')



# ++++++++++++++++++++ another method +++++++++++++++++++++





class EmployeeListView(ListView):
    model = Employee
    template_name = 'index.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['name', 'email', 'address', 'phone']
    success_url = reverse_lazy('index')
    template_name = 'index.html'

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['name', 'email', 'address', 'phone']
    success_url = reverse_lazy('index')
    template_name = 'index.html'

class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy('index')

@require_POST
def delete_selected(request):
    employee_ids = request.POST.getlist('employee_ids[]')
    deleted_count = Employee.objects.filter(id__in=employee_ids).delete()
    return redirect('index')
