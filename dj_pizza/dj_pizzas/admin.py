# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from dj_pizzas.models import Topping, Dough, Pizza, OrderedToppings, Snacks, OrderedSnacks, Order, OrderPayment, Person, ClientAccount, ClientAccountPerson, Employee, ClientTransaction
from examplemodel.models import ExampleModel1, ExampleModel2, ExampleModel3, ExampleModel4, ExampleModel5

admin.site.register(Order)
admin.site.register(Topping)
admin.site.register(Dough)
admin.site.register(OrderedToppings)
admin.site.register(Pizza)
admin.site.register(Snacks)
admin.site.register(OrderedSnacks)
admin.site.register(OrderPayment)
admin.site.register(Person)
admin.site.register(ClientAccount)
admin.site.register(ClientAccountPerson)
admin.site.register(Employee)
admin.site.register(ClientTransaction)

admin.site.register(ExampleModel1)
admin.site.register(ExampleModel2)
admin.site.register(ExampleModel3)
admin.site.register(ExampleModel4)
admin.site.register(ExampleModel5)