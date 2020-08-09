from django.shortcuts import render
from django.http import HttpResponse


from footage_app.models import Branch, Terminal, Transaction
# Create your views here.


def home(request):
	# assign branch, terminal and transaction counts
	brn_count = Branch.objects.count()
	ter_count = Terminal.objects.count()
	txn_count = Transaction.objects.count()

	# assign success and failed counts
	success = Transaction.objects.filter(trxn_success__exact=1).count()
	failed = Transaction.objects.filter(trxn_success__exact=0).count()

	labels = ["Successful","Failed"]  # labels array
	data = [success, failed]          # data array
	
	context = {
		'brn_count': brn_count,
		'ter_count': ter_count,
		'txn_count': txn_count,
		'labels': labels,
		'data': data,
	}
	return render(request, "website/home.html", context=context)


def progress(request):
	return render(request, "website/progress.html")