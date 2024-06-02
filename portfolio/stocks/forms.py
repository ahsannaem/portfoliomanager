from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import RiskProfile, StockHolding

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
    }))
    
    # RiskProfile fields
    category = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Category',
    }))
    age = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Age',
    }))
    emergency_funds = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Emergency Funds',
    }))
    investment_percentage = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Investment Percentage',
    }))
    high_reture_high_risk = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'High Return High Risk',
    }))
    expected_return_rate = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Expected Return Rate',
    }))
    keep_capital_safe = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Keep Capital Safe',
    }))
    annual_take_home_income = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Annual Take Home Income',
    }))
    worry_if_fall_percentage = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Worry If Fall Percentage',
    }))
    current_life_stage = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Current Life Stage',
    }))
    investment_familiarity = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Investment Familiarity',
    }))
    investment_length = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Investment Length',
    }))
    work_status = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Work Status',
    }))
    critical_situation_response = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Critical Situation Response',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 
                  'category', 'age', 'emergency_funds', 'investment_percentage', 
                  'high_reture_high_risk', 'expected_return_rate', 'keep_capital_safe', 
                  'annual_take_home_income', 'worry_if_fall_percentage', 'current_life_stage', 
                  'investment_familiarity', 'investment_length', 'work_status', 'critical_situation_response')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            risk_profile = RiskProfile(
                user=user,
                category=self.cleaned_data['category'],
                age=self.cleaned_data['age'],
                emergency_funds=self.cleaned_data['emergency_funds'],
                investment_percentage=self.cleaned_data['investment_percentage'],
                high_reture_high_risk=self.cleaned_data['high_reture_high_risk'],
                expected_return_rate=self.cleaned_data['expected_return_rate'],
                keep_capital_safe=self.cleaned_data['keep_capital_safe'],
                annual_take_home_income=self.cleaned_data['annual_take_home_income'],
                worry_if_fall_percentage=self.cleaned_data['worry_if_fall_percentage'],
                current_life_stage=self.cleaned_data['current_life_stage'],
                investment_familiarity=self.cleaned_data['investment_familiarity'],
                investment_length=self.cleaned_data['investment_length'],
                work_status=self.cleaned_data['work_status'],
                critical_situation_response=self.cleaned_data['critical_situation_response']
            )
            risk_profile.save()
        return user



class StockHoldingForm(forms.ModelForm):
    class Meta:
        model = StockHolding
        fields = ['company_symbol', 'company_name', 'sector', 'number_of_shares', 'investment_amount']
        widgets = {
            'company_symbol': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sector': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_shares': forms.NumberInput(attrs={'class': 'form-control'}),
            'investment_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }