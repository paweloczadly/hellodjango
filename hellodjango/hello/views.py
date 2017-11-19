from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.http import HttpResponse
from .models import Person
from redis.exceptions import ConnectionError
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def index(req):
    try:
        if 'persons' in cache:
            persons = cache.get('persons')
        else:
            persons = list(Person.objects.all())
            cache.set('persons', persons, timeout=CACHE_TTL)
        logger.info('Read from Redis')
    except ConnectionError:
        persons = list(Person.objects.all())
        logger.info('Read from Postgres')

    return HttpResponse(str(', '.join([p.name for p in persons])))

def create(req, person_name):
    p = Person(name = person_name)
    p.save()
    return HttpResponse("Created: " + person_name)

def delete(req, person_name):
    Person.objects.filter(name = person_name).delete()
    return HttpResponse("Deleted: " + person_name)
