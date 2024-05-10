from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('feedback-form', views.FeedbackFormView.as_view(), name='feedback-form'),
    path('feedback-complete', TemplateView.as_view(template_name='feedback/feedback_done.html'), name='feedback-done'),
]
