people = [
    {"name":"Tom", "id" : 95},
    {"name":"Kim", "id" : 5},
    {"name":"Ezra", "id" : 9},
    {"name":"Kim", "id" : 15},
    {"name":"Bob", "id" : 49},
    {"name":"Hope", "id" : 25},
    {"name":"Dom", "id" : 45},
    {"name":"Pope", "id" : 12},
    {"name":"Sam", "id" : 11}
]


def f(people):
    return people["id"]

# lambda people: people["id"]
# lambda input : output 

people.sort(key = lambda people: people["id"])

print(people)