from django.db import models

class Menu(models.Model):
  name = models.CharField(max_length=255)
  desc = models.CharField(max_length=255)
  Kinds = models.TextChoices('Kinds','Breakfast Meals Snacks Desserts Drinks')
  kind = models.CharField(blank=True, choices=Kinds.choices, max_length=10)
  #img = models.ImageField(upload_to='uploads/')
  price = models.DecimalField(max_digits=8, decimal_places=2)

  def __str__(self):
          return self.name

class Reservation(models.Model): 
  fullname = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  phone_number = models.CharField(max_length=12)
  people = models.IntegerField()
  date = models.DateField()
  time = models.TimeField()
  message = models.TextField()

  def __str__(self):
          return self.fullname

class Gallery(models.Model): 
  image = models.ImageField(upload_to='uploads/')
  Types = models.TextChoices('Types','Food Drink Restaurant Dinner Dessert')
  type = models.CharField(blank=True, choices=Types.choices, max_length=20)

  def __str__(self):
          return str(self.image)

class Subscription(models.Model): 
  email = models.EmailField(max_length=255)

  def __str__(self):
          return str(self.email)

class Chef(models.Model): 
  fullname = models.CharField(max_length=255)
  #Types = models.TextChoices('Types','Head Chef, Pizza Chef, Grill Chef, Burger Chef')
  #type = models.CharField(blank=True, choices=Types.choices, max_length=20)  
  photo = models.ImageField(upload_to='uploads/')
  facebook = models.CharField(max_length=255)
  twitter = models.CharField(max_length=255)
  linkedin = models.CharField(max_length=255)

  def __str__(self):
          return str(self.fullname)

class Blog(models.Model): 
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  banner = models.ImageField(upload_to='uploads/')
  release_date = models.DateField()
  content = models.TextField()

  def __str__(self):
          return str(self.title)

class Contact(models.Model): 
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  subject = models.CharField(max_length=255)
  message = models.TextField()

  def __str__(self):
          return str(self.name)