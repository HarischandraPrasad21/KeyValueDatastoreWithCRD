import json
import os


#Read funtion to read the value of key provided
def Read(file):
  with open(file) as f:
    res = json.load(f)
    key = input("enter the key to search: ")
    if key in res:
      print(key,":",res[key])
    else:
      raise Exception(key,"not found")
    # try:
    #   #if key is present in the file, it will print the key- value pair
    #
    #   print(key+" : "+res[key])
    # except:
    #   #if key if not present in the file, it will raise an exception
    #   raise Exception("Key Does not exist's")




inp = input("Are you Willing to provide the file path\nif YES enter y or Y Otherwise enter n or N : " )
if inp == "y" or inp == "Y":
  File_path = input( "please enter file path :")
  FN1 = File_path
  if os.path.getsize(FN1) > 0:
    pass
  else:
    fill = {}
    with open(FN1, 'w') as fi:
      fi.write(json.dumps(fill))
elif inp == "n" or inp == "N":
  #assinging a randon name for file to store data
  FN1="datastoreGHCP11.json"
  #checking for the file exits or not
  file_exits = os.path.exists(FN1)
  if not file_exits:
    f = open(FN1, "x")
    f.close()
  #checking file contains data or not
  with open(FN1) as my_file:

    my_file.seek(0)
    first_char = my_file.read(1)
    if not first_char:
      FileEmpty = True

    else:
      FileEmpty = False

  if FileEmpty == True:
    with open(FN1,"w") as my_file:
      data = {}
      my_file.write(json.dumps(data))
else:
  print("please select a valid option")



print()
print("<------------------ MENU --------------->")
print(" 1. Adding Elements To File \n 2. Read To File \n 3. Deleteing from file")
print("-----------------------------------------")
#based on the value of option, the adding, reading, and the del will be happen

option = int(input("enter Your Option: "))
if option == 1:
  # opening file and read
  with open(FN1,"r") as f:
    data = json.load(f)

  file_size = os.path.getsize(FN1)
  #checking for the non functional requriment that the file size is less than 1gb or not, if not it will raise an error
  if file_size > 1048576:
    raise Exception("file size exceeded more than 1 GB")
  Key = str(input("enter the key: "))
  IntString = "123468790"
  #inserting only string in data store
  isInt = True
  for i in range(len(Key)):
    if Key[i] in IntString:
      isInt = True
    else:
      isInt = False
      break
  if isInt == True:
    raise Exception("key must be a string, but "+Key+" is not a string")
  #if the key is alredy in file error is raised
  if Key in data:
    raise Exception(Key+" alredy exists in data store")
  Value = input("enter the value of key: ")
  data[Key] = Value
  with open(FN1,"w") as f:
    json.dump(data, f)



elif option == 2:
  Read(FN1)

elif option == 3:

  key = input("enter the key to remove from file: ")
  with open(FN1) as f:
    data = json.load(f)
  #deleting the specifed key from the file
  del data[key]
  with open(FN1,"w") as f:
    json.dump(data, f)


