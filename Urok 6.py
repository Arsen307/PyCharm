try:
    print("start code")
    print(error)
    print("No errors")

except:
    print("We have an error")


print("code after capsule")

try:

    try:
        print("start code")
        print(error)
        print("No errors")

    except SyntaxError:
        print("Wrong Syntax")

except NameError as error:
    print(error)

class BuildingEror(Exception):
    def __str__(self):
        return f"With so much material the house cannot be built!"

def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return "enough material"
    else:
        raise BuildingEror(amount_of_material)