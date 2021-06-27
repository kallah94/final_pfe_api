# Generated by Django 3.0.5 on 2021-06-24 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root_app', '0005_atom_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='data_security',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='flexibility',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='geo_dispatching',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='maturity',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='price',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='reliability',
        ),
        migrations.CreateModel(
            name='ProviderAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='root_app.Attribute')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root_app.Provider')),
            ],
        ),
    ]
