from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST, require_http_methods
from .models import Card
import json

def home(request):
    data = Card.objects.all()
    context = {'data': data}
    return render(request, 'index.html', context=context)

def dashboard(request):
    data = Card.objects.filter(archived=False)
    return render(request, 'dashboard.html', {'data': data})

@require_POST
def delete_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    card.archived = True
    card.save()
    messages.info(request, 'Archived successfully')

    if request.is_ajax():
        return JsonResponse({'status': 'success'})
    return redirect('dashboard')

@require_POST
def archive_card(request):
    try:
        data = json.loads(request.body)
        card_id = data.get('card_id')
        card = get_object_or_404(Card, id=card_id)
        card.archived = True
        card.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

def restore_card(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    card.archived = False
    card.save()
    messages.info(request, 'Restored successfully')
    return redirect('archives')

def no_page(request):
    return render(request, 'no_page.html')

def archives(request):
    archived_cards = Card.objects.filter(archived=True)
    return render(request, 'archieves.html', {'archived_cards': archived_cards})
