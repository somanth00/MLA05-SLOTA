
# Candidate Elimination Algorithm

# Training dataset
data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

# Initialize hypotheses
S = ['0'] * 6
G = [['?'] * 6]

# Process training examples
for row in data:
    x = row[:-1]
    target = row[-1]

    if target == 'Yes':
        # Generalize specific hypothesis
        for i in range(6):
            if S[i] == '0':
                S[i] = x[i]
            elif S[i] != x[i]:
                S[i] = '?'

        # Remove inconsistent general hypotheses
        G = [
            g for g in G
            if all(g[i] == '?' or g[i] == x[i]
                   for i in range(6))
        ]

    else:
        # Specialize general hypothesis
        new_G = []

        for g in G:
            for i in range(6):
                if g[i] == '?' and S[i] != '?' and S[i] != x[i]:
                    h = g.copy()
                    h[i] = S[i]
                    new_G.append(h)

        G = new_G

print("Final Specific Hypothesis (S):")
print(S)

print("\nFinal General Hypothesis (G):")
for h in G:
    print(h)
