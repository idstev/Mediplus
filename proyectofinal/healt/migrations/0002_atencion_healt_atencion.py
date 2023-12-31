# Generated by Django 4.2.4 on 2023-09-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10, verbose_name='Horario de atencion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='fecha de modificacion')),
            ],
            options={
                'verbose_name': 'Dia laboral',
                'verbose_name_plural': 'Dias laborales',
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='healt',
            name='atencion',
            field=models.ManyToManyField(to='healt.atencion', verbose_name='Atencion'),
        ),
    ]
