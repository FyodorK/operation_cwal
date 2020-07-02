
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')
import django
django.setup()

from app_one.models import Topic, WebPage, AccessRecord
from faker import Faker
import random


fake_gen = Faker()

topic = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return t


def populate(n=5):

    for entry in range(n):
        top = add_topic()
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(date=fake_date, name=webpg)[0]


if __name__ == '__main__':
    populate(20)
    print("Done!")
