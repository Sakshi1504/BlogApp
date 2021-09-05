from django.utils.text import slugify

import string
import random

def generatestring(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res




def generate_slug(text):
    newslug=slugify(text)
    print("text is:::::::::::::", text)
    from Home.models import BlogModel
    if BlogModel.objects.filter(slug = newslug).exists():
        return generate_slug(text+generatestring(5))
    return newslug