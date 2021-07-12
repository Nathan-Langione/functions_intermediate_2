x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def update_x(lst):
    lst[1][0] = 15
    return lst
print(update_x(x))

def update_students(lst):
    lst[0]['last_name'] = "Bryant"
    return lst
print(update_students(students))

def update_sports(dic):
    dic["soccer"][0] = "Andres"
    return dic
print(update_sports(sports_directory))

def update_z(str):
    str[0]['y'] = 30
    return str

print(update_z(z))


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(lst):
    for i in lst:
        print(i)
iterateDictionary(students) 


def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])
    return
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students) 


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for k in some_dict:
        length = len(some_dict[k])
        print("{} {}".format(length, k.upper()))
        for i in some_dict[k]:
            print(i)
        print("\n")
printInfo(dojo)


