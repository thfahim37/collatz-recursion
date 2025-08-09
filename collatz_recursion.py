import matplotlib.pyplot as plt

print("Collatz Recursion v1.0")

# Recursion Function
def collatz(n):
	if n % 2 == 0:
		return n / 2
	elif n % 2 != 0:
		return 3 * n + 1

# User Input
n = int(input("Enter starting number:\n"))

# Data Arrays
n_vals = [n]
steps = [0]

# Update Loop
while True:
	new_step = steps[-1] + 1
	n_new = collatz(n_vals[-1])
	
	if new_step > 100:
		break # End after 100 steps
	
	steps.append(new_step)
	n_vals.append(n_new)

# Plot Customization
plt.title("Collatz Recursion")
plt.xlabel("Steps")
plt.ylabel("Number")
plt.grid(True)

# Results
plt.plot(steps, n_vals)
plt.show()