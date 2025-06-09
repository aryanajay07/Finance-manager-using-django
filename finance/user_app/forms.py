from django import forms
from .models import Account, Expense

class ExpenseForm(forms.ModelForm):
    long_term = forms.BooleanField(required=False, label='Is this a long-term expense?')
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'date', 'long_term', 'interest_rate', 'end_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'long_term': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'interest_rate': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        } 

        def clean(self):
            cleaned_data = super().clean()
            long_term = cleaned_data.get('long_term')
            start_date = cleaned_data.get('date')
            if long_term:
                interest_rate = cleaned_data.get('interest_rate')
                end_date = cleaned_data.get('end_date')
                amount = cleaned_data.get('amount')
                cleaned_data['long_term'] = True
            else:
                cleaned_data['end_date'] = None
                cleaned_data['interest_rate'] = 0.0
            return cleaned_data
        
