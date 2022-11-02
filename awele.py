from random import choice

COMPUTER = 0
PLAYER = 1


class Hole:
    def __init__(self, hole_number: int):
        self.seeds = 4
        self.number = hole_number
        self.owner = self.number // 6  # 6 first holes are the computer's, others are the human's

    def take(self) -> int:
        """ Take seeds from a hole """
        seeds = self.seeds
        self.seeds = 0
        return seeds

    def plant(self):
        self.seeds += 1


class Awele:
    def __init__(self):
        self.hole = [Hole(i) for i in range(12)]
        self.score = [0, 0]

    def deal(self, n: int, player: int) -> None:
        seeds = self.hole[n].take()
        leave_empty = None
        if seeds >= 12:
            leave_empty = n
        while seeds:
            n = (n + 1) % 12
            if n != leave_empty:
                self.hole[n].plant()
            seeds -= 1
        while 2 <= self.hole[n].seeds <= 3 and self.hole[n].owner != player:
            self.score[player] += self.hole[n].take()
            n = (n - 1) % 12

    def simulate(self, n: int, player: int = COMPUTER) -> int:
        """
        same as deal but virtually
        """
        virtual_board = [self.hole[i].seeds for i in range(12)]
        result = 0
        seeds = virtual_board[n]
        virtual_board[n] = 0
        leave_empty = None
        if seeds >= 12:
            leave_empty = n
        while seeds:
            n = (n + 1) % 12
            if n != leave_empty:
                virtual_board[n] += 1
            seeds -= 1
        while 2 <= virtual_board[n] <= 3 and n // 6 != player:
            result += virtual_board[n]
            virtual_board[n] = 0
            n = (n - 1) % 12
        return result

    def find_best_move(self):
        m = max([i for i in range(6) if self.hole[i].seeds != 0], key=lambda x: self.simulate(x))
        n = self.simulate(m)
        return choice([i for i in range(6) if self.hole[i] != 0 and self.simulate(i) == n])

    def __str__(self):
        result = "*" * 22 + "\n"
        for i in range(6):
            result += str(self.hole[i].seeds).zfill(2) + "\t"
        result += "\n"
        for i in range(11, 5, -1):
            result += str(self.hole[i].seeds).zfill(2) + "\t"
        result += "\n"
        result += "*" * 22 + "\n"
        return result


awele = Awele()
print(awele)
while sum(awele.score) < 48:
    j = int(input("quel trou voulez vous jouer ? (1..6) "))
    j = 12 - j
    awele.deal(j, PLAYER)
    print(awele)
    print(f"votre score : {awele.score[PLAYER]}")
    if sum(awele.score) < 48:
        awele.deal(awele.find_best_move(), COMPUTER)
        print(f"score ordi : {awele.score[COMPUTER]}")
        print(awele)
if awele.score[PLAYER] < awele.score[COMPUTER]:
    print("L'ordi a gagné.")
else:
    print("Bravo à vous !")
