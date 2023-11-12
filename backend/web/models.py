from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class CustomUserManager(BaseUserManager):
	def create_user(self, email, password=None, role=None):
		if not email:
			raise ValueError('A user email is needed.')

		if not password:
			raise ValueError('A user password is needed.')

		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, password=None):
		if not email:
			raise ValueError('A user email is needed.')

		if not password:
			raise ValueError('A user password is needed.')

		user = self.create_user(email, password, role='admin')
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user


class User(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, blank=True)
    employee_id = models.CharField(max_length=100, blank=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    SUPERUSER = 'superuser'
    BRANCH_ADMIN = 'branch_admin'
    BRANCH_PERSONNEL = 'branch_personnel'
    ROLE_CHOICES = [
        (SUPERUSER, ('Superuser')),
        (BRANCH_ADMIN, ('Branch Admin')),
        (BRANCH_PERSONNEL, ('Branch Personnel')),
    ]

    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default=SUPERUSER,
    )

    def __str__(self):
        return self.email


class Company(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)

class Branch(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)

class Supplier(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  # Name of the supplier
    contact_person = models.CharField(max_length=255)  # Name of the contact person
    contact_number = models.CharField(max_length=20)  # Contact number (can be a CharField or PhoneNumberField)
    email = models.EmailField()  # Email address of the supplier

class Brand(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, default="No description provided")
    # image = models.ImageField(null=True, default="image-svgrepo-com.svg")

class Category(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, default="No description provided")

class Product(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    actualweight = models.DecimalField(max_digits=8, decimal_places=2)
    netweight = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()
    units_sold = models.PositiveIntegerField()
    expiry_date = models.DateField()  
    status = models.CharField(max_length=20)  
    