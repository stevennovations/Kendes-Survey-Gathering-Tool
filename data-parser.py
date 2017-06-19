import numpy as np
import pandas as pd
import datetime as dateT
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

data = pd.read_csv('master-file.csv', sep=',', header=0)

#
#USER PROFILES
#

#BIRTHDATE
#Converted to Age

data_convert = data['birthdate']

for index in range(len(data_convert)):
	value = dateT.datetime.strptime(data_convert[index], '%d/%m/%Y')
	data_convert[index] = calculate_age(value)

data['birthdate'] = data_convert.astype(int)

#COLLEGE
#CCS = 0
#CLA = 1
#COB = 2
#COE = 3
#COS = 4
#SOE = 5
#CED = 6

data_convert = data['college']

for index in range(len(data_convert)):
	if (data_convert[index] == 'CCS'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'CLA'):
		data_convert[index] = '1'
	elif (data_convert[index] == 'COB'):
		data_convert[index] = '2'
	elif (data_convert[index] == 'COE'):
		data_convert[index] = '3'
	elif (data_convert[index] == 'COS'):
		data_convert[index] = '4'
	elif (data_convert[index] == 'SOE'):
		data_convert[index] = '5'
	elif (data_convert[index] == 'CED'):
		data_convert[index] = '6'

data['college'] = data_convert.astype(int)

#GENDER
#M = 0
#F = 1

data_convert = data['gender']

for index in range(len(data_convert)):
	if (data_convert[index] == 'M'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'F'):
		data_convert[index] = '1'

data['gender'] = data_convert.astype(int)

#HIGHSCHOOL1
#PRIVATE = 0
#PUBLIC = 1

data_convert = data['highschool1']

for index in range(len(data_convert)):
	if (data_convert[index] == 'PRIVATE'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'PUBLIC'):
		data_convert[index] = '1'

data['highschool1'] = data_convert.astype(int)

#HIGHSCHOOL2
#Co-ed = 0
#Exclusive (All boys/girls) = 1

data_convert = data['highschool2']

for index in range(len(data_convert)):
	if (data_convert[index] == 'Co-ed'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'Exclusive (All boys/girls)'):
		data_convert[index] = '1'

data['highschool2'] = data_convert.astype(int)

#DEVICE
#MOB = 0
#PC = 1
#TAB = 2

data_convert = data['device']

for index in range(len(data_convert)):
	if (data_convert[index] == 'MOB'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'PC'):
		data_convert[index] = '1'
	elif (data_convert[index] == 'TAB'):
		data_convert[index] = '2'

data['device'] = data_convert.astype(int)

#HOBBIES
#ART = 0
#SPORTS = 1
#TECH = 2
#TECHConsumer = 3
#TECHCreator = 4
#LITERATURE = 5
#SOCIAL = 6

data_convert = data['hobbies']

for index in range(len(data_convert)):
	if (data_convert[index] == 'ART'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'SPORTS'):
		data_convert[index] = '1'
	elif (data_convert[index] == 'TECH'):
		data_convert[index] = '2'
	elif (data_convert[index] == 'TECHConsumer'):
		data_convert[index] = '3'
	elif (data_convert[index] == 'TECHCreator'):
		data_convert[index] = '4'
	elif (data_convert[index] == 'LITERATURE'):
		data_convert[index] = '5'
	elif (data_convert[index] == 'SOCIAL'):
		data_convert[index] = '6'

data['hobbies'] = data_convert.astype(int)

#PRIMARYSHOP
#Retail Store = 0
#Online = 1

data_convert = data['primaryshop']

for index in range(len(data_convert)):
	if (data_convert[index] == 'Retail Store'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'Online'):
		data_convert[index] = '1'

data['primaryshop'] = data_convert.astype(int)

#SHOPNUMBER
#1-3 websites = 0
#3-6 websites = 1
#7 above = 2

data_convert = data['shopnumber']

for index in range(len(data_convert)):
	if (data_convert[index] == '1-3 websites'):
		data_convert[index] = '0'
	elif (data_convert[index] == '3-6 websites'):
		data_convert[index] = '1'
	elif (data_convert[index] == '7 above'):
		data_convert[index] = '2'

data['shopnumber'] = data_convert.astype(int)

#SHOPHOURS
#none = 0
#1-2hours = 1
#3-4hours = 2
#5 above = 3

data_convert = data['shophours']

for index in range(len(data_convert)):
	if (data_convert[index] == 'none'):
		data_convert[index] = '0'
	elif (data_convert[index] == '1-2hours'):
		data_convert[index] = '1'
	elif (data_convert[index] == '3-4hours'):
		data_convert[index] = '2'
	elif (data_convert[index] == '5 above'):
		data_convert[index] = '3'

