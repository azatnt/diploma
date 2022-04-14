from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    des = models.TextField()
    image = models.ImageField(upload_to='static/images', blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    des = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name='order_service', blank=True,
                                null=True)
    time = models.CharField(max_length=120, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.service.name

    class Meta:
        verbose_name = "Время услуги"
        verbose_name_plural = "Время услуги"


class Staff(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    des = models.TextField()
    service = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='static/images', blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + self.surname

    class Meta:
        verbose_name = "Сотрудники"
        verbose_name_plural = "Сотрудники"


class Message(models.Model):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=120, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name + " " + self.phone

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщение"


class OnlineOrder(models.Model):
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name="online_order_service")
    time = models.CharField(max_length=120)
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return self.service.name + " " + self.full_name

    class Meta:
        verbose_name = "Онлайн запись"
        verbose_name_plural = "Онлайн запись"

class Analiz(models.Model):
    name = models.CharField(max_length=150)
    des = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Анализы"
        verbose_name_plural = "Анализы"