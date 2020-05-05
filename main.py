import random


def main():
    random_choice()


def random_choice():
    classes = ["Bio", "Strength & Conditioning", "Writing for College",
               "Math Analysis", "AP SpLit", "AP Lang", "AP Macro",
               "CS 3A", "Tutorial", "AP Gov", "Trig"]
    for i in range(6):
        r_class = random.choice(classes)
        print(f"\nBefore: {r_class}")
        classes.remove(r_class)
        print(f"After: {r_class}")
        print(f"Classes after remove: {classes}\n")


if __name__ == "__main__":
    main()
