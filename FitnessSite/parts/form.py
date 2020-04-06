from django import forms


class PartForm(forms.Form):
    subject = forms.CharField(max_length=100)
    msg = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    part_txt = forms.CharField(label="部位代號", max_length="10")
    part_name = forms.CharField(label="部位名稱", max_length="10")
