from django.db import models, migrations
from django_mysql.models import ListCharField
import datetime


class Migration(migrations.Migration):
    dependencies = [ ('LectioEx', '0003_remove_choice_question'), ]
    operations = [
        migrations.AddField(
            model_name='Badge',
            name='Card',
            field=models.ForeignKey(default=1, to='LectioEx.Card', on_delete=models.CASCADE), preserve_default=False),
    ]
    

class Badge(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    upload_date = models.DateTimeField('uploade date', null=True)
    image = models.ImageField(upload_to='badges', null=True)

    def __str__(self):
        return self.name
    

class Card(models.Model):
    card_class_txt = models.CharField(max_length=200)
    card_niveau = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    badges = (
        models.ForeignKey(Badge, on_delete=models.CASCADE, null=True)
    )

    def __str__(self):
        return self.card_class_txt
    