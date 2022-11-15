from django.db import models

class Menu(models.Model):
  name = models.CharField(max_length=255)
  desc = models.CharField(max_length=255)
  Kinds = models.TextChoices('Kinds','Breakfast Meals Snacks Desserts Drinks')
  kind = models.CharField(blank=True, choices=Kinds.choices, max_length=10)
  price = models.DecimalField(max_digits=8, decimal_places=2)

  def __str__(self):
        return self.name