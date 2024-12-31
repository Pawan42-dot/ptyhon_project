menue={ "pizza":100,
        "coffee":80,
        "maggie":60,
        "pasta":50,
        "momos":40 
}
# add more items on menue according to your choice

print(" welcome to python cafe")
print(" pizza:100\n coffee:80\n maggie:60\n pasta:50\n momos:40")

total=0
item=input("enter your order :")

def add_item(item,total):
    if item in menue:
        print("succesfully added")

    else:
          print("not available")

total+= menue[item]

while True:
  another_order=input("you can add more item yes/no:")
  if another_order=="yes":
   item2=input("enter your order :")
   if item2 in menue:
        print("sucesfully added")
     
   else:
         print("not available")

  elif another_order=="no":
      print("thank you")
      break
     
  else:
      print("invalid input")
      break

  total+= menue[item2]

print(f"you can pay Rs{total}")
