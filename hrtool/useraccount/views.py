from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import PlotFile, ControlPlotFile


# Create your views here.
@login_required
def user_page(request):
    survplot = PlotFile.objects.get(plot_user=request.user)
    contrplot = ControlPlotFile.objects.get(plot_user=request.user)
    data = {'survplot':survplot.plot, 'contrplot':contrplot.plot}
    return render(request, 'account.html', data)

