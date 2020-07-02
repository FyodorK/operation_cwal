from django import forms


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter something")
    text = forms.CharField(widget=forms.Textarea())

    def clean(self):
        all_clean_data = super().clean()
        print(all_clean_data)
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("email check failed")

    """botcatcher = forms.CharField(required=False,
                             widget=forms.HiddenInput,
                             validators=[validators.MaxLengthValidator(0)])

    def clean_botcatcher(self):
    botcatcher = self.cleaned_data['botcatcher']
    if len(botcatcher) > 0:
        raise forms.ValidationError("I've got a bot")
    return botcatcher"""