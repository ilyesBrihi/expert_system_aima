from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("faq/", views.FAQView.as_view(), name="faq"),
    path("result/", views.ResultView.as_view(), name="result"),
]

urlpatterns += staticfiles_urlpatterns()