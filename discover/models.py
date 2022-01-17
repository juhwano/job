from django.db import models

# Create your models here.(시각화할 데이터)
class knowcode(models.Model):
    year = models.IntegerField()
    large_level = models.CharField(max_length=50)
    top_start_salary = models.IntegerField()
    avg_start_salary = models.IntegerField()
    top_salary = models.IntegerField()
    avg_salary = models.IntegerField()
    avg_age = models.IntegerField()
    man = models.IntegerField()
    woman = models.IntegerField()
    top_work_time = models.IntegerField()
    avg_work_time = models.IntegerField()
    count = models.IntegerField()
    ratio = models.IntegerField()

    def to_json(self):
        return {
            'year' : self.year,
            'large_level' : self.large_level,
            'top_start_salary' : self.top_start_salary,
            'avg_start_salary' : self.avg_start_salary,
            'top_salary' : self.top_salary,
            'avg_salary' : self.avg_salary,
            'avg_age' : self.avg_age,
            'man' : self.man,
            'woman' : self.woman,
            'top_work_time' : self.top_work_time,
            'avg_work_time' : self.avg_work_time,
            'count' : self.count,
            'ratio' : self.ratio,
        }

    def __str__(self):
        return str(self.year) + ", " + str(self.large_level) + "," + str(self.top_start_salary) + ", " + str(self.avg_start_salary)