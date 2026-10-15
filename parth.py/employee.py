project_a = {"Alice", "Bob", "Charlie", "David"}
project_b = {"Charlie", "David", "Eve", "Frank"}

print("--- Company Project Analysis ---")
print("Employees in Project A:", project_a)
print("Employees in Project B:", project_b)

both_projects = project_a.intersection(project_b)
print("\n--- Employees Working on Both Projects ---")
print(both_projects)

only_one_project = project_a.symmetric_difference(project_b)
print("\n--- Employees Working Only on One Project ---")
print(only_one_project)

all_employees = project_a.union(project_b)
print("\n--- Total Unique Employees Across Both Projects ---")
print(all_employees)