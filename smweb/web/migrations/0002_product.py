# Generated by Django 2.1.7 on 2019-03-12 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=200)),
                ('submenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Submenu')),
            ],
        ),
    ]