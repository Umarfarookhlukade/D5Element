from django.shortcuts import render,redirect
from .models import therepy
# Create your views here.

def home(request):
    return render(request,"Home.html")



def about(request):
    return render(request,"about.html")

def details(request):
    if request.method=='POST':
        print("Added")

        # retrive the infromation from form
        n1 = request.POST.get('p_name')
        n2 = request.POST.get('p_address')
        n3 = request.POST.get('phone')
        n4 = request.POST.get('p_therepy')
        n5 = request.POST.get('fees')
        n6 = request.POST.get('date')
        n7 = request.POST.get('nextdate')

        # create an object for models to show and save
        s = therepy()
        s.p_name=n1
        s.address=n2
        s.phone=n3
        s.treatment=n4
        s.fees=n5
        s.date=n6
        s.nextdate=n7

        s.save()
        return redirect('details')
    return render(request,"details.html")

def catalog(request):
    return render(request,"catalog.html")


from django.db.models import Q
from django.contrib import messages

def search_details(request):
    if request.method == 'GET':
        search_query = request.GET.get('search_query')
        results = therepy.objects.filter(Q(p_name__icontains=search_query) | Q(phone__icontains=search_query))

         # Add a success message
        messages.success(request, 'Data submitted successfully.')

        return render(request, "catalog.html", {'results': results})
    return render(request, "catalog.html")


def reminder(request):
    return render(request,"reminder.html")


def therapy_list(request):
    # Retrieve records with only the required attributes
    records = therepy.objects.values('p_name', 'treatment', 'nextdate', 'phone')

    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        records = records.filter(p_name__icontains=search_query) | records.filter(nextdate__icontains=search_query)

    return render(request, 'reminder.html', {'records': records})




# Contact Page
def contact(request):
    return render(request,"contact.html")