from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
from django.http import HttpResponse

def home_view(request):
    return HttpResponse('Welcome to the home page!')

def feedback_form_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
        # redirectinam i feedback_list kai pasubmitinam ir forma
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})
    #kitaip  einam i tuscia forma

def feedback_list_view(request):
    atsiliepimai = Feedback.objects.order_by('-sukurta')
    return render(request, 'feedback_list.html', {'atsiliepimai': atsiliepimai})
