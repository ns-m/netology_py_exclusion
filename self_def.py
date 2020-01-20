import csv

flats_list = list()

with open('output.csv', encoding='utf-8', newline='') as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)

# можете посмотреть содержимое файла с квартирами через print, можете - на вкладке output.csv
# print (flats_list)



# 1) Напишите цикл, который проходит по всем квартирам, и показывает только новостройки
# и их порядковые номера в файле. Подсказка - вам нужно изменить этот код:
new_home_count = 0
serial_number = [idx for idx, value in enumerate(flats_list) if value[2] == "новостройка"]
serial_num_ind = 0
for flat in flats_list:
    if "новостройка" in flat:
        # print(f"{serial_number[serial_num_ind]} ID: {flat[0]}")
        new_home_count += 1
        serial_num_ind += 1
# print(f"Всего новостроек: {new_home_count}")
# 2) добавьте в код подсчет количества новостроек

# print("--------------------------------")

# 1) Сделайте описание квартиры в виде словаря, а не списка. Используйте следующие поля из файла output.csv: ID, Количество комнат;Новостройка/вторичка, Цена (руб). У вас должно получиться примерно так:

# 2) Измените код, который создавал словарь для поиска квартир по метро так, чтобы значением словаря был не список ID квартир, а список описаний квартир в виде словаря, который вы сделали в п.1 
header = flats_list.pop(0)
subway_dict = {}
for flat in flats_list:
    subway = flat[3].replace("м.", "")
    flat_info = {"id": flat[0], "rooms": flat[1], "type": flat[2], "price": flat[11]}
    if subway not in subway_dict.keys():
        subway_dict[subway] = list()
    subway_dict[subway].append(flat_info)
# print(subway_dict, type(subway_dict))

# print("--------------------------------")
# 3) Самостоятельно напишите код, который подсчитывает и выводит, сколько квартир нашлось у каждого метро.
subway_apartment = 1
subway_dict2 = {}
for flat in flats_list:
    subway2 = flat[3].replace("м.", "")
    subway_dict2.setdefault(subway2, [])
    subway_dict2[subway2].append(subway_apartment)
subway_apartment_count = {key: len(val) for key, val in subway_dict2.items()}
subway_apartment_count['Не у метро'] = subway_apartment_count.pop('')
# for subway in subway_apartment_count:
    # print(f"Метро: {subway} - Количество квартир: {subway_apartment_count.get(subway)}")

print("--------------------------------")
def key_error():
  try:
    subway_dict['name']
  except KeyError:
    print('Поле "name" у документа отсутствует!')
key_error()