def vvod():
    return int(input("Введите элемент:"))

class Node:
    
    def __init__(self):
        self.value = None
        self.next = None

class SingleList:

    def __init__(self):
        self.head = Node()

    def list_print(self):
        if self.head.value is not None:
            print(self.head.value, end = " ")
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            print(current_node.value, end=" ")
        print()

    def del_element(self, value):
        temp = Node()
        current_node = self.head
        if self.head.value is None:
            print("Список пустой ")
            return
        elif (self.head.value == value) and (self.head.next is None):
            self.head.value = None
            print("Элемент ", value, " удален. Список пустой")
            return
        elif (self.head.value != value) and (self.head.next is None):
            print("Элемент не найден")
            return
        elif (self.head.value == value) and (self.head.next is not None):    
            self.head = self.head.next
            print("Элемент ", value, " удален")
            return
        temp = current_node.next
        while temp.value is not None:
            if temp.value == value:
                print("Элемент ", value, " удален")
                current_node.next = temp.next
                return
            current_node = current_node.next
            if temp.next is None:
                print("Элемент не найден")
                return
            temp = current_node.next

    def search_list(self, value):
        if self.head.value is None:
            print("Список пустой ")
            return
        elif (self.head.value == value) and (self.head.next is None):
            temp = Node()
            temp.value = int(input("Введите элемент который будем добавлять: "))
            current_node = self.head
            current_node.next = temp
            return
        temp = Node()
        current_node = self.head
        while current_node.value is not None:
            if current_node.value == value:
                temp.value = int(input("Введите элемент который будем добавлять: "))
                temp.next = current_node.next
                current_node.next = temp
                return
            if current_node.next is None:
                print("Элемент не найден")
                return
            current_node = current_node.next
        
    def addend(self, value):
        if self.head.value is None:
            self.head.value = value
            return
        temp = Node()
        temp.value = value
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = temp

    def addbegin(self, value):
        if self.head.value is None:
            self.head.value = value
            return
        temp = Node()
        temp.value = value
        temp.next = self.head
        self.head = temp

    def lenght(self):
        if self.head.value is None:
            size = 0
        else:
            size = 1
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            size += 1
        return size

help = '''
s - вставка элемента после какого-то элемента
b - добавление нового элемента в начало списка
e - добавление нового элемента в конец списка
d - удаление элемента из списка
w - вывод на экран всего списка
l - подсчет количества элементов в списке
q - выход
'''

ss = SingleList()
choice = ""
while choice != "q" and choice != "й":
    choice = input("(h - справка >>>) ")
    if choice == "b" or choice == "и": ss.addbegin(vvod())
    elif choice == "e" or choice == "у": ss.addend(vvod())
    elif choice == "w" or choice == "ц": ss.list_print()
    elif choice == "l" or choice == "д": print("Количество элементов списка:", ss.lenght())
    elif choice == "s" or choice == "ы": ss.search_list(vvod())
    elif choice == "d" or choice == "в": ss.del_element(vvod())
    elif choice == "h" or choice == "р": print(help)
