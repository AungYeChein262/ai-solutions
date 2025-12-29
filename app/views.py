from django.shortcuts import render, redirect
from .forms import EnquiryForm

def contact_view(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contact_success")
    else:
        form = EnquiryForm()

    return render(request, "website/contact.html", {"form": form})
