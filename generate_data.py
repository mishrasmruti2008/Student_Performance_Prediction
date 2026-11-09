import os
import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)
n_samples = 600

# Generate features
hours_studied = np.random.uniform(1.0, 10.0, n_samples)
attendance = np.random.uniform(50.0, 100.0, n_samples)
previous_scores = np.random.uniform(40.0, 100.0, n_samples)
sleep_hours = np.random.uniform(4.0, 9.5, n_samples)
extracurricular = np.random.choice([0, 1], n_samples)

# Calculate final grade with weighted formula + slight gaussian noise
final_grade = (
    (hours_studied * 4.2)
    + (attendance * 0.38)
    + (previous_scores * 0.22)
    + (sleep_hours * 1.2)
    + (extracurricular * 2.5)
    + np.random.normal(0, 2.5, n_samples)
)
final_grade = np.clip(final_grade, 0, 100)

# Create DataFrame
df = pd.DataFrame(
    {
        "Hours_Studied": hours_studied,
        "Attendance": attendance,
        "Previous_Scores": previous_scores,
        "Sleep_Hours": sleep_hours,
        "Extracurricular_Activities": extracurricular,
        "Final_Grade": final_grade,
    }
)

# Save dataset
os.makedirs("data", exist_ok=True)
df.to_csv("data/student_data.csv", index=False)
print("Dataset generated successfully at 'data/student_data.csv'!")