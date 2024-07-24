import random
from scipy.stats import chi2_contingency

# Input user data
user_visits = int(input("Enter the total number of users in the experiment: "))
conversions_A = int(input("Enter the number of conversions for version A: "))
conversions_B = int(input("Enter the number of conversions for version B: "))

# Define versions A and B
versions = ['A', 'B']

def assign_version():
    """Randomly assign a user to version A or B."""
    return random.choice(versions)

# Track data in a dictionary
data = {
    'A': {'visits': 0, 'conversions': 0},
    'B': {'visits': 0, 'conversions': 0}
}

# Simulate user visits and conversions
for _ in range(user_visits):
    version = assign_version()
    data[version]['visits'] += 1
    if version == 'A':
        if random.random() < conversions_A / user_visits:
            data[version]['conversions'] += 1
    else:
        if random.random() < conversions_B / user_visits:
            data[version]['conversions'] += 1

print("\nData collected:")
print(f"Version A - Visits: {data['A']['visits']}, Conversions: {data['A']['conversions']}")
print(f"Version B - Visits: {data['B']['visits']}, Conversions: {data['B']['conversions']}")

# Create contingency table
contingency_table = [
    [data['A']['conversions'], data['A']['visits'] - data['A']['conversions']],
    [data['B']['conversions'], data['B']['visits'] - data['B']['conversions']]
]

# Perform chi-square test
chi2, p, dof, expected = chi2_contingency(contingency_table)

print("\nResults of Chi-square test:")
print(f"Chi-square statistic: {chi2}")
print(f"P-value: {p}")

# Determine which version is better
if p < 0.05:  # Assuming a significance level of 0.05
    if data['A']['conversions'] / data['A']['visits'] > data['B']['conversions'] / data['B']['visits']:
        print("Version A is better.")
    else:
        print("Version B is better.")
else:
    print("No significant difference between versions.")