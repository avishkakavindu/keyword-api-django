from django.core.files.storage import default_storage, FileSystemStorage
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework import permissions
from keyword_extraction_api.keyword_extraction import keyword_extraction
from keyword_extraction_api.keyword_extraction import pdf_to_text
from rest_framework.response import Response
from rest_framework import status
from api.models import *
from api.serializers import UserSerializer


class KeywordExtractionAPIView(APIView):
    """
        Responsible for keyword extracting process
    """

    def post(self, request, *args, **kwargs):
        pdf_file = request.FILES['pdf_file']
        fs = FileSystemStorage()
        filename = fs.save(pdf_file.name, pdf_file)
        file_url = fs.url(filename)[1:]

        print('\n\n\n', file_url)

        links = keyword_extraction.get_link_sugessions(
            pdf_to_text.extract_text(file_url)
        )

        context = {
            'links': links
        }

        return Response(context, status=status.HTTP_200_OK)


class AssignmentScheduleAPIView(APIView):
    """
        Handles Assignment scheduling
    """

    authentication_classes = [JWTTokenUserAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # user = request.user
        user = User.objects.get(id=1)
        serializer = UserSerializer(user)

        context = {
            'assignment_details': serializer.data
        }

        return Response(context, status=status.HTTP_200_OK)

