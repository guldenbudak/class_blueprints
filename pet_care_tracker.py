pet_list = []


class Pet:
    def __init__(self, user_name, pet_name, pet_type, energy=0, hunger=0):
        self.user_name = user_name
        self.pet_name = pet_name
        self.pet_type = pet_type
        self.energy = energy
        self.hunger = hunger

    def pet_feeding(self,hunger):
        if self.hunger <= 75:
            self.hunger += 25
            print(f"{self.pet_name} has hunger {self.hunger} ")
        else:
            print("Hunger is at its maximum level.")

    def pet_bedtime(self, energy):
        if self.energy <= 50:
            self.energy += 50
            print(f"{self.pet_name} has energy {self.energy} ")
        else:
            print("Energy is at its maximum level.")

    def pet_playtime(self, energy, hunger):
        if self.hunger <= 25 and self.energy <= 25:
            print("Hunger and energy makes playing games unsuitable.")

        elif self.hunger >= 25 and self.energy >= 25:
            self.energy -= 25
            self.hunger -= 25
            print(f"{self.pet_name} has hunger {self.hunger} and energy {self.energy} ")


while True:
    print("Welcome to the pet game .")
    print("1- Pet adding")
    print("2- Pet feeding")
    print("3- Pet bedtime")
    print("4- Pet playtime")
    print("5- Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        user_name = input("Enter your name: ")
        pet_name = input("Enter your pet name: ")
        pet_type = input("Enter your pet type: ")
        for pet in pet_list:
            if pet.user_name == user_name and pet.pet_name == pet_name and pet.pet_type == pet_type:
                print("Already have that pet", pet.pet_name)
                break
        else:
            pet_added = Pet(user_name=user_name, pet_name=pet_name, pet_type=pet_type)
            pet_list.append(pet_added)
            print(
                f"Hello {pet_added.user_name} your {pet_added.pet_type} {pet_added.pet_name} Added to the game system: your pet's energy is 0 and its hunger level is 0.")

    elif choice == "2":
        user_name = input("Enter your name: ")
        pet_name = input("Enter your pet name: ")
        pet_type = input("Enter your pet type: ")
        for pet in pet_list:
            if pet.user_name == user_name and pet.pet_name == pet_name and pet.pet_type == pet_type:
                pet.pet_feeding(pet.hunger)
                break
        else:
            print("Please try again, your pet did not match.")

    elif choice == "3":
        user_name = input("Enter your name: ")
        pet_name = input("Enter your pet name: ")
        pet_type = input("Enter your pet type: ")
        for pet in pet_list:
            if pet.user_name == user_name and pet.pet_name == pet_name and pet.pet_type == pet_type:
                pet.pet_bedtime(pet.hunger)
                break
        else:
            print("Please try again, your pet did not match.")

    elif choice == "4":
        user_name = input("Enter your name: ")
        pet_name = input("Enter your pet name: ")
        pet_type = input("Enter your pet type: ")
        for pet in pet_list:
            if pet.user_name == user_name and pet.pet_name == pet_name and pet.pet_type == pet_type:
                pet.pet_playtime(pet.hunger,pet.energy)
                break
        else:
            print("Please try again, your pet did not match.")

    elif choice == "5":
        print("Thank you for using the pet play system. We hope to see you again soon.")
        break
