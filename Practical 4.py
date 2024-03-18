# pole and disc ## Tower of Hanoi
def towerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return

    towerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    print("Move Disc", n, "From Rod:", from_rod, "To rod", to_rod)
    towerOfHanoi(n - 1, aux_rod, to_rod, from_rod)

n = int(input("ENTER NUMBER OF DISC: "))
towerOfHanoi(n, 'A', 'B', 'C')