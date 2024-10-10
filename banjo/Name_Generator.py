import random
with open("banjo/first_names","r") as f:
    first_names = [line.strip() for line in f.readlines()]
with open("banjo/last_names","r") as f:
    last_names = [line.strip() for line in f.readlines()]


def generate_name():
    # Generate a random index for the first name and last name lists
    idx1 = random.randint(0, len(first_names) - 1)
    idx2 = random.randint(0, len(last_names) - 1)

    # Return a tuple containing the generated name
    return first_names[idx1]+ " "+ last_names[idx2]

# Generate and print a random name
print(generate_name())