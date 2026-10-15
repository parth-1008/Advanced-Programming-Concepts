import math

points = [(1, 2), (3, 4), (-5, 12), (0, 1)]

print("Current points list:", points)

new_x = float(input("\nEnter x for a new point: "))
new_y = float(input("Enter y for a new point: "))
points.append((new_x, new_y))
print("Updated points list:", points)


print("\n--- Calculate Distance Between Two Points ---")
index1 = int(input(f"Enter index of first point (0 to {len(points)-1}): "))
index2 = int(input(f"Enter index of second point (0 to {len(points)-1}): "))

p1 = points[index1]
p2 = points[index2]


distance = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
print(f"Distance between {p1} and {p2} is: {distance:.2f}")



print("\n--- Farthest Point from Origin ---")
farthest_point = points[0]
max_distance = math.sqrt(farthest_point[0] ** 2 + farthest_point[1] ** 2)

for p in points:

  dist_from_origin = math.sqrt(p[0] ** 2 + p[1] ** 2)

  if dist_from_origin > max_distance:
    max_distance = dist_from_origin
    farthest_point = p

print(
    f"The point farthest from (0, 0) is {farthest_point} with a distance of"
    f" {max_distance:.2f}"
)