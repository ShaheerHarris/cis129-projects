# Function to get total number of hot dogs needed
def get_total_hotdogs():
    people = int(input("Enter the number of people attending the cookout: "))
    hotdogs_per_person = int(input("Enter the number of hot dogs for each person: "))
    return people * hotdogs_per_person

# Displaying results
def show_results(dogs_left, min_dogs, buns_left, min_buns):
    print("Minimum packages of hot dogs needed:", min_dogs)
    print("Minimum packages of hot dog buns needed:", min_buns)
    print("Hot dogs left over:", dogs_left)
    print("Hot dog buns left over:", buns_left)

# Main program
def main():
    total = get_total_hotdogs()
    DOGS = 10
    BUNS = 8
    dogs_left = (DOGS - total % DOGS) % DOGS
    min_dogs = total // DOGS + (1 if total % DOGS != 0 else 0)
    buns_left = (BUNS - total % BUNS) % BUNS
    min_buns = total // BUNS + (1 if total % BUNS != 0 else 0)
    show_results(dogs_left, min_dogs, buns_left, min_buns)

main()
