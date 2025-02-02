from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    in_stock=models.BooleanField(default=True)



'''
    when we run migration it will convert from class to table
    CREATE TABLE myapp_item(
        'id' INTERGER NOT NULL PRIMARY KEY AUTOINCAREMENT,
        'name'VARCHAR(200) NOT NULL,
        'price'DECIMAL(4,2) NOT NULL

    )
'''
