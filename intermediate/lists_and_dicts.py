def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {'firstnamme': "Angel", "lastname": "Nava"}

    super_list = [
        {'firstname': "Angel", "lastname": "Nava"},
        {'firstname': "Facunndo", "lastname": "García"},
        {'firstname': "Miguel", "lastname": "Torres"},
        {'firstname': "Pepe", "lastname": "Rodelo"},
        {'firstname': "José", "lastname": "Pérez"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
    }
    
    for key, value in super_dict.items():
        print("{}: {}".format(key, value))
        
    for i in super_list:
        # print(i.items())
        print(i["firstname"], "-", i["lastname"])
        # print(i.keys())

if __name__ == '__main__':
    run()
