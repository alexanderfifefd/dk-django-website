from django.conf import settings
from django.shortcuts import render

from .forms import BuildForm, FollowForm, MemberForm
from .mail import notify_onboarding_inbox


def home(request):
    return render(request, "public/home.html")


def join(request):
    return render(request, "public/join/index.html")


def join_follow(request):
    submitted = False
    send_failed = False
    submitted_email = ""
    form = FollowForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        try:
            notify_onboarding_inbox(
                flow_label="Follow us",
                template_name="public/emails/join/follow.txt",
                context={
                    **form.cleaned_data,
                    "matrix_contact_url": settings.MATRIX_CONTACT_URL,
                },
            )
        except Exception:
            send_failed = True
        else:
            submitted = True
            submitted_email = form.cleaned_data["email"]

    return render(
        request,
        "public/join/follow.html",
        {
            "form": form,
            "submitted": submitted,
            "send_failed": send_failed,
            "submitted_email": submitted_email,
        },
    )


def join_member(request):
    submitted = False
    send_failed = False
    submitted_email = ""
    form = MemberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        try:
            notify_onboarding_inbox(
                flow_label="Become a member",
                template_name="public/emails/join/member.txt",
                context={
                    **form.cleaned_data,
                    "payment": settings.MEMBER_PAYMENT,
                },
            )
        except Exception:
            send_failed = True
        else:
            submitted = True
            submitted_email = form.cleaned_data["email"]

    return render(
        request,
        "public/join/member.html",
        {
            "form": form,
            "submitted": submitted,
            "send_failed": send_failed,
            "submitted_email": submitted_email,
            "payment": settings.MEMBER_PAYMENT,
        },
    )


def join_build(request):
    submitted = False
    send_failed = False
    submitted_email = ""
    form = BuildForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        try:
            notify_onboarding_inbox(
                flow_label="Build with us",
                template_name="public/emails/join/build.txt",
                context={
                    **form.cleaned_data,
                    "matrix_contact_url": settings.MATRIX_CONTACT_URL,
                },
            )
        except Exception:
            send_failed = True
        else:
            submitted = True
            submitted_email = form.cleaned_data["email"]

    return render(
        request,
        "public/join/build.html",
        {
            "form": form,
            "submitted": submitted,
            "send_failed": send_failed,
            "submitted_email": submitted_email,
        },
    )
