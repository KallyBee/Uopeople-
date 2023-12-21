Part A

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



Part B



def sentence_to_wordlist(sentence):

    word_list = sentence.split()

    reversed_word_list = list(reversed(word_list))

    return reversed_word_list



# Example usage:

input_sentence = input(“Enter a sentence: “)

output_word_list = sentence_to_wordlist(input_sentence)

print(“Reversed Word List:”, output_word_list)

 
