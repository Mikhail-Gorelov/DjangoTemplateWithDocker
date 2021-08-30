from django.conf import settings
from django.http import HttpRequest
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication

from .pagination import BasePageNumberPagination
from .serializers import SetTimeZoneSerializer
from .services import BlogMicroservice


class TemplateAPIView(APIView):
    """ Help to build CMS System using DRF, JWT and Cookies
        path('some-path/', TemplateAPIView.as_view(template_name='template.html'))
    """
    permission_classes = (AllowAny,)
    template_name = ''

    @method_decorator(name='create', decorator=swagger_auto_schema(auto_schema=None))
    def get(self, request, *args, **kwargs):
        return Response()


class SetUserTimeZone(GenericAPIView):
    serializer_class = SetTimeZoneSerializer
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = Response(serializer.data)
        response.set_cookie(
            key=getattr(settings, 'TIMEZONE_COOKIE_NAME', 'timezone'),
            value=serializer.data.get('timezone'),
            max_age=getattr(settings, 'TIMEZONE_COOKIE_AGE', 86400),
        )
        return response


class ArticleListView(GenericAPIView):
    pagination_class = BasePageNumberPagination

    def get(self, request, *args, **kwargs):
        url = '/posts/'
        service = BlogMicroservice(request=request, url=url)
        print(dir(request._request))
        print(request.get_host())
        return service.service_response()
