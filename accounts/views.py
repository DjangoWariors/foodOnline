from ast import If
from contextvars import Context
from django.shortcuts import redirect, render
from django.core.mail import message
from accounts.models import User
from .forms import UserForm

# Create your views here.

def registerUser(request):

    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            form.save()
            messages.success(request, 'Your account has been registered sucessfully!')
            return redirect('registerUser')
        else:
            context = {
            'form':form,
        }

        return render(request, 'accounts/registerUser.html',context)
    else:
        form = UserForm()    

    form = UserForm()
    context = {
        'form':form,
    }

    return render(request, 'accounts/registerUser.html',context)