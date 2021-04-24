from django.db import models

from multiselectfield import MultiSelectField


pizza_type_choices = (
    ('1', ' Regular'),
    ('2', 'Square')
)

pizza_size_choices = (
    ('1', 'Small'),
    ('2','Medium'),
    ('3','Large')
)

pizza_toppings_choices = (
    ('1', 'Onion'),
    ('2',' Tomato'),
    ('3',' Corn'),
    ('4', 'Capsicum'),
    ('5', 'Cheese'),
    ('6','Jalapeno')
)

class Pizza(models.Model):
    pizza_type     = models.CharField(max_length=50, choices=pizza_type_choices)
    pizza_size     = MultiSelectField(choices=pizza_size_choices)
    pizza_toppings = MultiSelectField(choices=pizza_toppings_choices)

    REQUIRED_FIELDS = ['pizza_type', 'pizza_size','pizza_toppings']
    def __str__(self):
        p = int(self.pizza_type)    
        return str(pizza_type_choices[p-1][1])
