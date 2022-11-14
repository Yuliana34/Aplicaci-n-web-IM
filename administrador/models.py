# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AdjuntarArchivos(models.Model):
    iddocumento = models.AutoField(primary_key=True)
    registro_fotografico = models.ImageField(upload_to='fotobuses', null=True)
    soat = models.FileField(upload_to='archivos', null=True)
    tecnomecanico = models.FileField(upload_to='archivos', null=True)
    identificacion_propietario = models.FileField(upload_to='archivos', null=True)
    tarjeta_propiedad = models.FileField(upload_to='archivos', null=True)

    class Meta:
        managed = False
        db_table = 'adjuntar_archivos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128,unique=True)
    password2 = models.CharField(max_length=128)
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CargarDocumento(models.Model):
    iddocumento = models.AutoField(primary_key=True)
    certificado_alcoholemia = models.FileField(upload_to='archivos', null=True)
    certificado_sustancias_psicoactivas = models.FileField(upload_to='archivos', null=True)

    class Meta:
        managed = False
        db_table = 'cargar_documento'


class Conductor(models.Model):
    idconductor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    correo_electronico = models.CharField(unique=True, max_length=30)
    numero_identificacion = models.CharField(unique=True, max_length=15)
    fecha_expedicion_documento = models.DateField()
    lugar_expedicion_documento = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    edad = models.PositiveIntegerField()
    direccion = models.CharField(max_length=20)
    telefono = models.CharField(unique=True, max_length=10)
    telefono_alterno = models.CharField(unique=True, max_length=10)
    turno_idturno = models.ForeignKey('Turno', models.DO_NOTHING, db_column='turno_idturno')
    subir_archivos_iddocumento = models.ForeignKey('SubirArchivos', models.DO_NOTHING, db_column='subir_archivos_iddocumento')
    departamento_iddepartamento = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='departamento_iddepartamento')

    class Meta:
        managed = False
        db_table = 'conductor'
        
        
    def __str__(self):
        return self.nombres


class Departamento(models.Model):
    iddepartamento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=90)
    codigo = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'departamento'
        
    def __str__(self):
        return self.nombre


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Municipio(models.Model):
    idmunicipio = models.AutoField(primary_key=True)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING)
    codigo = models.PositiveIntegerField()
    nombre = models.CharField(max_length=90)

    class Meta:
        managed = False
        db_table = 'municipio'


class Paradero(models.Model):
    idparadero = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    ubicacion_idubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, db_column='ubicacion_idubicacion')
    ruta_idruta = models.ForeignKey('Ruta', models.DO_NOTHING, db_column='ruta_idruta')

    class Meta:
        managed = False
        db_table = 'paradero'


class PlanRodamiento(models.Model):
    idplan_rodamiento = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    inicio_ruta = models.CharField(max_length=30)
    numero_vehiculo = models.PositiveIntegerField(blank=True, null=True)
    numero_ruta = models.PositiveIntegerField(blank=True, null=True)
    vehiculo_idvehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_idvehiculo')
    ruta_idruta = models.ForeignKey('Ruta', models.DO_NOTHING, db_column='ruta_idruta')
    cargar_documento_iddocumento = models.ForeignKey(CargarDocumento, models.DO_NOTHING, db_column='cargar_documento_iddocumento')

    class Meta:
        managed = False
        db_table = 'plan_rodamiento'


class Ruta(models.Model):
    idruta = models.AutoField(primary_key=True)
    inicio_ruta = models.CharField(max_length=30)
    retorno_ruta = models.CharField(max_length=30)
    fin_ruta = models.CharField(max_length=30)
    numero_ruta = models.PositiveIntegerField()
    distancia_kilometros = models.PositiveIntegerField()
    tiempo_estimado = models.CharField(max_length=15, blank=True, null=True)
    numero_vueltas = models.PositiveIntegerField(blank=True, null=True)
    vehiculo_idvehiculo = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_idvehiculo')

    class Meta:
        managed = False
        db_table = 'ruta'
    
    def __str__(self):
        return self.inicio_ruta



class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class SubirArchivos(models.Model):
    iddocumento = models.AutoField(primary_key=True)
    documento_identidad = models.FileField(upload_to='archivos', null=True)
    experiencia_laboral = models.FileField(upload_to='archivos', null=True)
    licencia_conduccion = models.FileField(upload_to='archivos', null=True)

    class Meta:
        managed = False
        db_table = 'subir_archivos'


class Turno(models.Model):
    idturno = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15)
    fecha = models.DateField()
    hora = models.TimeField()

    class Meta:
        managed = False
        db_table = 'turno'
        
    def __str__(self):
        return self.nombre


class Ubicacion(models.Model):
    idubicacion = models.AutoField(primary_key=True)
    longitud = models.FloatField()
    latitud = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ubicacion'


class Vehiculo(models.Model):
    idvehiculo = models.AutoField(primary_key=True)
    numero_orden = models.PositiveIntegerField(unique=True)
    numero_licencia_transito = models.CharField(unique=True, max_length=30)
    nombre_propietario = models.CharField(max_length=45)
    identificacion_propietario = models.CharField(unique=True, max_length=15)
    placa = models.CharField(unique=True, max_length=10)
    marca = models.CharField(max_length=20)
    linea = models.CharField(max_length=20)
    modelo = models.PositiveIntegerField()
    capacidad_personas = models.PositiveIntegerField()
    clase_vehiculo = models.CharField(max_length=20)
    cilindraje = models.FloatField()
    numero_chasis = models.CharField(unique=True, max_length=20)
    tipo_combustible = models.CharField(max_length=10)
    numero_motor = models.CharField(unique=True, max_length=20)
    tipo_carroceria = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    vin = models.CharField(unique=True, max_length=20)
    numero_ejes = models.IntegerField()
    conductor_idconductor = models.ForeignKey(Conductor, models.DO_NOTHING, db_column='conductor_idconductor')
    adjuntar_archivos_iddocumento = models.ForeignKey(AdjuntarArchivos, models.DO_NOTHING, db_column='adjuntar_archivos_iddocumento')
    ubicacion_idubicacion = models.ForeignKey(Ubicacion, models.DO_NOTHING, db_column='ubicacion_idubicacion')

    class Meta:
        managed = False
        db_table = 'vehiculo'
        
    def __str__(self):
        return self.placa
