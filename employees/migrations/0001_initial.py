# Generated for the Employee model.
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("department", models.CharField(max_length=80)),
                ("job_title", models.CharField(max_length=100)),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_joined", models.DateField()),
            ],
            options={"ordering": ["full_name"]},
        ),
    ]
