'''
File: main.py
Description: demonstration script, show how system works by crea􀆟ng objects, invoking methods, and printing results.
Author: Le Tuan Mai
ID: 110439345
Username: maily015
This is my own work as defined by the University's Academic Integrity Policy.
'''

from zoo import Zoo
from zookeeper import Zookeeper
from veterinarian import Veterinarian
from mammal import Mammal
from reptile import Reptile
from enclosure import Enclosure


#Creating zoo
zoo = Zoo("Sydney Wildlife Park")
print("Created zoo:", zoo.name)

#Creating staff
zk = Zookeeper("Alice")
vet = Veterinarian("Bob")

#Add staff to zoo
zoo.add_staff(zk)
zoo.add_staff(vet)

#Using Find staff method
print("Displaying Staff in zoo...\n")
print(zoo.find_staff_by_name("Alice"))
print(zoo.find_staff_by_name("Bob"))

#Creating Enclosures
sav = Enclosure(300,"Savannah")
jung = Enclosure(300,"Jungle")

zoo.add_enclosure(sav)
zoo.add_enclosure(jung)

#Creating animal
leo = Mammal("Leo", "lion", 5, "Meat", "Savannah", True)
croc = Reptile("Croc", "Crocodile", 6, "Meat", "Jungle", True)

#Find animal by name
zoo.add_animal(leo)
zoo.add_animal(croc)

print("Finding animal by name:....\n", zoo.find_animal_by_name("Leo")[0])

#Add animal to their enclosure
sav.add_animal(leo)
jung.add_animal(croc)

print("Displaying Enclosure and its animal in zoo...")
print(zoo.find_enclosure_by_environment("Savannah")[0])
print(zoo.find_enclosure_by_environment("Jungle")[0])

#Assigning staff to animal / Enclosure
zk.assign_enclosure(sav)
zk.assign_enclosure(jung)
vet.assign_animal(leo)
vet.assign_animal(croc)
vet.display_animal()

#Run daily schedule
print("Performing daily tasks.... \n ")
zoo.run_full_daily_schedule()

#Create Health Record on unhealthy animal when doing health check
samba = Mammal("Samba", "lion", 5, "meat", "Savannah", False)
zoo.add_animal(samba)
sav.add_animal(samba)
vet.assign_animal(samba)
vet.generate_record(samba, True)


#Get records
print("\nPulling Records for animal undertreatment....\n")
zoo.animal_under_treatment()

for i in zoo.get_health_records_for_animal(samba):
    print(i)

#Heal animal and close records
vet.heal_animal(samba)
for i in zoo.get_health_records_for_animal(samba):
    print(i)

#deactive staff  and remove staff / animal from zoo
print(zoo)

zoo.remove_animal(samba)
zoo.remove_staff(zk)
print("After removed:...")
print(zoo)