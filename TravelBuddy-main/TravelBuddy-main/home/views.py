from django.shortcuts import render, HttpResponse
import databaseOp as op
# Create your views here.
def index(request):
    return render(request, 'index.html')


data = {
        "packages" : [
        {"PID": 1001, 'From_City': 'Pune', 'From_State' : 'Maharashtra' , 'Dest' : 'New Delhi', 'NoOfDays': 5, 'Season': 'Winter', 'Rating': 4.1, 'Budget_Type' : 1},
        {"PID": 1004, 'From_City': 'New Delhi', 'From_State' : 'New Delhi' , 'Dest' : 'Jammu and Kashmir', 'NoOfDays': 8, 'Season': 'Summer', 'Rating': 4.5, 'Budget_Type' : 3}
        ]
    }
def packages(request):
    res = op.results
    # name = request.
    # print(name)
    
    return render(request, 'Packages.html', data)

def packageDetails(request, pkid):
    print(pkid)
    for i in data['packages']:
        print(i['PID'])
        if int(i["PID"]) == int(pkid) :
            d = i
    return render(request, 'packageDetails.html', d)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

