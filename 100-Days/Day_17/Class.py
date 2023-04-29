class User:
    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("Fidelis", 200)
user_2 = User("Angela", 201)
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
 