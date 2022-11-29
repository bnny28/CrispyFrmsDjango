from django.shortcuts import render
from .forms import CandidateForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Успешно!")
            return HttpResponseRedirect('/')
        else:
            context = {"form": form}
            return render(request, "candidates/home.html", context)
    else:
        form = CandidateForm()
        context = {"form": form}
        return render(request, "candidates/home.html", context)
