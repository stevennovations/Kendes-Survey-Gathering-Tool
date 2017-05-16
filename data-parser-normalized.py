import numpy as np
import pandas as pd

data = pd.read_csv('kansei-profile-design.csv', sep=',', header=0)

data_convert = data['relax_refresh']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['relax_refresh'] = data_convert.astype(int)

data_convert = data['cool_impress']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['cool_impress'] = data_convert.astype(int)

data_convert = data['light_interest']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['light_interest'] = data_convert.astype(int)

data_convert = data['mystery_elegant']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['mystery_elegant'] = data_convert.astype(int)

data_convert = data['classic_creative']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['classic_creative'] = data_convert.astype(int)

data_convert = data['sexy_chic']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['sexy_chic'] = data_convert.astype(int)

data_convert = data['klasiko_malikhain']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['klasiko_malikhain'] = data_convert.astype(int)

data_convert = data['fun_boring']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['fun_boring'] = data_convert.astype(int)

data_convert = data['M_F']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['M_F'] = data_convert.astype(int)

data_convert = data['pretty_adorable']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['pretty_adorable'] = data_convert.astype(int)

data_convert = data['beauty_cute']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['beauty_cute'] = data_convert.astype(int)

data_convert = data['child_profe']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['child_profe'] = data_convert.astype(int)

data_convert = data['calm_live']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['calm_live'] = data_convert.astype(int)

data_convert = data['masikip_maayos']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['masikip_maayos'] = data_convert.astype(int)

data_convert = data['simple_luxury']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['simple_luxury'] = data_convert.astype(int)

data_convert = data['crowded_neat']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['crowded_neat'] = data_convert.astype(int)

data_convert = data['plain_sopshiticated']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['plain_sopshiticated'] = data_convert.astype(int)

data_convert = data['comfort_style']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['comfort_style'] = data_convert.astype(int)

data_convert = data['oldf_future']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['oldf_future'] = data_convert.astype(int)

data_convert = data['gorgeous_charm']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['gorgeous_charm'] = data_convert.astype(int)

data_convert = data['masaya_nakakabagot']

for index in range(len(data_convert)):
 	if (data_convert[index] == 1 or data_convert[index] == 2):
 		data_convert[index] = -1
 	elif (data_convert[index] == 3):
 		data_convert[index] = 0
 	elif (data_convert[index] == 4 or data_convert[index] == 5):
 		data_convert[index] = 1

data['masaya_nakakabagot'] = data_convert.astype(int)

data_convert = data['birthdate']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 18) / float(24 - 18)
		data_convert[index] = normalized

data['birthdate'] = data_convert

#COLLEGE
#CCS = 0
#CLA = 1
#COB = 2
#COE = 3
#COS = 4
#SOE = 5
#CED = 6

data_convert = data['college']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(6 - 0)
		data_convert[index] = normalized

data['college'] = data_convert

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
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(2 - 0)
		data_convert[index] = normalized

data['device'] = data_convert

#HOBBIES
#ART = 0
#SPORTS = 1
#TECH = 2
#TECHConsumer = 3
#TECHCreator = 4
#LITERATURE = 5
#SOCIAL = 6

data_convert = data['hobbies']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(6 - 0)
		data_convert[index] = normalized

data['hobbies'] = data_convert

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
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(2 - 0)
		data_convert[index] = normalized

data['shopnumber'] = data_convert

#SHOPHOURS
#none = 0
#1-2hours = 1
#3-4hours = 2
#5 above = 3

data_convert = data['shophours']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(3 - 0)
		data_convert[index] = normalized

data['shophours'] = data_convert

#SHOPITEMS
#none = 0
#1-10items = 1
#11-20items = 2
#above 20 = 3

data_convert = data['shopitems']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(3 - 0)
		data_convert[index] = normalized

data['shopitems'] = data_convert

#PRODUCTS
#apparel = 0
#footwear = 1
#accessories = 2

data_convert = data['products']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(2 - 0)
		data_convert[index] = normalized

data['products'] = data_convert

#PRICE
#below = 0
#average = 1
#above = 2

data_convert = data['price']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(2 - 0)
		data_convert[index] = normalized

data['price'] = data_convert

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

#HEADER COLOR

data['header_color'] = data['header_color'].str.replace('#', '')

red_frame = data['header_color'].astype(str)
green_frame = data['header_color'].astype(str)
blue_frame = data['header_color'].astype(str)

for index in range(len(red_frame)):
	red_channel = red_frame[index][:2]
	red_channel = int(red_channel, 16)
	red_frame[index] = red_channel

red_frame = red_frame.astype('float64')

for index in range(len(red_frame)):
	red_frame[index] = red_frame[index] / 255

data['header_color_red'] = red_frame

for index in range(len(green_frame)):
	green_channel = green_frame[index][2:-2]
	green_channel = int(green_channel, 16)
	green_frame[index] = green_channel

green_frame = green_frame.astype('float64')

