import os
from datetime import date

fecha = date.today()
date =("{}_{}_{}_pywombat.txt".format(fecha.day,fecha.strftime("%b"), fecha.year))
print (date)
file = open(date, "w")
file.close()