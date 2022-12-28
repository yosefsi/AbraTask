from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import massage_Form
from django.db import DatabaseError, transaction
from .models import *



def home(request):
    return render(request, 'APP/dashboard.html')


def massage(request):                    # ----------------------------------inbox
    massages = MASSAGE.objects.filter(Q(receiver=request.user))
    return render(request, 'APP/massages.html', {'massages': massages})


def outbox(request):
    massages = MASSAGE.objects.filter(Q(user=request.user))
    return render(request, 'APP/outbox.html', {'massages': massages})


def unread(request):
    massages = MASSAGE.objects.filter(Q(is_read=False) & (Q(receiver=request.user)))
    return render(request, 'APP/massages.html', {'massages': massages})


"""def create_massage(request):
    form = massage_Form()
    form.user = request.user
    if request.method == 'POST':
        form = massage_Form(request.POST)
        if form.is_valid():
            form.save()
            response = redirect('/massages')
            return response
    context = {'form': form}

    return render(request, 'APP/massage_form.html', context)"""


def deleteMassage_inbox(request, pk):
    u1 = MASSAGE.objects.get(id=pk)
    u1.delete()
    return redirect('massages')


def deleteMassage_outbox(request, pk):
    u1 = MASSAGE.objects.get(id=pk)
    u1.delete()
    return redirect('outbox')


def deleteMassage_unread(request, pk):
    u1 = MASSAGE.objects.get(id=pk)
    u1.delete()
    return redirect('outbox')


def readmassage_inbox(request, pk):
    massages = MASSAGE.objects.get(id=pk)
    massages.is_read = True
    try:
        with transaction.atomic():
            massages.save()
    except DatabaseError:
        massages.active = False
    return render(request, 'APP/read_massage.html', {'massages': massages})


def readmassage_outbox(request, pk):
    massages = MASSAGE.objects.get(id=pk)
    massages.is_read = True
    try:
        with transaction.atomic():
            massages.save()
    except DatabaseError:
        massages.active = False
    return render(request, 'APP/read_outbox.html', {'massages': massages})


def readmassage_unread(request, pk):
    massages = MASSAGE.objects.get(id=pk)
    massages.is_read = True
    try:
        with transaction.atomic():
            massages.save()
    except DatabaseError:
        massages.active = False
    return render(request, 'APP/read_unread.html', {'massages': massages})


def loginPage(request):
    if request.user.is_authenticated:
        response = redirect('/')
        return response
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                response = redirect('/')
                return response

            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'APP/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

