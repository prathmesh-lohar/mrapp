from django.contrib import admin
from django.urls import path, include
from django.views import View
from api import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'testing', views.TestingViewSet)

urlpatterns = [
    path('testing',views.testingClassBassedView.as_view()),
    path('testing/<int:id>',views.testingClassBassedView.as_view()),

    path('mruser',views.mr_userClassBassedView.as_view()),
    path('mruser/<int:id>',views.mr_userClassBassedView.as_view()),

    path('druser',views.dr_userClassBassedView.as_view()),
    path('druser/<int:id>',views.dr_userClassBassedView.as_view()),

    path('visit',views.visitClassBassedView.as_view()),
    path('visit/<int:id>',views.visitClassBassedView.as_view()),


    path('mrlogin/<str:user_name>',views.mrloginClassBassedView.as_view()),

    # path('',include(router.urls)),

    # path('visit', views.visit_detail, name="visit"),
    # path('visit_create', views.visit_create, name="visit_create"),
    # path('testing_api', views.testing_detail, name="testing_api"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 