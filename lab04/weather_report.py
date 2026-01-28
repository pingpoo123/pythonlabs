from pathlib import Path
import file_reader 
#import weather_functions as wf
from weather_functions import *

# The file name is actually 'temperatur_data.csv' but added some extra path-stuff here  
# to make sure that it will be found by everyone
file_path = Path(__file__).parent / 'temperatur_data.csv'

#read month 2 temperatures from data.csv
#temp_list = file_reader.read_from_file(file_path, 1)

#avg_temp = sum(temp_list) / len(temp_list)
#print(format(avg_temp, '.2f'))
#print(format(calculate_avg_temp(temp_list), '.2f'))
#print(when_is_spring(temp_list))

menu_input = int(input('Vad vill du göra? Tryck 1 för medeltemperatur och 2 för vårens ankomst\n'))  
if menu_input == 1:
    month_input = int(input('Vilken månad vill du beräkna medeltemperaturen för? Ange månadsnummer\n'))
    if 1 <= month_input <= 12:
        temp_list = file_reader.read_from_file(file_path, month_input)
        print(f'Medeltemperaturen för månad {month_input} är {format(calculate_avg_temp(temp_list), '.2f')}')
    else:
        print('Ange ett giltigt månadsnummer.')
elif menu_input == 2:
    print('Letar efter våren...')
    for month in range(1,13):
        temp_list = file_reader.read_from_file(file_path, month)
        if when_is_spring(temp_list) != -1:
            break
    print(f'Våren infaller på dag {when_is_spring(temp_list) + 1} i månad {month}')
else:
    print('Tryck 1 eller 2')