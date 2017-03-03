from django.forms import ModelForm

from .. import models


class Registration(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        instance = kwargs.get('instance')
        if instance:
            self.fields['documents'].queryset = instance.member.documents.order_by('created_date')
