# There's a list with info about people who search for a date. For each person, a few
# parameters are specified: their gender, age, hobbies, and city.
# Help a new user write a function that selects from the given list people older t
# han 30, interested in art, and living in Berlin. The function should return their names
# as a string, separated by a comma and a space, e.g. "Maria, Daniel" for the example list
# above.

def run():
    potential_dates = [{"name": "Julia", "gender": "female", "age": 29,
                        "hobbies": ["jogging", "music"], "city": "Hamburg"},
                       {"name": "Sasha", "gender": "male", "age": 18,
                        "hobbies": ["rock music", "art"], "city": "Berlin"},
                       {"name": "Maria", "gender": "female", "age": 35,
                        "hobbies": ["art"], "city": "Berlin"},
                       {"name": "Daniel", "gender": "non-conforming", "age": 50,
                        "hobbies": ["boxing", "reading", "art"], "city": "Berlin"},
                       {"name": "John", "gender": "male", "age": 41,
                        "hobbies": ["reading", "alpinism", "museums"], "city": "Munich"}]

    selected = []

    for person in potential_dates:
        if person['age'] > 30 and 'art' in person['hobbies'] and person['city'] == 'Berlin':
            selected.append(person['name'])

    return ', '.join(selected)


if __name__ == "__main__":
    run()
    print(run())
