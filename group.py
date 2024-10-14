"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...

my_group = {
    'Jill' : {
        'age' : 26,
        'job' : 'biologist',
        'connection' : {'Zalika' : 'friend', 'John' : 'partner'}
    },
    'Zalika' : {
        'age' : 28,
        'job' : 'artist',
        'connection' : {'Jill' : 'friend'}
    },
    'John' : {
        'age' : 27,
        'job' : 'writer',
        'connection' : {'Jill' : 'partner'}
    },
    'Nash' : {
        'age' : 34,
        'job' : 'chef',
        'connection' : {'John' : 'cousin', 'Zalika' : 'landlord'}
    }
}

for key, value in my_group.items():
    for k, v in value['connection'].items():
        my_group[k]['connection'][key] = v

print(my_group)

max_age = 0
avg_age = 0
max_age_at_least_1conn = 0
max_age_at_least_1friend = 0
for key in my_group:
    age = my_group[key]["age"]
    avg_age += age
    if age > max_age:
        max_age = age
        if age > max_age_at_least_1conn and len(my_group[key]['connection']) > 0:
            max_age_at_least_1conn = age
            if age > max_age_at_least_1friend:
                for k, v in my_group[key]['connection'].items():
                    if v == 'friend':
                        max_age_at_least_1friend = age
                        break

avg_age /= len(my_group)

def main():
    print(max_age)
    print(avg_age)
    print(max_age_at_least_1conn)


if __name__ == "__main__":
    main()