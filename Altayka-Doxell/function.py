

def summ_numbers_key():
    "Суммирование значений одинаковых ключей"
    my_dict = subcategory_dict
    my_dict['восп'] = sum(my_dict['восп'])
    my_dict['оп'] = sum(my_dict['оп'])
    my_dict['увп'] = sum(my_dict['увп'])
    my_dict['завед'] = sum(my_dict['завед'])
    my_dict['пр пп'] = sum(my_dict['пр пп'])
    print(my_dict)