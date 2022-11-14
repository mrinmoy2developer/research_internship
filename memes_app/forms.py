from django import forms
from . models import SubmitImage


Humour = (
    ('not_funny', 'Not Funny'),
    ('funny', 'Funny'),
    ('very_funny', 'Very Funny'),
    ('hilarious','Hilarious')
)

Sarcastic = (
    ('not_sarcastic', 'Not Sarcastic'),
    ('general', 'General'),
    ('twisted_meaning', 'Twisted Meaning'),
    ('very_twisted','Very Twisted')
)

Offensive = (
    ('not_offensive', 'Not Offensive'),
    ('slight', 'Slight'),
    ('very_offensive', 'Very Offensive'),
    ('hateful_offensive','Hateful Offensive')
)

Motivational = (
    ('motivational', 'Motivational'),
    ('not_motivational', 'Not Motivational')

)


classification_based_on = (
    ('image', 'Image'),
    ('text', 'Text'),
    ('image_and_text ','Image and text')

)



class imageform(forms.ModelForm):

    pic_humour = forms.ChoiceField(widget=forms.RadioSelect, choices=Humour)
    pic_sarcastic = forms.ChoiceField(widget=forms.RadioSelect, choices=Sarcastic)
    pic_offensive = forms.ChoiceField(widget=forms.RadioSelect, choices=Offensive)
    pic_motivational = forms.ChoiceField(widget=forms.RadioSelect, choices=Motivational)
    class Meta:
        model=SubmitImage
        fields=('pic_humour','pic_sarcastic','pic_offensive','pic_motivational','classification_based_on')
