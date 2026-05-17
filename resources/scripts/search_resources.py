resources = [
    "python programming",
    "Networking Basics",
    "Cybersecuruty Essentials",
    "Open Source Fundamentals",

]

search = input("Search resources:   ")


for item in resources:
    if search.lower() in item.lower():
        print(item)