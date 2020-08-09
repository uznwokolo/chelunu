from django import forms




class Atm_Pan_Date_SearchForm(forms.Form):
    atmId = forms.CharField(label='ATM ID:', max_length=4)
    cardPan = forms.CharField(label='Card PAN:', max_length=4)
    #trxnAmount = forms.IntegerField(label='Amount:')
    trxnDate = forms.DateField(label='Date:')

    
class Atm_Trxn_SearchForm(forms.Form):
    atmId = forms.CharField(label='ATM ID:', max_length=4)


class Date_SearchForm(forms.Form):
	trxnDate = forms.DateField(label='Date:')