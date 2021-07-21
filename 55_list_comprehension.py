friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print(friends)
print(starts_s)
print(friends is starts_s)
print("friends:", id(friends), "starts_s:", id(starts_s))
print(id(friends) is id(starts_s))
