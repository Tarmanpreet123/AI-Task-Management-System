import random
import pandas as pd
from faker import Faker

# Initialize Faker instance
fake = Faker()

# List of possible values
skill_levels = [1, 2, 3, 4, 5]  # Skill levels from 1 to 5
preferred_task_types = ["Technical", "Research", "Admin", "Support"]

# Function to generate synthetic user data
def generate_user_data(num_users):
    users = []
    
    for user_id in range(1, num_users + 1):
        skill_level = random.choice(skill_levels)
        avg_completion_time = round(random.uniform(1, 5), 2)  # Average completion time in hours
        tasks_completed = random.randint(50, 100)  # Tasks completed between 50 to 100
        current_workload = round(random.uniform(1, 5), 2)  # Current workload in hours
        preferred_task_type = random.choice(preferred_task_types)
        performance_score = round(random.uniform(0.5, 1), 2)  # Performance score between 0.5 and 1
        
        user = {
            "User_ID": f"U{user_id:02d}",
            "Skill_Level": skill_level,
            "Avg_Completion_Time": f"{avg_completion_time} hrs",
            "Tasks_Completed": tasks_completed,
            "Current_Workload": f"{current_workload} hrs",
            "Preferred_Task_Type": preferred_task_type,
            "Performance_Score": performance_score
        }
        users.append(user)
    
    return pd.DataFrame(users)

# Generate synthetic user data
num_users = 10  # Number of synthetic users to generate
user_data = generate_user_data(num_users)

# Display the generated user data
print(user_data)

# Save the generated user data to a CSV file
user_data.to_csv("user_behavior_profile.csv", index=False)