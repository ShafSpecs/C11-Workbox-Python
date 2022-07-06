def longest_consec(strarr: list, k: int):
  concatenated = []
  temp_list = []
  counter = 0
  i = 0
  
  while counter < len(strarr) - k:
    if len(temp_list) < k:
      temp_list.append(strarr[i + counter])
      i += 1
    else:
      str_ = "".join(temp_list)
      concatenated.append(str_)
      temp_list.clear()
      counter += 1
      i = 0
  concatenated.sort()
  print(concatenated)


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
