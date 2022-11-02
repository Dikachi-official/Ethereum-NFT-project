from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User  # To be able to use the user function at (myuser(variable)
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
#for django to authenticate the user to check if password and email being entered is same as that in our db
from .models import Profile
from login import settings



# Create your views here.
def home(request):
    if request.method != "POST":
        return HttpResponse("Method not Allowed")
        return redirect('signup')

    if error_403:
        return redirect('error_403')    

    else:
        return render(request, "home.html") 


def error_403(request, exception):
    return render(request,"error_403.html")        

def signup(request):
    if request.method == "POST":
        # username = request.POST.get/
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if request.method != "POST":
            return HttpResponse("Method not Allowed")
        
        if User.objects.filter(username = username): #if we query database and see inputed username exist then reply
            messages.error(request, "Username already exists! Please try another username")
            return redirect('signup')
            
        if User.objects.filter(email =email): #if we query database and see inputed email exist then reply
            messages.error(request,"Email already registered")
            return redirect('signup')
        
        if len(username)>10: 
            messages.error(request,"Username must be a maximum of 10 characters")
            return redirect('signup')
            
        if pass1 != pass2:
            messages.error(request,"Passwords don't match")
            return redirect('signup')
            
        if not username.isalnum(): #If username is something other than alpha-numeric
            messages.error(request,"Username must be Alphanumeric")
            return redirect('signup')           
                
        #variable(or object) = create a user for me whose username, email, password is (the attributes from the users signup input) 
        myuser = User.objects.create_user(username, email, pass1) #pass these input to the object 'myuser'
        myuser.first_name = fname #pass fname input to the myuser object
        myuser.last_name =lname   #pass fname input to the myuser object
        
        myuser.save()  # To save this in the database
        
        messages.success(request, "Your Account has been successfully created.")  # pop up message after registration
        
        
        #Welcome Email
        subject = "welcome to the login page"
        message = "hello" + myuser.first_name + "!! \n" + "Welcome to Myke Nft!!  \n Thank You for your partnership with us \n"
        
        
        return redirect('signin') #after registration, user should be redirected to the login place    
    return render(request, "signup.html")


def signin(request): 
    if request.method == "POST":
        
        # username = request.POST.get('')
        username = request.POST['username']
        pass1 = request.POST['pass1']   
        user = authenticate(username=username, password=pass1) #after authentication, it will return a "none" or "not none" response.
                                                               #Then pass the authentication to user object
        
        if user is not None: #if he is registered on our platform
            login(request, user)
            fname = user.first_name #get users firstname for welcome msg
            return render(request, "home.html", {'fname': fname})
        
        
        if request.method != "POST":
            return HttpResponse("Method not Allowed")
            return redirect('signup')
        
            
        # Not registered send the error mesage below
        else:  
            messages.error(request,"Wrong details")
            return redirect('signin')    #direct the user to the signup page
    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('signup')

        