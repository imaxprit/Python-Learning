# Exercise 10. Call Function using Positional and Keyword Arguments

def describe_pet(animal_type, pet_name) :
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
    print()

describe_pet("Hamster", "Harry")
describe_pet(animal_type="dog", pet_name="willie")