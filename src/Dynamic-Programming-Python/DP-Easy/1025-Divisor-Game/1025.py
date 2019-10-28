#1025. Divisor Game
#Alice and Bob take turns playing a game, with Alice starting first.
#
#Initially, there is a number N on the chalkboard.  On each player's turn, that player makes a move consisting of:
#
#Choosing any x with 0 < x < N and N % x == 0.
#Replacing the number N on the chalkboard with N - x.
#Also, if a player cannot make a move, they lose the game.
#
#Return True if and only if Alice wins the game, assuming both players play optimally.


class Solution:
    def divisormath(self, n):
        return n % 2 == 0
    
    def recursive(self, n):
        if n <= 1: return True
        for i in range(1, n):
            if n % i == 0:
                if not self.recursive(n-i):
                    return True
        return False

print Solution().divisormath(81)