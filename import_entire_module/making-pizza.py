
'''
import pizza

pizza.make_pizza(16,'Tanduri hot')
pizza.make_pizza(18,'Chicken Roast', 'Sweet corn', 'Black olive', 'Meatballs')

'''
# CALL DIFFERENTLY - Using as to give a function an alias
'''
from pizza import make_pizza as mp
mp(16,'Tanduri hot')
mp(18,'Chicken Roast', 'Sweet corn', 'Black olive', 'Meatballs')
'''

# CALL DIFFERENTLY - Using as to give a module an alias

import pizza as p
p.make_pizza(16,'Tanduri hot')
p.make_pizza(18,'Chicken Roast', 'Sweet corn', 'Black olive', 'Meatballs')