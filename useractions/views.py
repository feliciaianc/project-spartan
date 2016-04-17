from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from useractions.models import Announcement
from authentication.models import Account,Spartan
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .forms import ProfileEditForm, PostForm, SpartanForm
import md5
import datetime
from django.contrib.auth.decorators import login_required



@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


@login_required
def create_post(request):
    curruser = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            post_text = form.cleaned_data['text']
            adress = form.cleaned_data['adress']
            country = form.cleaned_data['country'] 
            city = form.cleaned_data['city']
            category = form.cleaned_data['category']
            time = form.cleaned_data['timePost']
            time = ":".join(map(lambda item: item.strip(), time.split(":")))
            data_post = form.cleaned_data['data']
            data_post=datetime.datetime.strptime(data_post, '%m/%d/%Y').strftime('%Y-%m-%d')
            money_user = form.cleaned_data['price']
            announcement = Announcement.objects.create(title=title, text=post_text, address=adress, country=country,
                                                       category=category,money =money_user, city=city,data=data_post, timePost=time, author=request.user)
            announcement.save()
            subject='Anunt Project Spartan'
            messagetip=" Buna % s , \n Ati postat un anunt cu succes! \n" \
                " Titlul : %s ,\n Text: %s \n Adress: %s \n Country : %s \n City: %s \n category: %s \n" \
                " Time : %s \n Data indepliniri task-ului: %s \n " \
                "Suma maxima pentru licitatie: %s lei \n O zi buna!"  %(request.user.username,title,post_text,adress,country,city,category,time,data_post,money_user)
            from_email=settings.EMAIL_HOST_USER
            send_mail(subject, messagetip, from_email,
                      [request.user.email], fail_silently=True)
            return redirect('/')
        else:
            return render(request, 'useractions/create_post.html', {
                'cod': curruser.account.cod,
                'form': form,
                'errors': ['Invalid form'] })
    else:
        form = PostForm()
        if request.user.is_active and not  request.user.is_superuser:
            return render(request, 'useractions/create_post.html', {
                'cod': curruser.account.cod,
                'form': form})
        else:
            return render(request, 'useractions/create_post.html', {
                'cod': '61e1380365703a4c73c2480673d8993b',
                'form': form})


@login_required
def profile(request):
    curruser = request.user
    now = datetime.datetime.now()
    form = ProfileEditForm
    if request.method == 'POST':
    
        if request.user.is_active and not  request.user.is_superuser:
            return render(request, 'useractions/profile.html', {
                'cod': curruser.account.cod,
                'form': form
            })
        
        else:
            return render(request, 'useractions/profile.html', { 
                'cod': 1,
                'form':form})

    else:
        if request.user.is_active and not  request.user.is_superuser:
            return render(request, 'useractions/profile.html', {
                'cod': curruser.account.cod,
                'form': form, })
        else:
            return render(request, 'useractions/profile.html',{
                'cod': '61e1380365703a4c73c2480673d8993b',
                'form': form })
              

@login_required
def category(request, kind):
    an = Announcement.objects.filter(category=kind)
    curruser = request.user
    if request.user.is_active and not  request.user.is_superuser:
        return render(request, 'useractions/category.html', {
        'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others'],
        'kind': kind,
        'cod': curruser.account.cod,
        'ann': an
        })
    else: return render(request, 'useractions/category.html', {
        'categories': ['Garden', 'Moving', 'Cleaning', 'Babysitting', 'Cooking', 'Others'],
        'kind': kind,
        'cod': '61e1380365703a4c73c2480673d8993b',
        'ann': an
    })

def profileGeneral(request):
    return render(request, 'useractions/profilegeneral.html')



@login_required
def spartan(request):
    curruser = request.user
    if request.method == 'POST':
        form = SpartanForm(request.POST)
        if form.is_valid():
            nume = form.cleaned_data['nume']
            prenume = form.cleaned_data['prenume']
            data_nasterii = form.cleaned_data['data']
            data_nasterii=datetime.datetime.strptime(data_nasterii, '%m/%d/%Y').strftime('%Y-%m-%d')
            adress = form.cleaned_data['adress']
            cnp = form.cleaned_data['CNP']
            serie = form.cleaned_data['serie']
            cui = form.cleaned_data['cui']
            contBancar = form.cleaned_data['cont']
            abilitate1 = form.cleaned_data['abilitate1']
            abilitate2 = form.cleaned_data['abilitate2']
            abilitate3 = form.cleaned_data['abilitate3']
            spartan = Spartan.objects.create(nume=nume, prenume=prenume, data_nasterii=data_nasterii,
                                             address=adress, cnp=cnp,serie=serie,cui=cui,
                                             contBancar=contBancar,
                                             abilitate1=abilitate1,abilitate2=abilitate2,
                                             abilitate3=abilitate3,
                                             author=request.user)
            spartan.save()
            subject='Activare putere de Spartan'
            messagetip=" Buna % s , \n Ati completat formularul pentru activare puterii de Spartan \n" \
                " Nume : %s ,\n Prenume: %s \n Data nasterii: %s \n Adresa : %s \n CNP: %s \n Serie: %s \n" \
                " CUI : %s \n Cont Bancar: %s \n " \
                "Abilitate 1: %s  \n Abilitate 2: %s \n Abilitate 3:%s \n Datele dvs. vor fi analizate de Admin in vederea Activarii Puterii de Spartan \nO zi buna!"  %(request.user.username,nume,prenume,data_nasterii,adress,cnp,serie,cui,contBancar,abilitate1,abilitate2,abilitate3)
            from_email=settings.EMAIL_HOST_USER
            send_mail(subject, messagetip, from_email,
                      [request.user.email], fail_silently=True)
            return render(request, 'useractions/spartan.html' ,{'errors': ['Ati completat cu succes formularul,asteptati confirmarea administratorului!'],
                                                                    'cod': request.user.account.cod,
                                                                    'form': form})
        else:
            return render(request, 'useractions/spartan.html', {'cod': request.user.account.cod,
                                                                    'form': form,
                                                                    'errors':['Invalid form']
            })
    else:
        form = SpartanForm()
        if request.user.is_active and not  request.user.is_superuser:
            return render(request, 'useractions/spartan.html', {'cod': request.user.account.cod,
                                                                        'form': form})
        else :
            return render(request, 'useractions/spartan.html', {'cod': 1,
                                                                    'form': form })



