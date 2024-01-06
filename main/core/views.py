from django.shortcuts import render, redirect
from .forms import CombinedForm

def register(request):
    if request.method == 'POST':
        form = CombinedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CombinedForm()
    return render(request, 'register.html', {'form': form})