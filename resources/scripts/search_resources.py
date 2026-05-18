resources = [
    "Python Programming",
    "Networking Basics",
    "Cybersecurity Essentials",
    "Open Source Fundamentals"
]

search = input("Search resource: ")

for item in resources:
    if search.lower() in item.lower():
        print(item)