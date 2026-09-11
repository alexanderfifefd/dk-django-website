from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def notify_onboarding_inbox(*, flow_label: str, template_name: str, context: dict) -> None:
    body = render_to_string(template_name, context)
    subject = f"[{flow_label}] {context['email']}"
    send_mail(
        subject=subject,
        message=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.ONBOARDING_INBOX],
        fail_silently=False,
    )
