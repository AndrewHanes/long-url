from datetime import datetime
import random
from string import ascii_letters
from rest_framework import views
from rest_framework.response import Response
from long_url_app import models

__author__ = 'ahanes'


class ResolverView(views.APIView):
    def get(self, request, ident=None):
        resps = models.Resolver.objects.filter(ident=ident)
        data = models.ResolverSerializer(resps[0])
        return Response(data.data)


def gen_rand_str(length=2000):
    return "".join([random.choice(ascii_letters) for x in range(length)])


class ResolverCreate(views.APIView):
    def get(self, request):
        ip = get_client_ip(request)
        if len(models.Resolver.objects.filter(created_ip=ip)) > 100:
            return Response()
        has = models.Resolver.objects.filter(to=request.query_params['to'])
        if len(has) > 0:
            return Response(models.ResolverSerializer(has[0]).data)
        else:
            ident_length = 2000 - len(request.query_params['to'])
            if ident_length < 100:
                raise Exception("Url is too long!")
            data = dict(ident=gen_rand_str(length=ident_length),
                        to=request.query_params['to'],
                        created_ip=ip,
                        last_accessed=datetime.now())
            new_res = models.Resolver(**data)
            new_res.save()
            return Response(models.ResolverSerializer(new_res).data)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip