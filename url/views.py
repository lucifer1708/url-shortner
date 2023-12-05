from django.shortcuts import redirect, render

from .forms import UrlForm
from .models import Url

# Create your views here.


def home(request):
    form = UrlForm()
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data["link"]
            if ("http://" not in link) and ("https://" not in link):
                link = "http://" + link
            alias = form.cleaned_data["alias"]
            if alias != "admin":
                new_url = Url(link=link, alias=alias)
                new_url.save()
                return render(
                    request,
                    "show_url.html",
                    {"alias": alias, "form": form, "link": link},
                )
    return render(request, "index.html", {"form": form})


def redirecturl(request, pk):
    url = Url.objects.get(alias=pk)
    return redirect(url.link)
