calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    print(f"А это что за покемон?! '{string}'")

def is_contains(string, list_to_search):
    print(f"Проверяем наличие покемона '{string}' в списке {list_to_search}")
    
count_calls()
string_info('Ну привет!')
is_contains('белка', ['дерево', 'белка'])
count_calls()
is_contains('человек', ['выдра', 'человек'])
count_calls()

print(f"Количество вызовов: {calls}")