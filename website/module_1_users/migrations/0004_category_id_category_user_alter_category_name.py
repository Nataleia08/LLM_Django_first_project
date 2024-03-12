# Generated by Django 4.2.5 on 2024-03-03 16:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('module_1_users', '0003_category_remove_example_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='category',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='module_1_users.userprofile'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]