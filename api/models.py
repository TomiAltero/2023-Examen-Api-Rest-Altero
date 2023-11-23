# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categories(models.Model):
    categoryid = models.AutoField(db_column='CategoryID', primary_key=True)  
    categoryname = models.CharField(db_column='CategoryName', max_length=15)  
    description = models.TextField(db_column='Description', blank=True, null=True)  
    picture = models.TextField(db_column='Picture', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Categories'


class Customercustomerdemo(models.Model):
    customerid = models.OneToOneField('Customers', models.DO_NOTHING, db_column='CustomerID', primary_key=True)   
    customertypeid = models.ForeignKey('Customerdemographics', models.DO_NOTHING, db_column='CustomerTypeID')  

    class Meta:
        managed = False
        db_table = 'CustomerCustomerDemo'
        unique_together = (('customerid', 'customertypeid'),)


class Customerdemographics(models.Model):
    customertypeid = models.CharField(db_column='CustomerTypeID', primary_key=True, max_length=10)  
    customerdesc = models.TextField(db_column='CustomerDesc', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'CustomerDemographics'


class Customers(models.Model):
    customerid = models.CharField(db_column='CustomerID', primary_key=True, max_length=5)  
    companyname = models.CharField(db_column='CompanyName', max_length=40)  
    contactname = models.CharField(db_column='ContactName', max_length=30, blank=True, null=True)  
    contacttitle = models.CharField(db_column='ContactTitle', max_length=30, blank=True, null=True)  
    address = models.CharField(db_column='Address', max_length=60, blank=True, null=True)  
    city = models.CharField(db_column='City', max_length=15, blank=True, null=True)  
    region = models.CharField(db_column='Region', max_length=15, blank=True, null=True)  
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)  
    country = models.CharField(db_column='Country', max_length=15, blank=True, null=True)  
    phone = models.CharField(db_column='Phone', max_length=24, blank=True, null=True)  
    fax = models.CharField(db_column='Fax', max_length=24, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Customers'


class Employeeterritories(models.Model):
    employeeid = models.OneToOneField('Employees', models.DO_NOTHING, db_column='EmployeeID', primary_key=True)   
    territoryid = models.ForeignKey('Territories', models.DO_NOTHING, db_column='TerritoryID')  

    class Meta:
        managed = False
        db_table = 'EmployeeTerritories'
        unique_together = (('employeeid', 'territoryid'),)


class Employees(models.Model):
    employeeid = models.AutoField(db_column='EmployeeID', primary_key=True)  
    lastname = models.CharField(db_column='LastName', max_length=20)  
    firstname = models.CharField(db_column='FirstName', max_length=10)  
    title = models.CharField(db_column='Title', max_length=30, blank=True, null=True)  
    titleofcourtesy = models.CharField(db_column='TitleOfCourtesy', max_length=25, blank=True, null=True)  
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)  
    address = models.CharField(db_column='Address', max_length=60, blank=True, null=True)  
    city = models.CharField(db_column='City', max_length=15, blank=True, null=True)  
    region = models.CharField(db_column='Region', max_length=15, blank=True, null=True)  
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)  
    country = models.CharField(db_column='Country', max_length=15, blank=True, null=True)  
    homephone = models.CharField(db_column='HomePhone', max_length=24, blank=True, null=True)  
    extension = models.CharField(db_column='Extension', max_length=4, blank=True, null=True)  
    photo = models.TextField(db_column='Photo', blank=True, null=True)  
    notes = models.TextField(db_column='Notes')  
    reportsto = models.ForeignKey('self', models.DO_NOTHING, db_column='ReportsTo', blank=True, null=True)  
    photopath = models.CharField(db_column='PhotoPath', max_length=255, blank=True, null=True)  
    salary = models.FloatField(db_column='Salary', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Employees'


class Orderdetails(models.Model):
    orderid = models.OneToOneField('Orders', models.DO_NOTHING, db_column='OrderID', primary_key=True)   
    productid = models.ForeignKey('Products', models.DO_NOTHING, db_column='ProductID')  
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=4)  
    quantity = models.SmallIntegerField(db_column='Quantity')  
    discount = models.FloatField(db_column='Discount')  

    class Meta:
        managed = False
        db_table = 'OrderDetails'
        unique_together = (('orderid', 'productid'),)


