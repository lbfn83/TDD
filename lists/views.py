from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
#home_page = None

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    
    Item.objects.create(text = request.POST['item_text'], list = list_)
    return redirect(f'/lists/{list_.id}/')

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id) 
    
    return render(request, 'list.html', {'list':list_})


def home_page(request):
    #pass
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    #if request.method == 'POST':
    #    print(request.POST)
    #    return HttpResponse(request.POST['item_text'])
    
    #print( request.read())
    

    print("****view2****")
    print(request)
    print("****view2****")

    return render(request,'home.html')
