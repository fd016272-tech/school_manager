from django.db import migrations, models


def split_student_names(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    for student in Student.objects.all().iterator():
        parts = student.name.strip().rsplit(' ', 1)
        if len(parts) == 2:
            student.first_name, student.last_name = parts
        else:
            student.last_name = parts[0]
        student.save(update_fields=['first_name', 'last_name'])


def restore_student_names(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    for student in Student.objects.all().iterator():
        student.name = ' '.join(
            part for part in (student.first_name, student.last_name) if part
        )
        student.save(update_fields=['name'])


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='', max_length=100, verbose_name='prénom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=100, verbose_name='nom'),
            preserve_default=False,
        ),
        migrations.RenameField(
            model_name='student',
            old_name='classroom',
            new_name='classe',
        ),
        migrations.AlterField(
            model_name='student',
            name='classe',
            field=models.CharField(max_length=10, verbose_name='classe'),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='âge'),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='student',
            name='active',
            field=models.BooleanField(default=True, verbose_name='actif'),
        ),
        migrations.AddField(
            model_name='student',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='date de naissance'),
        ),
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='inscrit le'),
        ),
        migrations.RunPython(split_student_names, restore_student_names),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]
