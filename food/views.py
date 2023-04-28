from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import items
from django.template import loader 
from .forms import itemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
#This is a request handler (basically)

#DB data variables
#This cant be outside! If so, the lists wont refresh 
# because it will be pulling the list 
# from the creation of the project


def index(request):
    item_list = items.objects.all()
    context = {
        'item_list':item_list,
    }
    return render(request,'food/index.html',context)


#Example of class based views. Not in used right now. 
# Need to add the class to url.py with '.as_view()'
class indexClassView(ListView):
    model=items
    template_name='food/index.html'
    context_object_name='item_list'


def item(request):
    return HttpResponse('This is an item')

def tags(request):
    item_list = items.objects.all()
    template = loader.get_template('food/index.html')
    context={
        'item_list':item_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request,item_id):
    item= items.objects.get(pk=item_id)
    context={
        'item':item,
    }
    return render(request,'food/details.html',context)

class itemsDetailView(DetailView):
    model = items
    template_name = "food/details.html"


def create_item(request):
    form = itemForm(request.POST or None)

    if form.is_valid():
        form.instance.user_name=request.user #This line adds the item with the user that created it
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'form':form})


def update_item(request,item_id):
    item= items.objects.get(pk=item_id)

    form = itemForm(request.POST or None,instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'item':item,'form':form})


def delete_item(request,item_id):
    item= items.objects.get(pk=item_id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request,'food/item-delete.html',{'item':item})