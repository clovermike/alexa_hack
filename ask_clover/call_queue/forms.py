from django.forms import ModelForm

from call_queue.models import Call


class CallForm(ModelForm):

    class Meta:
        model = Call
        fields = ['personid', 'reason']
