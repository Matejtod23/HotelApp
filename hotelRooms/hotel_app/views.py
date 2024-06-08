from django.shortcuts import render, redirect

from hotel_app.models import Room, Reservation
from hotel_app.forms import ReservationForm, RoomForm

# Create your views here.
def index(request):
    rooms = Room.objects.filter(is_clean=True, numberOfBeds__lt=5).all()
    return render(request, 'index.html', {"rooms": rooms})

def add_reservation(request):
    form = ReservationForm()
    if request.method == 'POST':
        res_form = ReservationForm(request.POST, files=request.FILES)
        if res_form.is_valid():
            reservation = res_form.save(commit=False)
            reservation.id_image = res_form.cleaned_data['id_image']
            reservation.user = request.user
            reservation.save()
        return redirect("index")

    return render(request, 'add_reservation.html', {"form": form})

def details(request, room_id):
    room = Room.objects.get(id=room_id)
    return render(request, 'details.html', {'room': room})

def edit_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = RoomForm(instance=room)

    return render(request, 'edit_room.html', {'form': form})

def reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations.html', {"reservations": reservations})