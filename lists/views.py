from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#home_page = None
def home_page(request):
    #pass
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    #if request.method == 'POST':
    #    print(request.POST)
    #    return HttpResponse(request.POST['item_text'])
    
    print( request.read())
    return render(request,'home.html',{
        'new_item_text':request.POST.get('item_text',''),
        })
