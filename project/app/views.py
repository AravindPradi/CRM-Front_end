from django.shortcuts import render, get_object_or_404, redirect
from . models import Card
from django.contrib import messages


def home(request):
    data = Card.objects.all()
    context = {'data':data}
    return render(request,'index.html',context=context)

def dashboard(request):
    data = Card.objects.all()
    
    return render(request, 'dashboard.html', {'data':data})

def delete_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    card.archived = True
    card.save()
    messages.info(request,'Archieved successfully')
    return redirect('dashboard')

def restore_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    card.archived = False
    card.save()
    messages.info(request,'Restored successfully')
    return redirect('archieves')


def no_page(request):
    return render(request,'no_page.html')



def archieves(request):
    archived_cards = Card.objects.filter(archived=True)
    return render(request,'archieves.html',{'archived_cards': archived_cards,})
