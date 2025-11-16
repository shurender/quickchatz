from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
import random
import string
from .models import ChatRoom , Message

# home , signup, login, logout
def home(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =request.POST['password']

        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'signup.html')


def login_view(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('home')
    return render(request, 'login.html')
        

def logout_view(request):
    logout(request)
    return redirect('home')


#rooms creation
def room(request,code):
    room = ChatRoom.objects.get(code=code)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    return render(request, 'room.html', {
        'room': room,
        'messages': messages
    })     

def rooms(request):
    chat_rooms = ChatRoom.objects.all()
    return render(request,'rooms.html', {'rooms': chat_rooms})

def create_room(request):
    if request.method == 'POST':
        name = request.POST['name']
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

        ChatRoom.objects.create(name=name, code=code)
        return redirect('home')
    return render(request, 'create_room.html')

