from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Naimenovanie")
    description = models.TextField(verbose_name='place description',  blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor,on_delete=models.CASCADE, verbose_name='Sensor', null=True, blank=True)
    temperature = models.IntegerField(verbose_name='Temperature')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='measurement_images/')

    def __str__(self):
        return f"{self.sensor.name} - {self.temperature}°C (created at {self.created_at}, updated at {self.updated_at})"

    class Meta:
        ordering = ['-created_at']  # Сортировка измерений по времени создания (по умолчанию в порядке убывания)