from rest_framework import serializers
from .models import User, Company, Branch, Supplier, Brand, Category, Product, Cart
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100,
        min_length=8,
        style={'input_type': 'password'}
    )
    role = serializers.ChoiceField(
        choices=User.ROLE_CHOICES,
        default=User.SUPERUSER
    )
    employee_id = serializers.CharField(max_length=100, required=False)
    contact = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'role', 'employee_id', 'contact']

    def create(self, validated_data):
        user_password = validated_data.get('password', None)
        db_instance = self.Meta.model(
            email=validated_data.get('email'),
            username=validated_data.get('username'),
            role=validated_data.get('role'),
            employee_id=validated_data.get('employee_id', ''),
            contact=validated_data.get('contact', '')
        )
        db_instance.set_password(user_password)
        db_instance.save()
        return db_instance



class UserLoginSerializer(serializers.Serializer):
	email = serializers.CharField(max_length=100)
	username = serializers.CharField(max_length=100, read_only=True)
	password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
	token = serializers.CharField(max_length=255, read_only=True)
#######

class SuperAdminRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'role')

class BranchAdminRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
    employee_id = serializers.CharField(max_length=100)
    contact = serializers.CharField(max_length=100)
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    # roles = serializers.ChoiceField(choices=User.ROLE_CHOICES, default=User.BRANCH_ADMIN)
    
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password', 'employee_id', 'contact', 'company', 'role']

    def create(self, validated_data):
        user_password = validated_data.get('password', None)
        role = get_user_model().BRANCH_ADMIN  # Set the role to 'BRANCH_ADMIN'

        # Extract values for employee_id and contact from validated_data
        employee_id = validated_data.get('employee_id')
        contact = validated_data.get('contact')
        company = validated_data.get('company')


        db_instance = self.Meta.model(
            email=validated_data.get('email'),
            username=validated_data.get('username'),
            role=role,
            employee_id=employee_id,
            contact=contact,
            company=company,
            # roles=validated_data.get('roles')
        )
        db_instance.set_password(user_password)
        db_instance.save()
        return db_instance
        # else:
        #     raise serializers.ValidationError('Permission denied. Only superusers can create branch admins.')
#######

class BranchPersonnelRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
    employee_id = serializers.CharField(max_length=100)
    contact = serializers.CharField(max_length=100)
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    # roles = serializers.ChoiceField(choices=User.ROLE_CHOICES, default=User.BRANCH_ADMIN)
    
    class Meta:
        model = get_user_model()
        fields = ['email', 'username', 'password', 'employee_id', 'contact', 'company', 'role']

    def create(self, validated_data):
        user_password = validated_data.get('password', None)
        role = get_user_model().BRANCH_PERSONNEL 

        # Extract values for employee_id and contact from validated_data
        employee_id = validated_data.get('employee_id')
        contact = validated_data.get('contact')
        company = validated_data.get('company')


        db_instance = self.Meta.model(
            email=validated_data.get('email'),
            username=validated_data.get('username'),
            role=role,
            employee_id=employee_id,
            contact=contact,
            company=company,
            # roles=validated_data.get('roles')
        )
        db_instance.set_password(user_password)
        db_instance.save()
        return db_instance
    
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
        company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())


# class ProductSerializer(serializers.ModelSerializer):
#     category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True)
#     brand_id = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), write_only=True)

#     class Meta:
#         model = Product
#         fields = ['id', 'name', 'barcode', 'price', 'description', 'weight', 'category_id', 'brand_id', 'stock_quantity', 'units_sold']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    brand = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all())


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        branch = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
