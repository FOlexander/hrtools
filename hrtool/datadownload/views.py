from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from openpyxl import load_workbook
import pandas as pd
import matplotlib.pyplot as plt
import io


# Create your views here.
def download_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data = pd.read_excel(request.FILES['file'])
            return HttpResponseRedirect(reverse('handle', args=data.all()))
    else:
        form = UploadFileForm()

    return render(request, 'dl.html', {'form': form})
