import os
import os.path

import datetime
from datetime import date
from time import strftime


today = date.today()
h=datetime.datetime.now()
date=today.strftime("%d/%m/%Y")
heure=h.strftime("%H:%M")
source='heure.txt'

#test='python3 piant.py 5 1'
#os.system(test)
ouvre = 'python3 piant.py ouvre 35'
ferme = 'python3 piant.py ferme 35'
with open(source, 'r') as filin: 
	lines = filin.readlines()
	for line in lines:
		jour=(line.split()[1])
		if jour=="1er":
			jour=1
		if len(jour)=1:
			jour="0"+jour
		mois=(line.split()[2])
		leve=(line.split()[4])
		leve=leve.replace("h", ":")
		couche=(line.split()[5])
		couche=couche.replace("h", ":")

		if mois=="janvier":
			mois="01"
		elif mois== "février":
			mois="02"
		elif mois== "mars":
			mois="03"
		elif mois== "avril":
			mois="04"
		elif mois== "mai":
			mois="05"
		elif mois== "juin":
			mois="06"
		elif mois== "juillet":
			mois="07"
		elif mois== "août":
			mois="08"
		elif mois== "septembre":
			mois="09"
		elif mois== "octobre":
			mois="10"
		elif mois=="novembre":
			mois="11"
		elif mois== "décembre":
			mois="12"

		annee=(line.split()[3])

		datelu=(f"{jour}/{mois}/{annee}")
		print(datelu,date)

		if datelu==date:
			int_heure=int(heure.replace(":", ""))
			int_couche=int(couche.replace(":", ""))
			print(int_couche-100, int_heure)
			print(datelu,date)
			if heure==leve :
				os.system(ouvre)

			elif int_couche ==int_heure-100 :
				os.system(ferme)
				
