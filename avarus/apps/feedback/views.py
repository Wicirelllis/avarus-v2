from apps.feedback.forms import FeedbackForm
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views import generic


class FeedbackFormView(generic.View):
    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            if settings.FEEDBACK_SEND_EMAIL:
                send_mail(
                    f'Feedback from {feedback.name}',
                    f'{feedback.name} (email: {feedback.email}) has left following feedback on the site\n\n{feedback.feedback}',
                    settings.EMAIL_HOST_USER,
                    settings.FEEDBACK_EMAIL_RECIPIENTS
                )
        return redirect('feedback-done')

    def get(self, request):
        return redirect('/')
