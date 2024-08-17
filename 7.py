import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_simulations):
    results = [0] * 13  # Індекси від 2 до 12
    for _ in range(num_simulations):
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        sum_rolls = roll_1 + roll_2
        results[sum_rolls] += 1

    probabilities = [result / num_simulations for result in results]
    return probabilities[2:] 

num_simulations = 1000000
probabilities = monte_carlo_simulation(num_simulations)

print("Сума\tІмовірність")
for i in range(2, 13):
    print(f"{i}\t{probabilities[i-2]*100:.2f}% ({probabilities[i-2]:.5f})")

# Графік 
sums = list(range(2, 13))
plt.bar(sums, probabilities, color='skyblue')
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Ймовірності сум при киданні двох кубиків')
plt.show()