data['shophours'] = data_convert.astype(int)

#SHOPITEMS
#none = 0
#1-10items = 1
#11-20items = 2
#above 20 = 3

data_convert = data['shopitems']

for index in range(len(data_convert)):
	if (data_convert[index] == 'none'):
		data_convert[index] = '0'
	elif (data_convert[index] == '1-10items'):
		data_convert[index] = '1'
	elif (data_convert[index] == '11-20items'):
		data_convert[index] = '2'
	elif (data_convert[index] == 'above 20'):
		data_convert[index] = '3'

data['shopitems'] = data_convert.astype(int)

#PRODUCTS
#apparel = 0
#footwear = 1
#accessories = 2

data_convert = data['products']

for index in range(len(data_convert)):
	if (data_convert[index] == 'apparel'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'footwear'):
		data_convert[index] = '1'
	elif (data_convert[index] == 'accessories'):
		data_convert[index] = '2'

data['products'] = data_convert.astype(int)

#PRICE
#below = 0
#average = 1
#above = 2

data_convert = data['price']

for index in range(len(data_convert)):
	if (data_convert[index] == 'below'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'average'):
		data_convert[index] = '1'
	elif (data_convert[index] == 'above'):
		data_convert[index] = '2'

data['price'] = data_convert.astype(int)

#DESIGNORFUNCTIONALITY
#design = 0
#functionality = 1

data_convert = data['designorfunctionality']

for index in range(len(data_convert)):
	if (data_convert[index] == 'design'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'functionality'):
		data_convert[index] = '1'

data['designorfunctionality'] = data_convert.astype(int)

#HOMEPAGE
#simple = 0
#detailed = 1

data_convert = data['homepage']

for index in range(len(data_convert)):
	if (data_convert[index] == 'simple'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'detailed'):
		data_convert[index] = '1'

data['homepage'] = data_convert.astype(int)

#
#WEBSITE VALUES
#

#TEXT ALIGN
#Left = 0
#Right = 1

data_convert = data['text_align']

for index in range(len(data_convert)):
	if (data_convert[index] == 'Left'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'Right'): 
		data_convert[index] = '1'

data['text_align'] = data_convert.astype(int)

#TEXT SIZE
#Small = 0
#Medium = 1
#Large = 2

data_convert = data['text_size']

for index in range(len(data_convert)):
	if (data_convert[index] == 'Small'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'Medium'): 
		data_convert[index] = '1'
	elif (data_convert[index] == 'Large'): 
		data_convert[index] = '2'

data['text_size'] = data_convert.astype(int)

#FONT SERIF
#Slabo 27px = 0
#Roboto Slab = 1
#Merriweather = 2

data_convert = data['font_serif']

for index in range(len(data_convert)):
	if (data_convert[index] == 'Slabo 27px'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'Roboto Slab'): 
		data_convert[index] = '1'
	elif (data_convert[index] == 'Merriweather'): 
		data_convert[index] = '2'

data['font_serif'] = data_convert.astype(int)

#FONT SANS SERIF
#Open Sans = 0
#Roboto = 1
#Lato = 2

data_convert = data['font_sans_serif']

for index in range(len(data_convert)):
	if (data_convert[index] == 'Open Sans'):
		data_convert[index] = '0'
	elif (data_convert[index] == 'Roboto'): 
		data_convert[index] = '1'
	elif (data_convert[index] == 'Lato'): 
		data_convert[index] = '2'

data['font_sans_serif'] = data_convert.astype(int)

print(data)

kanseiprofiledesign = ['relax_refresh', 'cool_impress', 'light_interest', 'mystery_elegant', 'classic_creative', 'sexy_chic', 'klasiko_malikhain', 'fun_boring', 'M_F', 'pretty_adorable', 'beauty_cute', 'child_profe', 'calm_live', 'masikip_maayos', 'simple_luxury', 'crowded_neat', 'plain_sopshiticated', 'comfort_style', 'oldf_future', 'gorgeous_charm', 'masaya_nakakabagot', 'birthdate', 'college', 'gender', 'highschool1', 'highschool2', 'device', 'hobbies', 'primaryshop', 'shopnumber', 'shophours', 'shopitems', 'products', 'price', 'designorfunctionality', 'homepage', 'header_color', 'header_font_color', 'header_font_weight', 'header_letter_spacing', 'top_bottom_padding', 'left_right_padding', 'text_align', 'text_size', 'top_bottom_margin', 'left_right_margin', 'border_radius', 'button_bg_color', 'button_font_color', 'font_serif', 'font_sans_serif']
data.to_csv('kansei-profile-design.csv', sep=',', columns=kanseiprofiledesign)