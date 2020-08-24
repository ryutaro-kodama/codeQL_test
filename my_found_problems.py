class DengerousDefaultValue:
    def __init__(self, my_list=[]):
        self.my_list = my_list

def my_default_value():
    dfb = DengerousDefaultValue()
    dfb.my_list.append('A')
    print(dfb.my_list)    # A

    dfb2 = DengerousDefaultValue()
    dfb2.my_list.append('B')
    print(dfb2.my_list)   # ここは？ -> ['A', 'B']

def my_default_global():
    i = 1
    def xxx(a = i):
        print(a)

    i = 2
    xxx()  # 1

def my_closure():
    list_of_printers = []
    for i in [1, 2, 3]:
        def printer():
            print(i)
        list_of_printers.append(printer)

    for func in list_of_printers:
        func()  # ここは？ -> 3 3 3

def my_list():
    my_list = [[0]*3]*3
    my_list[0][1] = 1
    print(my_list)  # [[0, 1, 0],[0, 1, 0],[0, 1, 0]]

    my_list2 = [[0]*3 for k in range(3)]
    my_list2[0][1] = 1
    print(my_list2)  # [[0, 1, 0],[0, 0, 0],[0, 0, 0]]

my_default_value()
my_default_global()
my_closure()
my_list()