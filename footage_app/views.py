from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from footage_app.forms import Atm_Pan_Date_SearchForm as apdForm
from footage_app.forms import Atm_Trxn_SearchForm as atrForm
from footage_app.forms import Date_SearchForm as dateForm
from footage_app.models import Transaction, Terminal

# Create your views here.

def apdSearchTrxn(request):
    if request.method == "POST":
        form = apdForm(request.POST)    #Atm_Pan_Date_SearchForm
        if form.is_valid():
            atmid = form.cleaned_data['atmId']
            pan = form.cleaned_data['cardPan']
            date = form.cleaned_data['trxnDate']
            
            # sql query to find all transactions that match terminal id, card pan and date
            allTrxns = Transaction.objects.filter(terminal_id__exact=atmid,
            card_pan__exact=pan, timestamp__contains=date)
            
            # dictionary for results
            userquery = {
                "trxnlist": allTrxns,
            }

            template = loader.get_template('app/search.html')
            
            return HttpResponse(template.render(userquery, request))
    else:
        form = apdForm()
    return render(request, "app/search.html", {"form": form})


def atmTransactionsById(request):
    if request.method == "POST":
        form2 = atrForm(request.POST)
        if form2.is_valid():
            atmid = form2.cleaned_data['atmId']
            
            # check if the terminal id is valid before running other queries
            try:
                inputAtm = Terminal.objects.get(terminal_id__exact=atmid)
                trxnsByAtm = Transaction.objects.filter(terminal_id__exact=atmid)
                userquery = {
                    "atmtrxns": trxnsByAtm,
                    "theAtm": inputAtm,
                }
            except Terminal.DoesNotExist:
                userquery = {
                    "theAtm": "Terminal not found",
                }
            
            # are we using a new form or the old one??
            template = loader.get_template('app/atmtrxns.html')
            
            return HttpResponse(template.render(userquery, request))
    else:
        form2 = atrForm()
    return render(request, "app/atmtrxns.html", {"form": form2})


def transactionsByDate(request):
    if request.method =="POST":
        form3 = dateForm(request.POST)
        if form3.is_valid():
            trxnDate = form3.cleaned_data['trxnDate']
            trxnsByDate = Transaction.objects.filter(timestamp__contains=trxnDate)
            userquery = {
                "trxnsByDate": trxnsByDate,
                "theDate": trxnDate,
            }

            template = loader.get_template('app/datetrxns.html')
            
            return HttpResponse(template.render(userquery, request))
    else:
        form3 = dateForm()
    return render(request, "app/datetrxns.html", {"form": form3})


def results(request):
    return render(request, "app/results.html")