def main():    
    dice1 = list(map(int, input().strip().split()))[:6]
    dice2 = list(map(int, input().strip().split()))[:6]
    dice3 = list(map(int, input().strip().split()))[:6]
    n = int(input())
    cnt = 0
    for x in dice1:
        for y in dice2:
            for z in dice3:
                if x + y + z == n:
                    cnt += 1
    print(f"{(cnt / 216) * 100:.2f}%")

if __name__ == "__main__":
    main()

