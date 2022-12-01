'''Wide search algorithm'''
from collections import deque

graph = {
    'Iaroslav': ['Vladimir', 'Andrew', 'Svetlana'],
    'Vladimir': ['Karina', 'Vovchik'],
    'Andrew': ['Kirill'],
    'Svetlana': ['Vovchik'],
    'Karina': [],
    'Vovchik': [],
    'Kirill': []
}


def person_is_seller(name):
    return name == 'Kirill'


def wide_search(name):
    queue = deque()
    queue += graph[name]
    checked = []
    print(queue)
    while queue:
        person = queue.popleft()
        if not person in checked:
            print(person)
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                queue += graph[person]
                checked.append(person)
    return print('There are no mango seller among your friends!')


print(wide_search('Iaroslav'))
