import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker instance
fake = Faker()

# List of possible values
categories = ["Feature", "Bug", "Improvement"]
priorities = ["Low", "Medium", "High"]
classes = ["Research", "Admin", "Technical", "Support"]

# Function to generate synthetic task datag
def generate_task_data(num_tasks):
    tasks = []
    
    for task_id in range(1, num_tasks + 1):
        created_date = fake.date_this_year(before_today=True, after_today=False)
        deadline = created_date + timedelta(days=random.randint(1, 10))  # Deadline within 1-10 days after creation
        est_hours = round(random.uniform(1, 10), 2)
        category = random.choice(categories)
        priority = random.choice(priorities)
        class_type = random.choice(classes)
        assigned_to = f"U{random.randint(1, 10):02d}"  # U01 to U10
        
        task = {
            "Task_ID": task_id,
            "Task_Description": fake.sentence(nb_words=6),
            "Created_Date": created_date,
            "Deadline": deadline,
            "Est. Hours": est_hours,
            "Category": category,
            "Priority": priority,
            "Class": class_type,
            "Assigned_To": assigned_to
        }
        tasks.append(task)
    return pd.DataFrame(tasks)

# Generate synthetic task data
num_tasks = 20000  # Number of synthetic tasks to generate
synthetic_data = generate_task_data(num_tasks)

# Display the generated data
print(synthetic_data)

synthetic_data.to_csv("synthetic_task_data.csv", index=False)