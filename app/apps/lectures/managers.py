from django.db import models

class LectureManager(models.Manager):
    def filter_by_sensor_and_date_range(self, sensor_code, start_datetime, end_datetime):
        return self.filter(
            sensor__code=sensor_code,
            created__gte=start_datetime,
            created__lte=end_datetime
        )
    
    def filter_by_sensor_and_date_range_and_topic(self, sensor_code, start_datetime, end_datetime, topic):
        return self.filter(
            sensor__code=sensor_code,
            created__gte=start_datetime,
            created__lte=end_datetime
        ).values(str(topic), 'created')
   