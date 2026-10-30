from django.urls import path
from . import views
urlpatterns=[
 path('',views.home), path('about/',views.about), path('register/',views.patient_register),
 path('doctors/',views.doctor_list), path('book/',views.book_appointment),
 path('book/<int:doctor_id>/',views.book_appointment),
 path('my-appointments/',views.my_appointments),
 path('cancel/<int:id>/',views.cancel_appointment),
 path('complete/<int:id>/',views.complete_appointment),
 path('history/',views.appointment_history),
 path('dashboard/',views.admin_dashboard),
 path('add-bulk-doctors/', views.add_bulk_doctors, name='add_bulk_doctors'),
 path('manage-patients/', views.manage_patients, name='manage_patients'),
 path('manage-doctors/', views.manage_doctors, name='manage_doctors'),
 path('manage-appointments/', views.manage_appointments, name='manage_appointments'),
]