for index in range(len(green_frame)):
	green_frame[index] = green_frame[index] / 255

data['header_color_green'] = green_frame

for index in range(len(blue_frame)):
	blue_channel = blue_frame[index][-2:]
	blue_channel = int(blue_channel, 16)
	blue_frame[index] = blue_channel

blue_frame = blue_frame.astype('float64')

for index in range(len(blue_frame)):
	blue_frame[index] = blue_frame[index] / 255

data['header_color_blue'] = blue_frame

#HEADER FONT COLOR

data['header_font_color'] = data['header_font_color'].str.replace('#', '')

red_frame = data['header_font_color'].astype(str)
green_frame = data['header_font_color'].astype(str)
blue_frame = data['header_font_color'].astype(str)

for index in range(len(red_frame)):
	red_channel = red_frame[index][:2]
	red_channel = int(red_channel, 16)
	red_frame[index] = red_channel

red_frame = red_frame.astype('float64')

for index in range(len(red_frame)):
	red_frame[index] = red_frame[index] / 255

data['header_font_color_red'] = red_frame

for index in range(len(green_frame)):
	green_channel = green_frame[index][2:-2]
	green_channel = int(green_channel, 16)
	green_frame[index] = green_channel

green_frame = green_frame.astype('float64')

for index in range(len(green_frame)):
	green_frame[index] = green_frame[index] / 255

data['header_font_color_green'] = green_frame

for index in range(len(blue_frame)):
	blue_channel = blue_frame[index][-2:]
	blue_channel = int(blue_channel, 16)
	blue_frame[index] = blue_channel

blue_frame = blue_frame.astype('float64')

for index in range(len(blue_frame)):
	blue_frame[index] = blue_frame[index] / 255

data['header_font_color_blue'] = blue_frame

#BUTTON BG COLOR

data['button_bg_color'] = data['button_bg_color'].str.replace('#', '')

red_frame = data['button_bg_color'].astype(str)
green_frame = data['button_bg_color'].astype(str)
blue_frame = data['button_bg_color'].astype(str)

for index in range(len(red_frame)):
	red_channel = red_frame[index][:2]
	red_channel = int(red_channel, 16)
	red_frame[index] = red_channel

red_frame = red_frame.astype('float64')

for index in range(len(red_frame)):
	red_frame[index] = red_frame[index] / 255

data['button_bg_color_red'] = red_frame

for index in range(len(green_frame)):
	green_channel = green_frame[index][2:-2]
	green_channel = int(green_channel, 16)
	green_frame[index] = green_channel

green_frame = green_frame.astype('float64')

for index in range(len(green_frame)):
	green_frame[index] = green_frame[index] / 255

data['button_bg_color_green'] = green_frame

for index in range(len(blue_frame)):
	blue_channel = blue_frame[index][-2:]
	blue_channel = int(blue_channel, 16)
	blue_frame[index] = blue_channel

blue_frame = blue_frame.astype('float64')

for index in range(len(blue_frame)):
	blue_frame[index] = blue_frame[index] / 255

data['button_bg_color_blue'] = blue_frame

#BUTTON FONT COLOR

data['button_font_color'] = data['button_font_color'].str.replace('#', '')

red_frame = data['button_font_color'].astype(str)
green_frame = data['button_font_color'].astype(str)
blue_frame = data['button_font_color'].astype(str)

for index in range(len(red_frame)):
	red_channel = red_frame[index][:2]
	red_channel = int(red_channel, 16)
	red_frame[index] = red_channel

red_frame = red_frame.astype('float64')

for index in range(len(red_frame)):
	red_frame[index] = red_frame[index] / 255

data['button_font_color_red'] = red_frame

for index in range(len(green_frame)):
	green_channel = green_frame[index][2:-2]
	green_channel = int(green_channel, 16)
	green_frame[index] = green_channel

green_frame = green_frame.astype('float64')

for index in range(len(green_frame)):
	green_frame[index] = green_frame[index] / 255

data['button_font_color_green'] = green_frame

for index in range(len(blue_frame)):
	blue_channel = blue_frame[index][-2:]
	blue_channel = int(blue_channel, 16)
	blue_frame[index] = blue_channel

blue_frame = blue_frame.astype('float64')

for index in range(len(blue_frame)):
	blue_frame[index] = blue_frame[index] / 255

data['button_font_color_blue'] = blue_frame

#HEADER FONT WEIGHT

data_convert = data['header_font_weight']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 500) / float(700 - 500)
		data_convert[index] = normalized

data['header_font_weight'] = data_convert

#TOP BOTTOM PADDING

data_convert = data['top_bottom_padding']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(24 - 0)
		data_convert[index] = normalized

data['top_bottom_padding'] = data_convert

#LEFT RIGHT PADDING

data_convert = data['left_right_padding']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(24 - 0)
		data_convert[index] = normalized

data['left_right_padding'] = data_convert

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
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(2 - 0)
		data_convert[index] = normalized

data['text_size'] = data_convert