class Orders(models.Model):
    orderid = models.AutoField(db_column='OrderID', primary_key=True)  
    customerid = models.ForeignKey(Customers, models.DO_NOTHING, db_column='CustomerID', blank=True, null=True)  
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EmployeeID', blank=True, null=True)  
    orderdate = models.DateTimeField(db_column='OrderDate', blank=True, null=True)  
    requireddate = models.DateTimeField(db_column='RequiredDate', blank=True, null=True)  
    shippeddate = models.DateTimeField(db_column='ShippedDate', blank=True, null=True)  
    shipvia = models.ForeignKey('Shippers', models.DO_NOTHING, db_column='ShipVia', blank=True, null=True)  
    freight = models.DecimalField(db_column='Freight', max_digits=10, decimal_places=4, blank=True, null=True)  
    shipname = models.CharField(db_column='ShipName', max_length=40, blank=True, null=True)  
    shipaddress = models.CharField(db_column='ShipAddress', max_length=60, blank=True, null=True)  
    shipcity = models.CharField(db_column='ShipCity', max_length=15, blank=True, null=True)  
    shipregion = models.CharField(db_column='ShipRegion', max_length=15, blank=True, null=True)  
    shippostalcode = models.CharField(db_column='ShipPostalCode', max_length=10, blank=True, null=True)  
    shipcountry = models.CharField(db_column='ShipCountry', max_length=15, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Orders'


class Products(models.Model):
    productid = models.AutoField(db_column='ProductID', primary_key=True)  
    productname = models.CharField(db_column='ProductName', max_length=40)  
    supplierid = models.ForeignKey('Suppliers', models.DO_NOTHING, db_column='SupplierID', blank=True, null=True)  
    categoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='CategoryID', blank=True, null=True)  
    quantityperunit = models.CharField(db_column='QuantityPerUnit', max_length=20, blank=True, null=True)  
    unitprice = models.DecimalField(db_column='UnitPrice', max_digits=10, decimal_places=4, blank=True, null=True)  
    unitsinstock = models.SmallIntegerField(db_column='UnitsInStock', blank=True, null=True)  
    unitsonorder = models.SmallIntegerField(db_column='UnitsOnOrder', blank=True, null=True)  
    reorderlevel = models.SmallIntegerField(db_column='ReorderLevel', blank=True, null=True)  
    discontinued = models.TextField(db_column='Discontinued')  

    class Meta:
        managed = False
        db_table = 'Products'


class Region(models.Model):
    regionid = models.IntegerField(db_column='RegionID', primary_key=True)  
    regiondescription = models.CharField(db_column='RegionDescription', max_length=50)  

    class Meta:
        managed = False
        db_table = 'Region'


class Shippers(models.Model):
    shipperid = models.AutoField(db_column='ShipperID', primary_key=True)  
    companyname = models.CharField(db_column='CompanyName', max_length=40)  
    phone = models.CharField(db_column='Phone', max_length=24, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Shippers'


class Suppliers(models.Model):
    supplierid = models.AutoField(db_column='SupplierID', primary_key=True)  
    companyname = models.CharField(db_column='CompanyName', max_length=40)  
    contactname = models.CharField(db_column='ContactName', max_length=30, blank=True, null=True)  
    contacttitle = models.CharField(db_column='ContactTitle', max_length=30, blank=True, null=True)  
    address = models.CharField(db_column='Address', max_length=60, blank=True, null=True)  
    city = models.CharField(db_column='City', max_length=15, blank=True, null=True)  
    region = models.CharField(db_column='Region', max_length=15, blank=True, null=True)  
    postalcode = models.CharField(db_column='PostalCode', max_length=10, blank=True, null=True)  
    country = models.CharField(db_column='Country', max_length=15, blank=True, null=True)  
    phone = models.CharField(db_column='Phone', max_length=24, blank=True, null=True)  
    fax = models.CharField(db_column='Fax', max_length=24, blank=True, null=True)  
    homepage = models.TextField(db_column='HomePage', blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'Suppliers'


class Territories(models.Model):
    territoryid = models.CharField(db_column='TerritoryID', primary_key=True, max_length=20)  
    territorydescription = models.CharField(db_column='TerritoryDescription', max_length=50)  
    regionid = models.ForeignKey(Region, models.DO_NOTHING, db_column='RegionID')  

    class Meta:
        managed = False
        db_table = 'Territories'


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
