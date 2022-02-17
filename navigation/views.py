from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse


from .models import Contribute
from .forms import ContributeForm


# Create your views here.


@login_required(login_url="/login/")
def contribute(request):
    msg = ""
    if request.method == 'POST':
        comment_form = ContributeForm(request.POST,instance=request.user)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            data["user"] = request.user
            Contribute.objects.create(**data)
            msg = "The form has been successfully submitted"
        else:
            print("invalid")
            msg = "Invalid Form"
            form = ContributeForm()

    form = ContributeForm()
    return render(request, 'contribute.html', locals())



