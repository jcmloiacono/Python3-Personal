import re

nombre1="Sandra Lopez"
nombre2="Antonio Gomez"
nombre3="sandra Lopez"
nombre4="43356543"


if re.search("Sandra", nombre3, re.IGNORECASE):

	print("Hemos encontrado el nombre")

else:

	print ("no hemos encontrado el nombre")


if re.match(".andra", nombre3, re.IGNORECASE):

	print("Hemos encontrado el nombre")

else:

	print ("no hemos encontrado el nombre")


if re.match("\d", nombre4):

	print("Hemos encontrado el nombre")

else:

	print ("no hemos encontrado el nombre")