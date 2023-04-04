from django.contrib import admin

from apps.main.models import Research, Customer, Order, Organization, Statement


@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    ...

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    ...

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ...

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    ...

@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    ...




