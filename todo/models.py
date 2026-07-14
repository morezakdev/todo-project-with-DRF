from django.db import models

# Create your models here.


class todoModel(models.Model):
    title = models.CharField(max_length=225, verbose_name="عنوان")
    content = models.TextField(verbose_name="محتوا", null=True, blank=True)
    privory = models.IntegerField(default=1, verbose_name="اولویت")
    is_done = models.BooleanField(default=False, verbose_name="آیا انجام شده است؟")

    class Meta:
        db_table = "todos"
        verbose_name = "لیست انجام کار"
        verbose_name_plural = "تمامی لیست های انجام کار"

    def __str__(self):
        return self.title
