# To check if a value does not appear in a list you can use the not keyword
banned_users = ["andrew", "carolina", "david"]
user = "marie"

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")