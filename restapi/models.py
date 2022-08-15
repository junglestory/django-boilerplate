# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Salary(models.Model):
    empno = models.IntegerField(db_column='EMPNO')  # Field name made lowercase.
    sal = models.IntegerField(db_column='SAL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SALARY'


class Student(models.Model):
    no = models.IntegerField(db_column='NO')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=10)  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE')  # Field name made lowercase.
    subject = models.CharField(db_column='SUBJECT', max_length=20)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STUDENT'


class Student2(models.Model):
    no = models.IntegerField(db_column='NO')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=10)  # Field name made lowercase.
    grade = models.IntegerField(db_column='GRADE')  # Field name made lowercase.
    subject = models.CharField(db_column='SUBJECT', max_length=20)  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE')  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STUDENT2'


class Student3(models.Model):
    stid = models.IntegerField(db_column='STID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=10)  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE')  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DEPTID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STUDENT3'


class Subject(models.Model):
    code = models.IntegerField(db_column='CODE')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=10)  # Field name made lowercase.
    grade = models.CharField(db_column='GRADE', max_length=2)  # Field name made lowercase.
    score = models.IntegerField(db_column='SCORE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SUBJECT'


class T1(models.Model):
    code = models.CharField(db_column='CODE', max_length=4)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T1'


class T2(models.Model):
    no = models.CharField(db_column='NO', max_length=2)  # Field name made lowercase.
    rule = models.CharField(db_column='RULE', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T2'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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
    id = models.BigAutoField(primary_key=True)
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


class News(models.Model):
    seq = models.AutoField(db_column='SEQ', primary_key=True)  # Field name made lowercase.
    journal_id = models.CharField(db_column='JOURNAL_ID', max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=200)  # Field name made lowercase.
    publish_date = models.CharField(db_column='PUBLISH_DATE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    link_url = models.CharField(db_column='LINK_URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    writer = models.CharField(db_column='WRITER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    reg_date = models.DateTimeField(db_column='REG_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'news'
