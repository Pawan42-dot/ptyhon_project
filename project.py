info={ }

def add_contact(name,number):
    info[name]=number
    print("succesfully added")


def update_contact(name,number):
    if name in info:
        info[name]=number
        print("update succesfully")

    else:
        print("no  data found")

    
def view_contact():
    print(info)

def delete_contact(name):
    if name in info:
        del info[name]
        print("successfully deleted")

    else:
        print("no data found")

def main():
    while True :
        print("1.add_contact")
        print("2.update_contact")
        print("3.delete_contact")
        print("4.view_contact")

        choice=int(input("enter your choice 1-4 :"))

        if choice==1:
            name=input("enter name :")
            number=int(input("enter number :"))

            add_contact(name,number)

        elif choice==2:
            name=input("enter name: ")
            number=int(input("enter no :"))
            update_contact(name,number)
            


        elif choice==3:
            input("enter name :")
            delete_contact(name)
            break

        elif choice==4:
            view_contact()

        else:
            print("invalid input")

main()

