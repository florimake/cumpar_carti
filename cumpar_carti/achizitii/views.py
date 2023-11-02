from django.shortcuts import render
from .models import *

# Create your views here.

############################################################### index ##################################################################
def view_index(request):
    context = {"paragrafe": Paragraf.objects.all(), "contacte": Contact.objects.all()}
    return render(request, "index.html", context)
############################################################### index ##################################################################
