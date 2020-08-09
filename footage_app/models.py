from django.utils.timezone import now
from django.core.validators import MinValueValidator

from django.db import models


# Create your models here.
class Branch(models.Model):
    branch_id = models.CharField(max_length=4, primary_key=True)
    branch_name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.branch_id}" #| {self.branch_name}"


class Terminal(models.Model):
    terminal_id = models.CharField(max_length=4, primary_key=True)
    ip_address = models.CharField(max_length=15)
    terminal_name = models.CharField(max_length=30)
    branch_id = models.ForeignKey(Branch, on_delete=models.SET_DEFAULT, default='XXXX')
    # SET_DEFAULT changes value to default value specified if a branch is deleted
    def __str__(self):
        return f"{self.branch_id}{self.terminal_id}"#/ {self.ip_address}"


class Transaction(models.Model):
    terminal_id = models.ForeignKey(Terminal, on_delete=models.SET_DEFAULT, default='9999')
    card_id = models.CharField(max_length=6)
    card_pan = models.CharField(max_length=4)
    amount = models.PositiveIntegerField(default=1000, validators=[MinValueValidator(1000)])
    timestamp = models.DateTimeField(default=now, editable=False)
    trxn_success = models.BooleanField(default=True)
    
    def __str__(self):
        return f"ID: {self.terminal_id}, PAN: {self.card_pan}, AMT: N{self.amount}, {self.timestamp}"

    
    
   