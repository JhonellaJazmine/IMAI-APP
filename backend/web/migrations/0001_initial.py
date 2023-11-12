# Generated by Django 4.2.6 on 2023-11-09 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('contact_person', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(default='No description provided', max_length=255)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(default='No description provided', max_length=255)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_person', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('contact_person', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('actualweight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('netweight', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock_quantity', models.PositiveIntegerField()),
                ('units_sold', models.PositiveIntegerField()),
                ('expiry_date', models.DateField()),
                ('status', models.CharField(max_length=20)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.branch')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.supplier')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.company'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
