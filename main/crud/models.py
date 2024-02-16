from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = ("Employee")
        verbose_name_plural = ("Employees")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Employee_detail", kwargs={"pk": self.pk})

