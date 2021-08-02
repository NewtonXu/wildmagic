def reset_zero(consecutive_fails):
    return 0

def decrease_by_x(consecutive_fails):
    x = 2
    return max(0, consecutive_fails - x)

def no_decrease(consecutive_fails):
    return consecutive_fails

decrement_on_fail = 0.05 #How much to increase odds by per failure
min_chance = 0.75 #Cap on surge boost
n = 6 #Number of spells per short rest
probabilities = (n+1)*[0] #Index is number of wild surges
reset_strat = reset_zero #Which reset strategy to use on success


for i in range(0,pow(2,n)):
    consecutive_fails = 0
    cur_chance = 0.95
    total_success = 0
    base_probability = 1
    for j in range(0,n):
        if (i >> j & 1)==0:
            base_probability *= max(min_chance, cur_chance-consecutive_fails*decrement_on_fail)
            consecutive_fails += 1
        else:
            total_success += 1
            base_probability *= (1-max(min_chance, cur_chance-consecutive_fails*decrement_on_fail))
            consecutive_fails = reset_strat(consecutive_fails)

    probabilities[total_success] += base_probability

print([round(x, 3) for x in probabilities])