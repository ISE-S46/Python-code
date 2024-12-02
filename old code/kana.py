import random
n_students = 20
days_in_years = 365
n_simulations = 10000
X = []
for l in range(0,n_simulations,1):
    for i in range(0,n_students,1):
        X.append(random.randint(1, days_in_years))
for i in range(0,n_students*n_simulations,1):
    print(X[i])


