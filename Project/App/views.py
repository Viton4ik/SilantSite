from django.shortcuts import render

from django.contrib.auth.models import User

from django.core.paginator import Paginator

# ===== rest_framework =====

from rest_framework import permissions
from rest_framework import viewsets

import django_filters.rest_framework
from App.serializers import *


# create a ReadOnly
class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
    
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_active',]

    permission_classes = [permissions.IsAuthenticated]
    # XXX: permission_classes = [permissions.IsAdminUser]


class VehicleModelViewSet(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class EngineModelViewSet(viewsets.ModelViewSet):
    queryset = EngineModel.objects.all()
    serializer_class = EngineModelSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # FIXME: class has to chosen properly!
    permission_classes = [permissions.IsAdminUser]


class TransmissionModelViewSet(viewsets.ModelViewSet):
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionModelSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # NOTE: полный доступ только аутентифицированным пользователям с правами доступа к модели
    permission_classes = [permissions.DjangoModelPermissions]


class DriveAxleModelViewSet(viewsets.ModelViewSet):
    queryset = DriveAxleModel.objects.all()
    serializer_class = DriveAxleModelSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # NOTE: полный доступ аутентифицированным пользователям с правами доступа к модели и только чтение для неаутентифицированных пользователей
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class SteeringAxleModelViewSet(viewsets.ModelViewSet):
    queryset = SteeringAxleModel.objects.all()
    serializer_class = SteeringAxleModelSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class MaintenanceTypeViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceType.objects.all()
    serializer_class = MaintenanceTypeSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class MalfunctionOverviewViewSet(viewsets.ModelViewSet):
    queryset = MalfunctionOverview.objects.all()
    serializer_class = MalfunctionOverviewSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class RepairingMethodViewSet(viewsets.ModelViewSet):
    queryset = RepairingMethod.objects.all()
    serializer_class = RepairingMethodSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class MaintenanceCompanyViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceCompany.objects.all()
    serializer_class = MaintenanceCompanySerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', ]

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class ServiceCompanyViewSet(viewsets.ModelViewSet):
    queryset = ServiceCompany.objects.all()
    serializer_class = ServiceCompanySerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    ffilterset_fields = ['id', 'name', 'description', 'role']

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', 'role', ]

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', 'role', ]

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


# Essences
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'vehicleNumber', 'vehicleModel', 'engineModel', 'engineNumber', 'transmissionModel', 'transmissionNumber', 'driveAxleModel', 'driveAxleNumber', 'steeringAxleModel', 'steeringAxleNumber', 'deliveryContract_N_data', 'deliveryDate', 'consignee', 'deliveryAdress', 'completeSet', 'client', 'serviceCompany',]

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]


class ClaimsViewSet(viewsets.ModelViewSet):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'

    # TODO: class has to chosen properly!
    permission_classes = [permissions.IsAuthenticated|ReadOnly]



# ===== views =====

def html_404(request):
    return render(request, 'App/404.html', {}, status=404)


def indexPage(request):
    return render(request, 'App/index.html', {})


def mainPage(request):

    # vehicles=Vehicle.objects.filter().values_list("deliveryDate", flat=True)
    # vehicles=Vehicle.objects.filter().values("deliveryDate")
    vehicles = Vehicle.objects.all().order_by('-deliveryDate')
    user = request.user
    print('user:', user)
    print('user.id:', user.id)
    print('vehicle:', vehicles)

    # Получение страницы из параметров запроса
    page_number = request.GET.get('page')

    # Создание объекта Paginator
    paginator = Paginator(vehicles, 10)  

    # Получение объекта Page для текущей страницы
    page = paginator.get_page(page_number)

    return render(request, 'App/main.html', {'vehicles': vehicles, 'page': page})


