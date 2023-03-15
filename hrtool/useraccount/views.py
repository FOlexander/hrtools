from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import PlotFile


# Create your views here.
@login_required
def user_page(request):
    plot = PlotFile.objects.get(plot_user=request.user)
    print(plot)
    return render(request, 'account.html')

