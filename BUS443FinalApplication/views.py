from django.shortcuts import render
from django.http import HttpResponse
from BUS443FinalApplication.models import CourseDetails
from BUS443FinalApplication.models import StudentDetails
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    
@login_required
def home(request):
    cursorobj = connection.cursor()
    cursorobj.execute('SELECT COUNT(*) FROM bus443finalapplication_studentdetails')
    studentsdata = dictfetchall(cursorobj)
    context = {'studentsdata': studentsdata}
    return render(request, 'bus443finalapplication/home.html', context)
    
    
@login_required   
def studentdetails(request):
    studentdetailsdata = StudentDetails.objects.all()
    paginator = Paginator(studentdetailsdata, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data' :minidata}
    return render(request, 'bus443finalapplication/studentdetails.html', context)


@login_required    
def coursedetails(request):
    coursedetailsdata = CourseDetails.objects.all()
    paginator = Paginator(coursedetailsdata, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data' :minidata}
    return render(request, 'bus443finalapplication/coursedetails.html', context)
    