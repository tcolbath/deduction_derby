from horse import Horse

class Player:
    def __init__(self, name="Player"):
        self._name = name
        self.wallet = 100
        self.payout = 0

    def bid(self, horse, amount, turn, crossed_the_line):
        if amount > self.wallet:
            print("Not enough money!")
            return
        if amount + horse._total_bids > 9999:
            print(f"Exceeded max total bid for {horse._name}")
            return
        horse._total_bids += amount
        self.wallet -= amount
        top_3 = crossed_the_line[0:2]
        if horse in top_3:
            self.calc_payout(horse, amount, turn, top_3)

    
    def calc_payout(self, horse, amount, turn, top_3):
        # first place finisher
        if top_3[0] == horse:
            pay = 3 * ((len(horse._rolls)) - turn) * amount
        # second place finisher
        if top_3[1] == horse:
            pay = 2 * ((len(horse._rolls)) - turn) * amount
        # third place finisher
        if top_3[2] == horse:
            pay = 1 * ((len(horse._rolls)) - turn) * amount      
        self.payout += pay

def bid_log():
    pass

def clear_bid_log():
    with open("./data/bid_log.txt", "w") as bid_log:
        bid_log.write("Deduction Derby -- Bid Log\n")
