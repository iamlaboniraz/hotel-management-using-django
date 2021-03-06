# Generated by Django 2.0 on 2020-03-04 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField()),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=50, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('contact_number', models.IntegerField(verbose_name='Contact Number')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('email_address', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customer Information',
                'ordering': ['-customer_id'],
                'permissions': (('can_view_customer', 'Can view customer'),),
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='Facility Name')),
                ('price', models.PositiveIntegerField(verbose_name='Facility Price')),
            ],
            options={
                'verbose_name': 'Facility',
                'verbose_name_plural': 'All Facility Information',
                'ordering': ['-id', '-price'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_adults', models.PositiveIntegerField(default=1, verbose_name='Number of Adult Member')),
                ('no_of_childrens', models.PositiveIntegerField(default=0, verbose_name='Number of Children')),
                ('reservation_date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Reservation Date Time')),
                ('expected_arrival_date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Expected Arrival Date Time')),
                ('expected_departure_date_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Expected Departure Date Time')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer', verbose_name='Customer Name')),
            ],
            options={
                'verbose_name': 'Reservation',
                'verbose_name_plural': 'Reservation Information',
                'ordering': ['-reservation_id'],
                'permissions': (('can_view_reservation', 'Can View Reservation'), ('can_view_reservations_default', 'Can view reservation default')),
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=10, unique=True, verbose_name='Room Number')),
                ('availability', models.BooleanField(default=0)),
                ('facility', models.ManyToManyField(to='myapp.Facility')),
                ('reservation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Reservation', verbose_name='Reservation Information')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Room',
                'ordering': ['room_no'],
                'permissions': (('can_view_room', 'Can View Room'),),
            },
        ),
        migrations.CreateModel(
            name='RoomCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='room_img/%Y/%m/%d', verbose_name='Room Picture', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('room_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField()),
                ('price', models.PositiveIntegerField(verbose_name='Room Price')),
                ('size', models.CharField(max_length=1000, verbose_name='Room Size')),
                ('capacity', models.IntegerField(verbose_name='Capacity')),
                ('pets', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], default='false', max_length=10)),
                ('breakfast', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], default='false', max_length=10)),
                ('features', models.CharField(blank=True, choices=[('true', 'true'), ('false', 'false')], default='false', max_length=10)),
                ('description', models.TextField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.RoomCatagory')),
                ('extras', models.ManyToManyField(to='myapp.Facility')),
            ],
            options={
                'verbose_name': 'RoomType',
                'verbose_name_plural': 'All Room Information',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RoomTypeName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_picture', models.ImageField(default='image/staff.png', upload_to='staff_img', verbose_name='Own Picture')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_number', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('email_address', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff Information',
                'ordering': ['first_name', 'middle_name', 'last_name'],
                'permissions': (('can_view_staff', 'Can view staff'), ('can_view_staff_details', 'Can view staff detail')),
            },
        ),
        migrations.AddField(
            model_name='roomtype',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.RoomTypeName'),
        ),
        migrations.AddField(
            model_name='roomimage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.RoomType'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.RoomType', verbose_name='Room Type'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='staff',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.fields.CharField, to='myapp.Staff', verbose_name='Staff Name'),
        ),
    ]
