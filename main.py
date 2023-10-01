import random
import time
horses = ["At 1", "At 2", "At 3", "At 4"]
positions = [0, 0, 0, 0]

def race():
    for i in range(len(horses)):
        distance = random.randint(1, 3)
        positions[i] += distance
        print(f"{horses[i]} {'. ' * positions[i]}")


def main():
    print("At yarışı başlıyor!")
    while True:
        race()
        time.sleep(1)
        winner = positions.index(max(positions))
        if positions[winner] >= 20:
            print(f"{horses[winner]} yarışı kazandı!")
            break

if __name__ == "__main__":
    main()
