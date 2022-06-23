
def main():
    n, m = map(int, input().split())
    num = [0] * m
    names = [""] * m
    for i in range(m):
        num[i], names[i] = input().split()
        num[i] = int(num[i])
    for i in range(n):
        checker = False
        for j in range(m):
            if (i + 1) % num[j] == 0:
                checker = True
                print(names[j], end="")
        if not checker:
            print((i + 1), end="")
        print()

if __name__ == "__main__":
    main()
