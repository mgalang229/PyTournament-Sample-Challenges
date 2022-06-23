def main():
    name, length = input().split()
    name = name
    temp = name[::-1]
    if name.lower() == temp.lower():
        print(f"{name} should be invited to the party!")
    else:
        print(f"{name} should not be invited to the party!")

if __name__ == "__main__":
    main()