#TOP BOTTOM MARGIN

data_convert = data['top_bottom_margin']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 8) / float(24 - 8)
		data_convert[index] = normalized

data['top_bottom_margin'] = data_convert

#LEFT RIGHT MARGIN

data_convert = data['left_right_margin']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 8) / float(24 - 8)
		data_convert[index] = normalized

data['left_right_margin'] = data_convert

#BORDER RADIUS

data_convert = data['border_radius']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(25 - 0)
		data_convert[index] = normalized

data['border_radius'] = data_convert

#FONT SERIF
#Slabo 27px = 0
#Roboto Slab = 1
#Merriweather = 2

data_convert = data['font_serif']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(2 - 0)
		data_convert[index] = normalized

data['font_serif'] = data_convert

#FONT SANS SERIF
#Open Sans = 0
#Roboto = 1
#Lato = 2

data_convert = data['font_sans_serif']
data_convert = data_convert.astype('float64') 

for index in range(len(data_convert)):
		value = data_convert[index]
		normalized = float(value - 0) / float(2 - 0)
		data_convert[index] = normalized

data['font_sans_serif'] = data_convert

print(data)

kanseiprofiledesign = ['relax_refresh', 'cool_impress', 'light_interest', 'mystery_elegant', 'classic_creative', 'sexy_chic', 'klasiko_malikhain', 'fun_boring', 'M_F', 'pretty_adorable', 'beauty_cute', 'child_profe', 'calm_live', 'masikip_maayos', 'simple_luxury', 'crowded_neat', 'plain_sopshiticated', 'comfort_style', 'oldf_future', 'gorgeous_charm', 'masaya_nakakabagot', 'birthdate', 'college', 'gender', 'highschool1', 'highschool2', 'device', 'hobbies', 'primaryshop', 'shopnumber', 'shophours', 'shopitems', 'products', 'price', 'designorfunctionality', 'homepage', 'header_color_red', 'header_color_green', 'header_color_blue', 'header_font_color_red', 'header_font_color_green', 'header_font_color_blue', 'header_font_weight', 'header_letter_spacing', 'top_bottom_padding', 'left_right_padding', 'text_align', 'text_size', 'top_bottom_margin', 'left_right_margin', 'border_radius', 'button_bg_color_red', 'button_bg_color_green', 'button_bg_color_blue', 'button_font_color_red', 'button_font_color_green', 'button_font_color_blue', 'font_serif', 'font_sans_serif']
data.to_csv('normalized.csv', sep=',', columns=kanseiprofiledesign)

#kanseidesign = ['userid', 'relax_refresh', 'cool_impress', 'light_interest', 'mystery_elegant', 'classic_creative', 'sexy_chic', 'klasiko_malikhain', 'fun_boring', 'M_F', 'pretty_adorable', 'beauty_cute', 'child_profe', 'calm_live', 'masikip_maayos', 'simple_luxury', 'crowded_neat', 'plain_sopshiticated', 'comfort_style', 'oldf_future', 'gorgeous_charm', 'masaya_nakakabagot', 'header_color', 'header_font_color', 'header_font_weight', 'header_letter_spacing', 'top_bottom_padding', 'left_right_padding', 'text_align', 'text_size', 'top_bottom_margin', 'left_right_margin', 'border_radius', 'button_bg_color', 'button_font_color', 'font_serif', 'font_sans_serif']
#data.to_csv('kansei+design.csv', sep=',', columns=kanseidesign)

#kanseiprofile = ['websitid', 'relax_refresh', 'cool_impress', 'light_interest', 'mystery_elegant', 'classic_creative', 'sexy_chic', 'klasiko_malikhain', 'fun_boring', 'M_F', 'pretty_adorable', 'beauty_cute', 'child_profe', 'calm_live', 'masikip_maayos', 'simple_luxury', 'crowded_neat', 'plain_sopshiticated', 'comfort_style', 'oldf_future', 'gorgeous_charm', 'masaya_nakakabagot', 'birthdate', 'college', 'gender', 'highschool1', 'highschool2', 'device', 'hobbies', 'primaryshop', 'shopnumber', 'shophours', 'shopitems', 'products', 'price', 'designorfunctionality', 'homepage']
#data.to_csv('kansei+profile.csv', sep=',', columns=kanseiprofile)

#profiledesign = ['kanseitb_idkanseitb', 'birthdate', 'college', 'gender', 'highschool1', 'highschool2', 'device', 'hobbies', 'primaryshop', 'shopnumber', 'shophours', 'shopitems', 'products', 'price', 'designorfunctionality', 'homepage', 'header_color', 'header_font_color', 'header_font_weight', 'header_letter_spacing', 'top_bottom_padding', 'left_right_padding', 'text_align', 'text_size', 'top_bottom_margin', 'left_right_margin', 'border_radius', 'button_bg_color', 'button_font_color', 'font_serif', 'font_sans_serif']
#data.to_csv('profile+design.csv', sep=',', columns=profiledesign)