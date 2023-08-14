
from django.urls import path, include

from .views import html_404, indexPage, mainPage

# rest_framework
from rest_framework import routers
from App import views


router = routers.DefaultRouter()

router.register(r'user', views.UserViewset, basename='api_user')
router.register(r'roles', views.RoleViewSet, basename='api_roles')

router.register(r'catalog/vehicle_model', views.VehicleModelViewSet, basename='api_vehicle_model')
router.register(r'catalog/engine_model', views.EngineModelViewSet, basename='api_engine_model')
router.register(r'catalog/transmission_model', views.TransmissionModelViewSet, basename='api_transmission_model')
router.register(r'catalog/drive_axle_model', views.DriveAxleModelViewSet, basename='api_drive_axle_model')
router.register(r'catalog/steering_axle_model', views.SteeringAxleModelViewSet, basename='api_steering_axle_model')
router.register(r'catalog/maintenance_type', views.MaintenanceTypeViewSet, basename='api_maintenance_type')
router.register(r'catalog/malfunction_overview', views.MalfunctionOverviewViewSet, basename='api_malfunction_overview')
router.register(r'catalog/repairing_method', views.RepairingMethodViewSet, basename='api_repairing_method')
router.register(r'catalog/maintenance_company', views.MaintenanceCompanyViewSet, basename='api_maintenance_company')
router.register(r'catalog/service_company', views.ServiceCompanyViewSet, basename='api_service_company')
router.register(r'catalog/client', views.ClientViewSet, basename='api_client')
router.register(r'catalog/manager', views.ManagerViewSet, basename='api_manager')

router.register(r'vehicle', views.VehicleViewSet, basename='api_vehicle')
router.register(r'maintenance', views.MaintenanceViewSet, basename='api_maintenance')
router.register(r'claims', views.ClaimsViewSet, basename='api_claims')


# swagger/redoc
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Silant Site",
        default_version='ver 1.0',
        description="API documentation",
        # terms_of_service="https://www.example.com/policies/terms/",
        terms_of_service="https://www.termsofservicegenerator.net/live.php?token=2osovODN2S0I3urRQYV6YKp8etpttYXF",
        # contact=openapi.Contact(email="viton4ik@gmail.com"),
        contact=openapi.Contact(
            name="Victor",
            url="https://github.com/Viton4ik",
            email="viton4ik@gmail.com",
        ),
        # license=openapi.License(
        #     name="BSD License",
        #     url="https://www.example.com/licenses/bsd/"
        # ),
        license=openapi.License(
            name="MIT License",
            url="https://opensource.org/licenses/MIT",
        ),
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,), 
    # permission_classes=(permissions.IsAdminUser,), 
    # permission_classes=(permissions.IsAuthenticated ,), 
    permission_classes=(permissions.IsAuthenticatedOrReadOnly ,), 
)


urlpatterns = [

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # rest_framework
    path('api/', include(router.urls), name='api'),

    # ===== views =====
    path('', indexPage, name='indexPage'),
    path('main/', mainPage, name='mainPage'),
    path('404/', html_404, name='html_404'),

]
