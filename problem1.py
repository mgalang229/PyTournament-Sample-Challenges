def main():
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    print(max(arr))
    print(min(arr))

if __name__ == "__main__":
    main()
