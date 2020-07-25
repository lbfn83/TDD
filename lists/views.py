from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
#home_page = None
def home_page(request):
    #pass
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    #if request.method == 'POST':
    #    print(request.POST)
    #    return HttpResponse(request.POST['item_text'])
    
    #print( request.read())
    
    if request.method =='POST':
        print("*****view**********")
        print(request)
       
        Item.objects.create(text=request.POST['item_text'])
        
        print(Item)
        print("*****view**********")
        
        return redirect('/')

    items = Item.objects.all()

    return render(request,'home.html', {'items':items})
