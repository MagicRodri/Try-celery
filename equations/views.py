from django.shortcuts import redirect, render
from django.views import View

from .forms import CalculationForm
from .models import Calculation
from .tasks import fibonacci_task

# Create your views here.


def fibonacci_list(request):
    
    return render(request,'equations/list.html',{'calculs' : Calculation.objects.all()})

def fibonacci_create(request):
    form = CalculationForm()
    if request.method == 'POST':
        """Process a form & start a Fibonacci calculation"""
        form = CalculationForm(request.POST)
        if form.is_valid():
            calculation = form.save()
        fibonacci_task.delay(calculation.id)

        return redirect('fibonacci-list')

    """Show a form to start a calculation"""
    return render(request, 'equations/input.html',{'form':form})