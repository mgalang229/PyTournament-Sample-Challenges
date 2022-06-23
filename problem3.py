import math

def main():
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    res = 0
    for x in arr:
        res += x
    res /= n
    # print(res)
    mn = math.fabs(arr[0] - res)
    for i in range(1, n):
        mn = min(mn, math.fabs(arr[i] - res))
    for x in arr:
        if math.fabs(x - res) == mn:
            print(x, end=" ")
    print()


if __name__ == "__main__":
    main()
