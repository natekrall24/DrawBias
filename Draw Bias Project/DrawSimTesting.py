import numpy as np
from sympy import factorial

# Calculates the probability of yielding a completely biased draw 
# when you have a draw of n players, and b players you're trying to rig the draw for
# assuming every kind of draw is equally likely

# Limitations:
# b must be a power of two -- 
# the logic behind "maximum bias" varies heavily when you have an in-between-power-of-2 for b
# only considers "maximum bias" --
# draws like the Louisville draw are biased to an extent but not to the maximum which involves more thorough analysis
# does not consider seeding whatsoever; players are completely randomized in the draw

n = 16  # for example, 128 players in Louisville draws
b = 4  # for example, 8 Louisville players in that tournament

def simulateDraw(n, b):

    draw = np.array([1]*b + [0]*(n-b))
    np.random.shuffle(draw)

    biased = True
    for i in range(b):
        s = i * int(n/b)
        count = 0
        for j in range(int(n/b)):
            if draw[s + j] == 1:
                 count += 1
        if count != 1:
            biased = False
            break
    
    return biased

def trueExpression(n,b):
    return (((n / b)**b) * factorial(b) * factorial(n - b) / factorial(n)) #formula calculated by hand

n_draws = 100000

biasedCount = sum(simulateDraw(n, b) for _ in range(n_draws))
trueExp = trueExpression(n, b)

print(biasedCount/n_draws)
print(trueExp)

