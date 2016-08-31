import random

side = random.randint(1,2)

# if side = 1, its heads
# if side = 2, its tails

if (side==1):
    result = "heads"
else:
    result = "tails"

print("I flipped a coin and the result is", result)
