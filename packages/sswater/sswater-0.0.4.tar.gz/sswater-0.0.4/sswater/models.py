from django.db import models

# 단일 유량 모델
class Water(models.Model):
    data_time = models.DateTimeField(null=True) # 시간
    ma_q = models.FloatField(null=True) # 유량

# 기후 추가 모델
class WaterCli(models.Model):
    data_time = models.DateTimeField(null=True) # 시간
    ma_q = models.FloatField(null=True) # 유량
    temp = models.FloatField(null=True) # 기온
    humodity = models.IntegerField(null=True) # 습도
    atmo = models.FloatField(null=True) # 증기압
    floor = models.FloatField(null=True) # 지면온도
    hr = models.FloatField(null=True) # 일조량