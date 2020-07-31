from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
#home_page = None
def view_list(request):
    items = Item.objects.all()
    print("*****view_view_list**********")
    for a in items:
        print(a.text)

    print("*****view_view_list**********")
    return render(request, 'list.html', {'items':items})


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
        
        return redirect('/lists/the-only-list-in-the-world/')

    print("****view2****")
    print(request)
    print("****view2****")

    return render(request,'home.html')
