from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import StockHolding, Portfolio
from .forms import CustomUserCreationForm, StockHoldingForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a Portfolio for the new user
            Portfolio.objects.create(user=user, name=f"{user.username}'s Portfolio")

            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
        
        


@login_required
def home(request):
    # Retrieve all StockHolding objects

 stockholdings = StockHolding.objects.filter(portfolio__user=request.user)
 return render(request, 'home.html', {'stockholdings': stockholdings})

@login_required
def add_stock(request):
    try:
        portfolio = Portfolio.objects.get(user=request.user)
    except Portfolio.DoesNotExist:
        # Create a Portfolio if it doesn't exist
        portfolio = Portfolio.objects.create(user=request.user, name=f"{request.user.username}'s Portfolio")

    if request.method == 'POST':
        form = StockHoldingForm(request.POST)
        if form.is_valid():
            stockholding = form.save(commit=False)
            # Ensure the stockholding is associated with the current user's portfolio
            stockholding.portfolio = Portfolio.objects.get(user=request.user)
            stockholding.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = StockHoldingForm()
    return render(request, 'add_stock.html', {'form': form})