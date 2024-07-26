people = []

def add_person(person):
    people.append(person)



def remove_person(name):
    if name not in people:
        print()
        print("Siz adam atyn tuura emes jazdynyz!")
        print()
    else:
        people.remove(name)


def get_all():
    for i in range(len(people)):
        print(f'{i + 1}) {people[i]}')
        print()

def get_person(index):
    print()
    print(people[index - 1])
    print()

def get_persons_with_len(length=5):
    for person in people:
        if len(person) > length:
            print(person)



def main():
    while True:
        print("1) add")
        print("2) remove")
        print("3) get all")
        print("4) get person")
        print("5) get len person")
        print("6) exit")
        value = int(input("Bir variantty tandanyz:"))

        if value == 6:
            break
        elif value == 1:
            adam = input("Enter name: ")
            add_person(person=adam)
        elif value == 2:
            aty = input("Enter name:")
            remove_person(name=aty)
        elif value == 3:
            get_all()
        elif value == 4:
            ind = int(input("Enter index: "))
            get_person(index=ind)
        elif value == 5:
            length = int(input("Enter length: "))
            if length != 0:
                get_persons_with_len(length=length)
        else:
            print("Tuura variantty tandanyz!")
        
        
main()
    

