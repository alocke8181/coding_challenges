def triple_step(steps):
    #A child is hopping up a set of 'n' steps. They can hop up 1, 2, or 3 steps at a time. How many possible ways can the child go up the steps

    if steps < 0:
        return 0
    elif steps == 0:
        return 1
    else:
        return triple_step(steps-1) + triple_step(steps - 2) + triple_step(steps-3)