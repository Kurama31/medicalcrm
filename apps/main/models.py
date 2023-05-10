from django.db import models
from django.db.models import QuerySet


from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class MenuItem(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name




#==================================================================== Example fo future
class Research(models.Model):
    organization = models.ForeignKey(
        "main.Organization",
        on_delete=models.deletion.SET_NULL,
        related_name='organization_researches',
        db_index=True,
        null=True,
        blank=False
    )
    @property
    def statement_history(self):
        return self.research_statement_history.all()
    # ONE TO MANY Statement (Statement history)


class Customer(models.Model):
    first_name = models.CharField(
        max_length=255, null=False, blank=True
    )
    last_name = models.CharField(
        max_length=255, null=False, blank=True
    )
    email = models.EmailField(
        max_length=255, null=False, blank=True
    )


    organization = models.ForeignKey(
        "main.Organization",
        on_delete=models.deletion.SET_NULL,
        related_name='organization_customers',
        null=True,
        blank=False
    )

    @property
    def orders(self):
        return self.customers_orders.all()

#class payment

class Order(models.Model):
    # ONE TO MANY Statement (Statement history)
    # ONE TO ONE Customer (у ордера может быть только один кастамер)
    organization = models.ForeignKey(
        "main.Organization",
        on_delete=models.deletion.SET_NULL,
        related_name='organization_orders',
        null=True,
        blank=False
    )

    organization = models.ForeignKey(
        "main.Customer",
        on_delete=models.deletion.SET_NULL,
        related_name='customers_orders',
        null=True,
        blank=False
    )

    @property
    def statement_history(self):
        return self.order_statement_history.all()


class Organization(models.Model):
    # ONE TO MANY Research
    # ONE TO MANY Customer
    # ONE TO MANY Order
    # ONE TO ONE head of organization -> UserModel
    # ONE TO MANY employees -> UserModel
    name = models.CharField(
        max_length=255, null=False, blank=True
    )

    email = models.EmailField(
        max_length=255, null=False, blank=True
    )

    @property
    def researches(self) -> QuerySet[Research]:
        return self.organization_researches.all()

    @property
    def customer(self) -> QuerySet[Customer]:
        return self.organization_customers.all()

    @property
    def Order(self) -> QuerySet[Order]:
        return self.organization_orders.all()


# One to many
class Statement(models.Model):
    research = models.ForeignKey(
        "main.Research",
        on_delete=models.deletion.SET_NULL,
        related_name='research_statement_history',
        null=True,
        blank=False
    )

    order = models.ForeignKey(
        "main.Order",
        on_delete=models.deletion.SET_NULL,
        related_name='order_statement_history',
        null=True,
        blank=False
    )
