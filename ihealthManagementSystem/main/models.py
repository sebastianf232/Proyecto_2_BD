from django.db import models

# Create your models here.
class Asignacion(models.Model):
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_smartwatch = models.ForeignKey('Smartwatch', models.DO_NOTHING, db_column='id_smartwatch', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asignacion'

class CategoriaEjercicio(models.Model):
    id_categoria = models.CharField(primary_key=True, max_length=8)
    ejercicio = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categoria_ejercicio'

class MetodoPago(models.Model):
    cod_tarjeta = models.CharField(primary_key=True, max_length=8)
    nombre_tarjeta = models.CharField(max_length=75, blank=True, null=True)
    fecha_caducidad = models.DateField(blank=True, null=True)
    cvv = models.IntegerField(blank=True, null=True)
    tipo_tarjeta = models.ForeignKey('TipoTarjeta', models.DO_NOTHING, db_column='tipo_tarjeta', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'metodo_pago'

class Pago(models.Model):
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    cod_tarjeta = models.ForeignKey(MetodoPago, models.DO_NOTHING, db_column='cod_tarjeta', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pago'


class SesionEjercicio(models.Model):
    id_sesion = models.CharField(primary_key=True, max_length=8)
    fecha = models.DateField(blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    duracion = models.FloatField(blank=True, null=True)
    instructor = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='instructor', blank=True, null=True)
    categoria = models.ForeignKey(CategoriaEjercicio, models.DO_NOTHING, db_column='categoria', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sesion_ejercicio'


class SesionNutricionista(models.Model):
    id_sesion = models.CharField(primary_key=True, max_length=8)
    fecha = models.DateField(blank=True, null=True)
    hora_inicio = models.TimeField(blank=True, null=True)
    hora_fin = models.TimeField(blank=True, null=True)
    nutricionista = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='nutricionista', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sesion_nutricionista'


class Smartwatch(models.Model):
    id_smartwatch = models.CharField(primary_key=True, max_length=8)
    estado_smartwatch = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'smartwatch'


class Suscripcion(models.Model):
    id_suscripcion = models.CharField(primary_key=True, max_length=8)
    tipo = models.CharField(max_length=15, blank=True, null=True)
    precio = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'suscripcion'


class TipoRol(models.Model):
    cod_rol = models.CharField(primary_key=True, max_length=8)
    rol = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_rol'


class TipoTarjeta(models.Model):
    id_tipo_tarjeta = models.CharField(primary_key=True, max_length=8)
    tipo = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tipo_tarjeta'


class Trabajador(models.Model):
    id = models.CharField(primary_key=True, max_length=8)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    correo = models.CharField(unique=True, max_length=30, blank=True, null=True)
    passwordc = models.CharField(max_length=30, blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)
    rol = models.ForeignKey(TipoRol, models.DO_NOTHING, db_column='rol', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'trabajador'


class Usuario(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=8)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    nickname = models.CharField(unique=True, max_length=30, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    altura = models.FloatField(blank=True, null=True)
    caloria_actual = models.FloatField(blank=True, null=True)
    peso_actual = models.FloatField(blank=True, null=True)
    correo = models.CharField(unique=True, max_length=30, blank=True, null=True)
    passwordc = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'usuario'


class UsuarioSuscripcion(models.Model):
    id_usuario = models.ForeignKey(Usuario, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_suscripcion = models.ForeignKey(Suscripcion, models.DO_NOTHING, db_column='id_suscripcion', blank=True, null=True)
    activo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'usuario_suscripcion'

