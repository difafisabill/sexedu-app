# sexeduapp/urls.py
from django.urls import path # type: ignore
from . import views

app_name = 'sexeduapp'

urlpatterns = [
    path('course/', views.course, name='course'),
    path('class_content/', views.class_content, name='class_content'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('register/', views.register, name='register'),
    path('report/', views.report, name='report'),
    path('about/', views.about, name='about'),
    path("user_login/", views.user_login, name="user_login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboardclass/", views.dashboardclass, name="dashboardclass"),
    path('pesanberhasil/', views.pesanberhasil, name='pesanberhasil'), 
    path('laporan/', views.Laporan, name='Laporan'),
    path('report_view/', views.report_view, name='report_view'),
    path('pesanberhasil/', views.pesanberhasil_view, name='pesanberhasil'),
    





    # URL pattern lainnya
]
