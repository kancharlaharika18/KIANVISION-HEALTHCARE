from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import Patient, Doctor, Appointment

def home(request): 
    return render(request,'home.html',{'doctors':Doctor.objects.all()[:6]})

def about(request):
    return render(request,'about.html')

def patient_register(request): 
    if request.method=='POST':
        if Patient.objects.filter(email=request.POST.get('email')).exists():
            messages.error(request,"Email already exists!")
        else:
            Patient.objects.create(name=request.POST.get('name'),email=request.POST.get('email'),phone=request.POST.get('phone'),age=request.POST.get('age'),gender=request.POST.get('gender'))
            return redirect('/doctors/')
    return render(request,'patient_register.html')

def doctor_list(request): 
    q=request.GET.get('q','')
    doctors=Doctor.objects.filter(Q(name__icontains=q)|Q(specialization__icontains=q)) if q else Doctor.objects.all()
    return render(request,'doctor_list.html',{'doctors':doctors,'query':q})

def book_appointment(request,doctor_id=None): 
    if request.method=='POST':
        did=request.POST.get('doctor_id'); date=request.POST.get('date'); time=request.POST.get('time')
        if Appointment.objects.filter(doctor_id=did,date=date,time=time,status='Scheduled').exists():
            messages.error(request,"Doctor busy! Choose other slot"); return redirect('/book/')
        Appointment.objects.create(patient_id=request.POST.get('patient_id'),doctor_id=did,date=date,time=time)
        return redirect('/my-appointments/')
    sel=get_object_or_404(Doctor,id=doctor_id) if doctor_id else None
    return render(request,'book_appointment.html',{'patients':Patient.objects.all(),'doctors':Doctor.objects.all(),'selected_doctor':sel})

def my_appointments(request): 
    return render(request,'my_appointments.html',{'appointments':Appointment.objects.filter(status='Scheduled')})

def cancel_appointment(request,id): 
    a=get_object_or_404(Appointment,id=id); a.status='Cancelled'; a.save(); return redirect('/my-appointments/')

def complete_appointment(request,id): 
    a=get_object_or_404(Appointment,id=id); a.status='Completed'; a.save(); return redirect('/history/')

def appointment_history(request): 
    return render(request,'appointment_history.html',{'history':Appointment.objects.filter(status__in=['Completed','Cancelled'])})

def admin_dashboard(request): 
    return render(request,'admin_dashboard.html',{'total_patients':Patient.objects.count(),'total_doctors':Doctor.objects.count(),'total_appts':Appointment.objects.count(),'scheduled':Appointment.objects.filter(status='Scheduled').count(),'appointments':Appointment.objects.all()[:10]})


def manage_patients(request):
    patients = Patient.objects.all()
    return render(request, 'manage_patients.html', {'patients': patients})

def manage_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'manage_doctors.html', {'doctors': doctors})

def manage_appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'manage_appointments.html', {'appointments': appointments})