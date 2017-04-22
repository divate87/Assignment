import csv
from django.shortcuts import render, redirect

def index(request):
        if request.method == 'POST':
                    csvfile = request.FILES['csvfile']
                    reader       = csv.reader( csvfile )
                    return render(request, "index.html", {"reader":reader})
        else:
                    return render(request, "index.html", {})
