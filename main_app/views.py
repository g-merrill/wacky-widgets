from django.shortcuts import render, redirect
from .models import Widget

# Create your views here.
def home(request):
    if request.method == 'POST':
        Widget.objects.create(description=request.POST['description'], quantity=request.POST['quantity'])
        return redirect('home')
    widgets = Widget.objects.all()
    total = 0
    for widget in widgets:
        total += widget.quantity
    return render(request, 'home.html', { 'widgets': widgets, 'total': total })

def delete_wdgt(request, wdgt_id):
    Widget.objects.get(id=wdgt_id).delete()
    return redirect('home')