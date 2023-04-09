from django.db import models

from commons.models import CreatedUpdatedMixin
from users.models import User


class TransactionInfo(CreatedUpdatedMixin):
    class ExpensesType(models.TextChoices):
        FOODS = 'Foods', 'Foods'
        GIFTS = 'Gifts', 'Gifts'
        MEDICAL = 'Medical', 'Medical'
        EXPENSES = 'Expenses', 'Expenses'
        HOME = 'Home', 'Home'
        TRANSPORTATION = 'Transportation', 'Transportation'
        PERSONAL = 'Personal expenses', 'Personal expenses'
        PETS = 'Pets', 'Pets'
        BILLS = 'bills', 'bills'
        TRIPS = 'Trips', 'Trips'
        DEBTS = 'Debts', 'Debts'
        OTHER = 'Other', 'Other'
        SERVICES = 'Services', 'Services'

    class RevenueType(models.TextChoices):
        SAVINGS = 'Savings', 'Savings'
        SALARY = 'Salary', 'Salary'
        BONUSES = 'Bonuses', 'Bonuses'
        INTERESTS = 'Interests', 'Interests'
        OTHER = 'Other', 'Other'

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=8, decimal_places=2)
    is_revenue = models.BooleanField(choices=((True, 'Revenue'), (False, 'Expenses')))
    revenue_type = models.CharField(max_length=32, choices=RevenueType.choices, null=True, blank=True)
    expenses_type = models.CharField(max_length=32, choices=ExpensesType.choices, null=True, blank=True)
    description = models.CharField(null=True, blank=True)

    class Meta:
        abstract = True


class Recurring(TransactionInfo):
    class RepeatType(models.TextChoices):
        WEEKLY = 'Weekly', 'Weekly'
        MONTHLY = 'Monthly', 'Monthly'
        ANNUALLY = 'Annually', 'Annually'

    until = models.DateField()
    repeat = models.CharField(max_length=16, choices=RepeatType.choices, null=True, blank=True)
    is_active = models.BooleanField(default=False)


class Transaction(TransactionInfo):
    pass
