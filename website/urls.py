from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("contact/", views.contact_view, name="contact"),
    path("contact/success/", views.contact_success, name="contact_success"),

    path("solutions/", views.solutions, name="solutions"),
    path("articles/", views.articles, name="articles"),
    path("events/", views.events, name="events"),

    path(
        "articles/custom-software-development-trends/",
        views.article_custom_software_trends,
        name="article_custom_software_trends"
    ),

    # ✅ ONLY ONE feedback URL
    path("feedback/", views.feedback_view, name="feedback"),
    path("articles/<slug:slug>/", views.article_detail, name="article_detail"),
    path("solutions/custom-software-development/",views.solution_custom_software, name="solution_custom_software"),

]
