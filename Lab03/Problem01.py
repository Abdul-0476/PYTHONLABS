class SocialNetwork:
    def __init__(self):
        self.network = {}

    def add_user(self, user):
        self.network.setdefault(user, set())

    def add_friendship(self, user1, user2):
        self.network[user1].add(user2)
        self.network[user2].add(user1)

    def print_network(self):
        for user, friends in self.network.items():
            print(f"{user}'s friends: {', '.join(friends) if friends else 'No friends'}")


sn = SocialNetwork()
users = ["Ahmed", "Ali", "Lela", "Sara", "Fahad", "Nora", "Khalid"]
for user in users:
    sn.add_user(user)

friendships = [("Ahmed", "Nora"), ("Ahmed", "Khalid"), ("Ali", "Khalid"), ("Ali", "Sara"),
               ("Ali", "Lela"), ("Sara", "Nora"), ("Nora", "Khalid"), ("Lela", "Fahad")]
for u1, u2 in friendships:
    sn.add_friendship(u1, u2)

sn.print_network()
