import wolframalpha
import wikipedia
import webbrowser
from django.shortcuts import render, redirect
from django.contrib import messages
import random
from django.http import HttpResponse
from .models import Contact
from django.contrib.auth.models import User, auth
import requests


fine = ['how are you', 'what\'s up', 'how are you doing']
sad = ['i am sad', 'i am very sad', 'iam very sad', 'iam sad']
feel = ['what do you feel', 'can you feel', 'how do you feel', 'tell me about your feelings']
language = ['what language do you speak', 'your language', 'which language do you know', 'what is your language', 'do you know any language']
made = ['who made you']
how = ['how you were made', 'how you were programmed']
name = ['what is your name', 'your name', 'who are you']
do = ['what can you do']
hi = ['hi', 'hi how are you']
weather = ['what is the weather of today?' 'the weather of today', 'the weather', "what is today's weather?" ]

client = wolframalpha.Client('XXV62Y-J775ELR3AV')

def index(request):
    return render(request, 'index.html')

def bot(request):
    return render(request, 'chat.html')

def response(request):
    query = request.POST['query']
    que = query
    query = query.lower()

    if query in fine:
        stMsgs = ['I am fine.', 'I am full of energetic.', 'I am very fine.']
        results = random.choice(stMsgs)
    elif 'wikipedia' in query:
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=1)
    elif query in sad:
        results = 'I am sorry. Hope you will fine.'           
    elif query in name:
        results = 'my name is Zarif\'s chatbot'
    elif query in do:
        results = 'I can do many thing.'
    elif 'hello' in query:
        results = 'Hello Sir! I am your digital assistant  Zarif\'s Chatbot.'
    elif query in feel:
        results = 'I am a robot. I don\'t have feelings.'
    elif query in made:
        results = 'I was made by my friend Zarif. He is my owner.'
    elif query in hi:
        stMsgs = ['Hi Sir! Hope you are well', 'Hi Sir!', 'Hi Sir! Thank you.']
        results = random.choice(stMsgs)
    elif query in how:
        results = 'I can\'t tell you how i was programmed. you can only get my api from my friend and owner Zarif.'
    elif query in language:
        results = 'I am only know python because i was programmed on it. English was programmed in my machine by Zarifsoftware\'s owner Sadman Islam Zarif.'
    elif 'open ' in query:
        if 'open yahoo' in query:
            results = query
            return redirect('https://yahoo.com')
        elif 'open google' in query:
            results = query
            return redirect('https://google.com')
        elif 'open facebook' in query:
            results = query
            return redirect('https://facebook.com')
        elif 'open youtube' in query:
            results = query
            return redirect('https://youtube.com')
        elif 'open messenger' in query:
            results = query
            return redirect('https://messenger.com')
        elif 'open twitter' in query:
            results = query
            return redirect('https://twitter.com')
        elif 'open linkedin' in query:
            results = query
            return redirect('https://linkedin.com')
        elif 'open github' in query:
            results = query
            return redirect('https://github.com')
        else:
            query = query.replace('open', '')
            query = query.replace(' ', '')
            results = 'https://'+ query
            # print(results)
            return redirect(results)

    elif query == 'the weather':
        results = 'Opening our Weather Site. You can search your city\'s Weather.'
        return render(request, 'weather.html')

    elif bool(query) == False:
        query = ''
        results = ''
    elif 'bye' in query:
        results = 'Bye Sir, have a good day.'
    else:
        try:
            res = client.query(query)
            results = next(res.results).text
        except:
            results = wikipedia.summary(query, sentences=1)

    return render(request, 'chat.html', {'que': que , 'ans': results})

def contact(request):
    return render(request, 'contact.html')

def con(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    print(name, email, phone, message)
    contact= Contact(name=name, email=email, phone=phone, content=message)
    Contact.save(contact)
    messages.success(request,'Successfully your message has been sent.')
    return render(request, 'contact.html')

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,'Successfully Logged in')
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')
            return redirect('/')
    else:
        return redirect('/')    

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email Taken')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.success(request,'user created')
                return redirect('/')

        else:
            messages.error(request,'password not matching..')    
            return redirect('register')
        
        
    else:
        return redirect('/')



def logout(request):
    auth.logout(request)
    messages.success(request,'Succesfully logged out')
    return redirect('/')       

def profile(request):
    return render(request, 'profile.html')

def weather(request):
    return render(request, 'weather.html')

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def get_weather(request):
    city = request.POST['city']
    weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    if not city == '':
        params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
        response = requests.get(url, params=params)
        weather = response.json()
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
    else:
        name = ''
        desc = ''
        temp = ''
    return render(request, 'weather.html', {'name':name , 'desc':desc, 'temp':temp})
