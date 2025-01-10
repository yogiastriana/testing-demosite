from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import time

# Create your views here.
@login_required(login_url='/login/')
def rebalancing_dashboard(request):
    is_f1_run_exist = 1 if 'f1_runs' in request.session and request.session['f1_runs'] else 0

    context = {
        'page_title': 'Welcome to the template home page',
        'is_f1_run_exist': is_f1_run_exist
    }
    

    return render(request, 'rebalancing/dashboard.html', context)


@login_required(login_url='/login/')
def run_rebalancing_f1_view(request):

    time.sleep(2)

    context = {

    }

    return render(request, 'f1/summary_result.html', context)


@login_required(login_url='/login/')
def current_f1_result_view(request):

    context = {

    }

    return render(request, 'f1/f1_output.html', context)