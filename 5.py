# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки,
# на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

def find_people(datahub=documents):
    number_input = input('Введите номер документа: ')
    for datas in datahub:
        if number_input == datas['number']:
            return datas['name']
    return f'Не верный номер документа'

def add_docs(docs=documents,dirct=directories):
    a = ["type", "number", "name"]
    new_doc = dict.fromkeys(a)
    type_key = input('Введите тип нового документа: ')
    number_key = input('Введите номер нового документа: ')
    name_key = input('Введите фамилию и имя владельца документа: ')
    number_of_directory = input('Введите номер полки, куда добавить документ')
    new_doc["type"] = type_key
    new_doc["number"] = number_key
    new_doc["name"] = name_key
    docs.append(new_doc)
    for key, values in dirct.items():
        if number_of_directory in key:
            values.append(number_key)
        else:
            return ('Такой полки не существует')

def find_shelf(data=directories):
    number_input = input('Введите номер документа: ')
    for key, value in data.items():
        if number_input in value:
            return f' Ваш документ на полке # {key}'
    return f'Не верный номер документа'

def print_list(data=documents):
    docs_list = ""
    for datas in data:
        docs_list += f'{datas["type"]} "{datas["number"]}" {datas["name"]}\n'
    return docs_list

def main():
  while True:
    user_input = input('Введите команду')
    if user_input == 'p':
      print(find_people())
    elif user_input == 's':
      print(find_shelf())
    elif user_input == 'l':
      print(print_list())
    elif user_input == 'a':
        print(add_docs())
    elif user_input == 'q':
      print('До свидания!')
      break


main()