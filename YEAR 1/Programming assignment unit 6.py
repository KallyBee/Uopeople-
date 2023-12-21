Part 1
# Define a list of TICT staff members
tict_staff = ["Caleb", "Theo", "Panda", "Dominic", "Peace", "Moses", "Divine", "Maxwell", "Emma", "Precious"]

# Create two sublists from the tict_staff list
subList1 = tict_staff[:5]  # First five elements
subList2 = tict_staff[5:]  # Elements from index 5 to the end

# Add a new staff member, "Kriti Brown," to subList2
subList2.append("Kriti Brown")

# Remove the second element (index 1) from subList1
subList1.pop(1)

# Merge the two sublists to create a new list, merged_list
merged_list = subList1 + subList2

# Define a list of salaries corresponding to the staff members
salary_list = [30000, 75000, 40000, 13000, 15000, 12000, 10000, 70000, 50000, 14000]

# Calculate updated salaries by applying a 4% increase using list comprehension
updated_salary_list = [i * 1.04 for i in salary_list]

# Print the updated salary list
print(updated_salary_list)

# Sort the updated salary list in descending order to find the top 3 salaries
top3salaries = sorted(updated_salary_list, reverse=True)

# Select the top 3 salaries using list slicing
top3salaries = top3salaries[:3]

# Alternatively, you can directly slice the original salary list to get the top 3
# top3salaries = salary_list[:3]

# Print the top 3 salaries
print(top3salaries)



Explanation:
1. **tict_staff**: List of TICT staff members.
2. **subList1** and **subList2**: Split the staff list into two sublists.
3. **subList2.append("Kriti Brown")**: Add a new staff member to the second sublist.
4. **subList1.pop(1)**: Remove the second staff member from the first sublist.
5. **merged_list**: Combine the modified sublists into a new list.
6. **salary_list**: List of salaries corresponding to the staff members.
7. **updated_salary_list**: Calculate updated salaries with a 4% increase.
8. **top3salaries**: Sort the updated salary list in descending order and select the top 3.
9. **print(updated_salary_list)**: Display the updated salary list.
10. **print(top3salaries)**: Display the top 3 salaries.
