# Initialize data set
AllowedVehicleList = [
    'Ford F-150', 'Chevolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra',
    'Nissan Titan'
]


#print menu
def print_menu():
  print("********************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("********************************")
  print(" Please Ender the following number below from the following menu:")
  print()
  print("1. PRINT all Allowed Vehicles")
  print("2. EXIT")


#print ALlowed Vehicles
def print_AllowedVehicles():
  print("AllowedVehicleList:")
  for vehicle in AllowedVehicleList:
    print(vehicle)


def main():
  print_menu()  #print menu on program start
  #loop to display vehicles on 1 or close on 2
  while True:
    choice = input("Enter your choice: ")
    if choice == "1":
      print(
          "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
      )
      print_AllowedVehicles()  #function to print vehicles
      print_menu()  #function to print menu
    elif choice == "2":
      print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
      break
    else:
      print("Enter a valid choice")
      print_menu()
    input()  #close menu after key press


if __name__ == "__main__":
  main()
