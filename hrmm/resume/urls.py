from django.urls import include, path
from rest_framework import routers
from .views import ResumeViewSet,ResumtUploadView

router = routers.DefaultRouter()
router.register(r"", ResumeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("resumes", include(router.urls)),
    path("upload/", ResumtUploadView.as_view()),

]
