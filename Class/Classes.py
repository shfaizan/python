class User:
    name = "Faizan"
    Id = 1

def main():
    user = User()
    user1 = User()
    user2 = User()
    user1.name = "sentry"
    user2.name = "Thor"
    print(user.name)
    print(user1.name)
    print(user2.name)
    print(user1.Id)
    print(user2.Id)

if __name__ == "__main__": main()