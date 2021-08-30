from microservice_request.services import MicroServiceConnect
from django.conf import settings


class BlogMicroservice(MicroServiceConnect):
    api_key = settings.BLOG_API_KEY
    service = settings.BLOG_API_URL
