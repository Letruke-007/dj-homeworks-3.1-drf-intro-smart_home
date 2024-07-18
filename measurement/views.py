from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from .models import Measurement, Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


# Обновить датчик и получить информацию о конкретном датчике
# PUT (обновление) и GET (получение)
class SensorDetailView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = 'id'



# Добавить измерение
# POST
class AddMeasurementView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer



# Получить список датчиков и создать новый датчик
# GET (получение списка) и POST (создание)
class SensorListGreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class DeleteSensorView(generics.DestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Sensor successfully deleted"}, status=status.HTTP_200_OK)


# # Получить информацию по конкретному датчику
# # GET
# class GetSensorInfoView(generics.RetrieveAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer
#     lookup_field = 'id'


# Создать датчик
# # POST
# class CreateSensorView(generics.CreateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer


#
# # Получить список датчиков
# # GET
# class GetSensorListView(generics.ListAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer



# # Изменить датчик
# # PUT
# class UpdateSensorView(generics.UpdateAPIView):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorDetailSerializer
