# accounts/views.py

from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .models import Subject, Question


User = get_user_model()  # Use the custom user model

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)  # Use SignupForm
        if form.is_valid():
            # Create a new user
            user = form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']

            # Check if the input is an email
            if '@' in username_or_email:
                try:
                    user = User.objects.get(email=username_or_email)
                    username = user.username
                except User.DoesNotExist:
                    user = None
            else:
                username = username_or_email
            
            # Authenticate the user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Change this to your dashboard URL
            else:
                form.add_error(None, "Invalid username/email or password.")
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'accounts/dashboard.html', {'user': user})  # Create a template for this

@login_required
def profile(request):
    # Assuming that test history will be updated in the future
    
    test_history = []  # Placeholder for future test history data
    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'test_history': test_history
    })
    

@login_required    
def practice_questions(request):
    return render(request, 'accounts/practice_questions.html')

@login_required    
def mock_test(request):
    return render(request, 'accounts/mock_test.html')

# views.py


@login_required    
def subjects_list(request):
    subjects = Subject.objects.all()
    return render(request, 'accounts/subjects_list.html', {'subjects': subjects})

@login_required    
def subject_questions(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    questions = Question.objects.filter(subject=subject)
    return render(request, 'accounts/subject_questions.html', {'subject': subject, 'questions': questions})
