from django.urls import path, include
from api.api_views import *


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('keywords-extraction/', KeywordExtractionAPIView.as_view(), name='keyword_extraction'),
    path('assignment-scheddule/', AssignmentScheduleAPIView.as_view(), name='ass-sch'),
]
