from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
    ('text', 'Text'),
    ('image', 'Image'),
    ('image_and_text ','Image and text')

)


class SubmitImage(models.Model):
    pic_humour=models.CharField(choices=Humour,null=False,max_length=20)
    pic_sarcastic=models.CharField(choices=Sarcastic,null=False,max_length=20)
    pic_offensive=models.CharField(choices=Offensive,null=False,max_length=20)
    pic_motivational=models.CharField(choices=Motivational,null=False,max_length=20)
    classification_based_on=models.CharField(choices=classification_based_on,null=False,max_length=20)
    pic_overall=models.CharField(max_length=20)
    image=models.URLField(max_length=255)

    def __str__(self):
        return str(self.image)


class UserImage(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    annoted_image=models.IntegerField()

    def __str__(self):
        return str(self.userid)
