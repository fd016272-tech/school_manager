from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_database_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='téléphone'),
        ),
    ]
