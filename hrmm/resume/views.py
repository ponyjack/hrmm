from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ResumeSerializer
from .models import Resume
import rest_framework_filters as filters
from rest_framework_filters import backends

from rest_framework.pagination import PageNumberPagination
from url_filter.integrations.drf import DjangoFilterBackend

from .data import templteresume
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

import logging
import uuid
import tempfile
from django.http.response import JsonResponse



class ResumeFilter(filters.FilterSet):
    class Meta:
        model = Resume
        fields = "__all__"


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 100


class ResumeViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """

    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    # filter_class = ResumeFilter
    filter_backends = [DjangoFilterBackend]
    filter_fields = "__all__"
    pagination_class = StandardResultsSetPagination




class ResumtUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        logging.warning(request.FILES)
        for k, v in  request.FILES.items():
            tmpf = tempfile.NamedTemporaryFile()
            logging.warn(f"tmp file name {tmpf.name}")
            for chunk in v.chunks():
                tmpf.write(chunk)


        templteresume['name'] = uuid.uuid4().hex[:8]
        serializer = ResumeSerializer(data=templteresume)
        serializer.is_valid()
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)
