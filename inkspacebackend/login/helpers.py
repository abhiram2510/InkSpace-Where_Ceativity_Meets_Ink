from django.utils.text import slugify
import string
import random

def generate_random_slug(N):
    result = ''.join(random.choices(string.ascii_uppercase + string.digits,k=N))
    return result


def generate_slug(text):
    new_slug = slugify(text)
    from login.models import BlogModel
    if BlogModel.objects.filter(slug = new_slug).first():
         return generate_slug(text + generate_random_slug(5))
    return new_slug

