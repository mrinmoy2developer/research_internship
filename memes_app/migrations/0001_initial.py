# Generated by Django 2.1.7 on 2019-05-16 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_humour', models.CharField(choices=[('not_funny', 'Not Funny'), ('funny', 'Funny'), ('very_funny', 'Very Funny'), ('hilarious', 'Hilarious')], max_length=20)),
                ('pic_sarcastic', models.CharField(choices=[('not_sarcastic', 'Not Sarcastic'), ('general', 'General'), ('twisted_meaning', 'Twisted Meaning'), ('very_twisted', 'Very Twisted')], max_length=20)),
                ('pic_offensive', models.CharField(choices=[('not_offensive', 'Not Offensive'), ('slight', 'Slight'), ('very_offensive', 'Very Offensive'), ('hateful_offensive', 'Hateful Offensive')], max_length=20)),
                ('pic_motivational', models.CharField(choices=[('motivational', 'Motivational'), ('not_motivational', 'Not Motivational')], max_length=20)),
                ('classification_based_on', models.CharField(choices=[('text', 'Text'), ('image', 'Image'), ('image_and_text ', 'Image and text')], max_length=20)),
                ('pic_overall', models.CharField(max_length=20)),
                ('image', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=100, unique=True)),
                ('annoted_image', models.IntegerField()),
            ],
        ),
    ]
