<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

# Add labels
fake["label"] = 0
true["label"] = 1

# Combine datasets
data = pd.concat([fake, true])

# Define y
y = data["label"]

# Plot
sns.countplot(x=y)
plt.title("Fake vs Real News Distribution")
plt.show()
=======

>>>>>>> a0782c34c1fd423a4aa64d0e316125f97b28f9b5
