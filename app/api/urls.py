from django.urls import path
from app.api import views

################################################SWAGGER#####################################################################
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Todo App",
        default_version='v1',
        description="Users doing something",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

#################################################################################################################################

urlpatterns = [
    path('todos/', views.TodosList.as_view(), name='todos'),
    path('todos/<int:pk>/', views.TodosDetails.as_view(), name='todos_details'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]
