from django.shortcuts import render
from sexeduapp.forms import UserForm, UserProfileInfoForm,LaporanForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.utils import timezone


from sexeduapp.models import Laporan


def index(request):
    return render(request, 'sexeduapp/index.html')

def course(request):
    return render(request, 'sexeduapp/course.html')

# def report(request):
#     return render(request, 'sexeduapp/report.html')
def report(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        deskripsi = request.POST.get('deskripsi')

        laporan_baru = Laporan(nama=nama, email=email, deskripsi=deskripsi, waktu_laporan=timezone.now())
        laporan_baru.save()

        # Redirect atau tampilkan halaman berhasil
        return request('sexeduapp:pesanberhasil')  

    
    return render(request, "sexeduapp/report.html")

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                
                return HttpResponseRedirect(reverse("index"))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print(f"Username: {username} and password: {password}")
            return HttpResponse("Invalid login details supplied!")
    else:
        return render(request, "sexeduapp/login.html")

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # Hash the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'sexeduapp/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })

def class_content(request):
    return render(request, 'sexeduapp/class_content.html')

def about(request):
    return render(request, 'sexeduapp/about.html')

def loginpage(request):
    return render(request, 'sexeduapp/login.html')

def dashboard(request):
    return render(request, 'sexeduapp/dashboard.html')

def dashboardclass(request):
    return render(request, 'sexeduapp/dashboardclass.html')

def pesanberhasil(request):
    return render(request, 'pesanberhasil.html')

# def report_view(request):
#     if request.method == 'POST':
#         form = LaporanForm(data=request.POST)
        
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('index'))  # Redirect to success page after saving data
#     else:
#         form = LaporanForm()

#     return render(request, 'report.html', {'form': form})

def pesanberhasil_view(request):
    return render(request, 'pesanberhasil.html')


def report_view(request):
    if request.method == 'POST':
        form = LaporanForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('sexeduapp:pesanberhasil'))  # Redirect to success page after saving data
    else:
        form = LaporanForm()

    return render(request, 'sexeduapp/report.html', {'form': form})
