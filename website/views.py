from django.shortcuts import render, redirect
from .forms import EnquiryForm
from django.shortcuts import render

def contact_view(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()   # 🔥 THIS LINE SAVES TO DATABASE
            return redirect("contact_success")
    else:
        form = EnquiryForm()

    return render(request, "website/contact.html", {"form": form})


def contact_success(request):
    return render(request, "website/contact_success.html")

def contact(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_success")
    else:
        form = EnquiryForm()

    return render(request, "website/contact.html", {"form": form})


def contact_success(request):
    return render(request, "website/contact_success.html")

def home(request):
    return render(request, "website/home.html")


def solutions(request):
    return render(request, "website/solutions.html")

def articles(request):
    return render(request, "website/articles.html")

def events(request):
    return render(request, "website/events.html")

def article_custom_software_trends(request):
    return render(
        request,
        "website/articles/custom_software_development_trends.html"
    )

def feedback(request):
    return render(request, "website/feedback.html")

def contact_success(request):
    return render(request, "website/contact_success.html")

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Feedback

def feedback_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        job_title = request.POST.get("job_title")
        company = request.POST.get("company")
        rating = request.POST.get("rating")
        message = request.POST.get("message")

        if not all([name, job_title, company, rating, message]):
            messages.error(request, "All fields are required.")
            return redirect("feedback")

        Feedback.objects.create(
            name=name,
            job_title=job_title,
            company=company,
            rating=int(rating),
            message=message,
        )

        messages.success(request, "Feedback submitted successfully.")
        return redirect("feedback")

    return render(request, "website/feedback.html")

from .models import Article

def articles(request):
    articles = Article.objects.order_by("-created_at")
    return render(request, "website/articles.html", {
        "articles": articles
    })



from django.shortcuts import render, get_object_or_404
from .models import Article

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, "website/article_detail.html", {
        "article": article
    })

def solution_custom_software(request):
    return render(request, "website/solutions/custom_software.html")
