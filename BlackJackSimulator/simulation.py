from BlackJack import *
from random import *
import matplotlib.pyplot as plt
import numpy as np
from BlackjackS2 import *

class simulation:
    def __init__(self, num_of_runs):
        self.num_of_runs = num_of_runs

    def simulate(self):
        print("start simulation")
        result_sheet = []
        P_won_count = 0
        tie_count = 0
        for sim_num in range(self.num_of_runs):
            BlackJack1 = Blackjack(6)
            BJ_result = BlackJack1.BlackJack_Game()
            if BJ_result == 'Player Win':
                P_won_count += 1
            if BJ_result == 'tie':
                tie_count += 1
            result_sheet.append(BJ_result)
            # print('Player_Won=', P_won_count, 'tie_count =', tie_count, 'Dealer_won = ', self.num_of_runs-P_won_count-tie_count)
        return result_sheet

    def simulate_S2(self):
        print("start simulation S2")
        result_sheet_H = []
        result_sheet_S = []

        for sim_num in range(self.num_of_runs):
            BlackJack2 = BlackjackS2(6)
            BJ_result_H, BJ_result_S = BlackJack2.BlackJack_GameS2()
            result_sheet_H.append(BJ_result_H)
            result_sheet_S.append(BJ_result_S)
        return result_sheet_H, result_sheet_S


sim = simulation(100000)
sim_result = sim.simulate()
# sim_result_H, sim_result_S = sim.simulate_S2()

# print(sim_result)
x = sim_result
# x_H = sim_result_H
# x_S = sim_result_S

plt.hist(x)  # density=False would make counts
plt.ylabel('Frequency')
plt.xlabel('BJ Decision')
plt.show()

# plt.hist(x_H)  # density=False would make counts
# plt.ylabel('Frequency')
# plt.xlabel('BJ Strategy S2')
# plt.show()
#
# plt.hist(x_S)  # density=False would make counts
# plt.ylabel('Frequency')
# plt.xlabel('BJ Strategy S2')
# plt.show()



