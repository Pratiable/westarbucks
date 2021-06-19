# Generated by Django 3.2.4 on 2021-06-19 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition',
            name='caffeine_mg',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='protein_g',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='saturated_fat_g',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='size_fluid_ounce',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='size_ml',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='sodium_mg',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='sugars_g',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
