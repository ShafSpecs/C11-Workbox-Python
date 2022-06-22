import string

lower_case = string.ascii_lowercase

user_input = input("Enter the phrase: ")
user_input = user_input.lower()

letters = [lower_case[i] for i in range(0, len(lower_case))]

user_letters = []

for i in range(0, len(lower_case)):
  count = user_input.count(lower_case[i])
  user_letters.append(count)

final_dict = dict(zip(letters, user_letters))

print(final_dict)
