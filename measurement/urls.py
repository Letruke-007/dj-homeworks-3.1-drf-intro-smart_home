from django.urls import path
# from .views import CreateSensorView, SensorDetailView, AddMeasurementView, GetSensorListView
from .views import SensorListGreateView, SensorDetailView, AddMeasurementView, DeleteSensorView


urlpatterns = [
    path('create-sensor/', SensorListGreateView.as_view(), name='create_sensor'),
    path('update-sensor/<int:id>/', SensorDetailView.as_view(), name='update_sensor'),

    path('add-measurement/', AddMeasurementView.as_view(), name='add_measurement'),
    path('get-sensor-list/', SensorListGreateView.as_view(), name='get_sensor_list'),
    #path('get-sensor-info/<int:id>/', GetSensorInfoView.as_view(), name='get_sensor_info'),
    path('get-sensor-info/<int:id>/', SensorDetailView.as_view(), name='sensor_detail'),
    path('delete-sensor/<int:id>/', DeleteSensorView.as_view(), name ='delete_sensor'),
    # Другие маршруты...
]

