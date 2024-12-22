from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import ItemList,Item,AboutUs,FeedBack,BookTable

# Create your views here.
def HomeView(request):
    items = Item.objects.all()
    lists = ItemList.objects.all()
    reviews = FeedBack.objects.all()
    return render(request,'index.html',{'items':items,'lists' : lists,'reviews':reviews})

def AboutView(request):
    details = AboutUs.objects.all()
    return render(request,'about.html',{'details':details})

def MenuView(request):
    items = Item.objects.all()
    lists = ItemList.objects.all()
    return render(request,'menu.html',{'items':items,'lists' : lists})

def BookTableView(request):
    if request.method == 'POST':
        # Accessing POST data correctly
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        total_person = request.POST.get('total_person')
        booking_data = request.POST.get('booking_data')
        data = BookTable(
                name=name,
                phone_number=phone_number,
                email=email,
                total_person=total_person,
                booking_data=booking_data  # Note corrected variable name
            )
        data.save()
        # Ensure no fields are empty before saving
        # if all([name, phone_number, email, total_person, booking_date]):
        #     data = BookTable(
        #         name=name,
        #         phone_number=phone_number,
        #         email=email,
        #         total_person=total_person,
        #         booking_date=booking_date  # Note corrected variable name
        #     )
        #     data.save()

    return render(request, 'book.html')  # Render the booking form

def FeedBackView(request):
    return render(request,'feedback.html')


