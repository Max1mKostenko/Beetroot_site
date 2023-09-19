from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by("-date")
    return render(request, "news/news_home.html", {"news": news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = "news/details_view.html"
    context_object_name = "article"


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = "news/update_article.html"

    form_class = ArticlesForm
    # fields = ["title", "anons", "full_text", "date"]


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = "/news"
    template_name = "news/delete_article.html"


def create_article(request):
    error = ""
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("news_home")
        else:
            error = "Form didn't correct"
    form = ArticlesForm()

    data = {
        "form": form,
        "error": error
    }
    return render(request, "news/create_article.html", data)
