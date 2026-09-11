from django import forms


from django.conf import settings

class FollowForm(forms.Form):
    label_suffix = ""

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@example.com",
                "autocomplete": "email",
            }
        ),
    )
    newsletter = forms.BooleanField(
        required=False,
        label="Yes please — keep me updated on Datakollektivet",
    )

    if settings.DEBUG:
        send_email = forms.BooleanField(
            required=False,
            label="Send notification email (uncheck to suppress email)",
            initial=True,
        )


class MemberForm(forms.Form):
    label_suffix = ""

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@example.com",
                "autocomplete": "email",
            }
        ),
    )
    newsletter = forms.BooleanField(
        required=False,
        label="Yes please — keep me updated on Datakollektivet",
    )


class BuildForm(forms.Form):
    label_suffix = ""

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@example.com",
                "autocomplete": "email",
            }
        ),
    )
    interest = forms.CharField(
        label="Where could you contribute?",
        min_length=10,
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                "rows": 4,
                "placeholder": "Moderation, specific systems, initiatives, skills you bring…",
            }
        ),
        error_messages={
            "min_length": "Tell us a little about where you would like to contribute.",
        },
    )

    def clean_interest(self):
        value = self.cleaned_data["interest"].strip()
        if not value:
            raise forms.ValidationError(
                "Tell us a little about where you would like to contribute."
            )
        return value
