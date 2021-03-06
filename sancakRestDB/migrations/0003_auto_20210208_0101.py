# Generated by Django 3.1.6 on 2021-02-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sancakRestDB', '0002_auto_20210208_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='kunye',
            name='aciklama',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='aciklama'),
        ),
        migrations.AddField(
            model_name='kunye',
            name='yakinlik_derecesi',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='yakinlik_derecesi'),
        ),
        migrations.AlterField(
            model_name='kmtakip',
            name='aciklama',
            field=models.CharField(blank=True, db_column='Aciklama', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='kmtakip',
            name='adisoyadi',
            field=models.CharField(db_column='AdiSoyadi', max_length=40),
        ),
        migrations.AlterField(
            model_name='kmtakip',
            name='rota',
            field=models.CharField(blank=True, db_column='Rota', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='kunye',
            name='ehliyetno',
            field=models.CharField(db_column='EhliyetNo', default='Ekleyin!', max_length=10),
        ),
        migrations.AlterField(
            model_name='kunye',
            name='yelekdontarihi',
            field=models.CharField(blank=True, db_column='YelekDonTarihi', max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='sayman',
            name='aciklama',
            field=models.CharField(blank=True, db_column='Aciklama', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='sayman',
            name='odemeaciklama',
            field=models.CharField(blank=True, db_column='OdemeAciklama', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='sayman',
            name='odenentl',
            field=models.DecimalField(blank=True, db_column='OdenenTl', decimal_places=1, help_text='Sadece "diğer ödeme" seçeneğini seçtiğinizde fiyat giriniz', max_digits=5, null=True),
        ),
    ]
