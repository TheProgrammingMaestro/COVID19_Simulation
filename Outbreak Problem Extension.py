import random
class Person:
    def __init__(self, ID):
        self.friends = []
        self.status = False
        self.ID = ID
    def __str__(self):
        return str(self.status)

class Community:
    def __init__(self, peoplenum):
        self.people = []
        for i in range(0, peoplenum):
            self.people.append(Person(i))         
    def addFriends(self, person0, person1):
        self.people[person0].friends.append(self.people[person1])
        self.people[person1].friends.append(self.people[person0])
    def outbreak(self, virus_person):
        self.people[virus_person].status = True
        for i in range(0, len(self.people[virus_person].friends)):
            random_num = random.randint(1,3)
            if not self.people[virus_person].friends[i].status and random_num == 1:
                self.outbreak(self.people[virus_person].friends[i].ID)
    def death(self):
        i = 0
        while i < len(self.people):
            random_deathnum = random.randint(1,5)
            if self.people[i].status == True and (random_deathnum == 1 or random_deathnum == 2):
                for j in range(0, len(self.people[i].friends)):
                    self.people[i].friends[j].friends.remove(self.people[i])
                self.people.remove(self.people[i])
                print("Person", self.people[i].ID, "died for being a nerd")
                i -= 1
            i += 1
    def recovery(self):
        for i in range(0, len(self.people)):
            random_recovnum = random.randint(1,5)
            if self.people[i].status == True and (random_recovnum == 1 or random_recovnum == 2):
                self.people[i].status = False
                print("Person", self.people[i].ID, "recovered because they're an epic gamer.")
    def __str__(self):
        status_string = ""
        for i in range(0, len(self.people)):
            status_string += "Person "  + str(self.people[i].ID) + ":" + str(self.people[i].status) + "\n"
        return status_string
community = Community(9)
community.addFriends(0,1)
community.addFriends(1,2)
community.addFriends(1,5)
community.addFriends(2,6)
community.addFriends(3,6)
community.addFriends(4,5)
community.addFriends(4,7)
community.addFriends(5,6)
community.addFriends(6,8)
community.addFriends(7,8)
community.outbreak(random.randint(0,8))
print(community)
community.death()
community.recovery()
print("Survivors/Recovered People: ", "\n", community)
