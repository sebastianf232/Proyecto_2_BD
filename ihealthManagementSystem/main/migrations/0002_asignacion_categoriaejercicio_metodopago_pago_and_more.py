# Generated by Django 4.1.2 on 2022-10-11 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'asignacion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CategoriaEjercicio',
            fields=[
                ('id_categoria', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('ejercicio', models.CharField(blank=True, max_length=35, null=True)),
            ],
            options={
                'db_table': 'categoria_ejercicio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('cod_tarjeta', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre_tarjeta', models.CharField(blank=True, max_length=75, null=True)),
                ('fecha_caducidad', models.DateField(blank=True, null=True)),
                ('cvv', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'metodo_pago',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_tarjeta', models.ForeignKey(blank=True, db_column='cod_tarjeta', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.metodopago')),
            ],
            options={
                'db_table': 'pago',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SesionEjercicio',
            fields=[
                ('id_sesion', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('hora_inicio', models.TimeField(blank=True, null=True)),
                ('hora_fin', models.TimeField(blank=True, null=True)),
                ('duracion', models.FloatField(blank=True, null=True)),
                ('categoria', models.ForeignKey(blank=True, db_column='categoria', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.categoriaejercicio')),
            ],
            options={
                'db_table': 'sesion_ejercicio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SesionNutricionista',
            fields=[
                ('id_sesion', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('hora_inicio', models.TimeField(blank=True, null=True)),
                ('hora_fin', models.TimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sesion_nutricionista',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Smartwatch',
            fields=[
                ('id_smartwatch', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('estado_smartwatch', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'smartwatch',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id_suscripcion', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=15, null=True)),
                ('precio', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'suscripcion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoRol',
            fields=[
                ('cod_rol', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('rol', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'tipo_rol',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoTarjeta',
            fields=[
                ('id_tipo_tarjeta', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'tipo_tarjeta',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombres', models.CharField(blank=True, max_length=50, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=50, null=True)),
                ('correo', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('passwordc', models.CharField(blank=True, max_length=30, null=True)),
                ('activo', models.BooleanField(blank=True, null=True)),
                ('rol', models.ForeignKey(blank=True, db_column='rol', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.tiporol')),
            ],
            options={
                'db_table': 'trabajador',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombres', models.CharField(blank=True, max_length=50, null=True)),
                ('apellidos', models.CharField(blank=True, max_length=50, null=True)),
                ('nickname', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('altura', models.FloatField(blank=True, null=True)),
                ('caloria_actual', models.FloatField(blank=True, null=True)),
                ('peso_actual', models.FloatField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('passwordc', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UsuarioSuscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(blank=True, null=True)),
                ('id_suscripcion', models.ForeignKey(blank=True, db_column='id_suscripcion', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.suscripcion')),
                ('id_usuario', models.ForeignKey(blank=True, db_column='id_usuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.usuario')),
            ],
            options={
                'db_table': 'usuario_suscripcion',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.AddField(
            model_name='sesionnutricionista',
            name='nutricionista',
            field=models.ForeignKey(blank=True, db_column='nutricionista', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.trabajador'),
        ),
        migrations.AddField(
            model_name='sesionejercicio',
            name='instructor',
            field=models.ForeignKey(blank=True, db_column='instructor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.trabajador'),
        ),
        migrations.AddField(
            model_name='pago',
            name='id_usuario',
            field=models.ForeignKey(blank=True, db_column='id_usuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.usuario'),
        ),
        migrations.AddField(
            model_name='metodopago',
            name='tipo_tarjeta',
            field=models.ForeignKey(blank=True, db_column='tipo_tarjeta', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.tipotarjeta'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='id_smartwatch',
            field=models.ForeignKey(blank=True, db_column='id_smartwatch', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.smartwatch'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='id_usuario',
            field=models.ForeignKey(blank=True, db_column='id_usuario', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.usuario'),
        ),
    ]