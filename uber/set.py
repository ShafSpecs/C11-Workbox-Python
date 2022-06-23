s1 = {1, 2, 4, 5}
s2 = {4, 5, 6, 7}

s3 = {1, 2, 3, 4, 5, 6, 7, 8}

### Add Element ###
# s1.add(el) // add the specified element to the set; if el found, does nothing.

### Remove elements ###
# s1.remove(elem) // throws an error if not found.
# s1.discard(elem2) // no error thrown if elem2 not found.

### Remove(Pop Edition) ###
# s1.pop() // removes a random, arbitrary elem from the set.

##### RELATIONSHIPS #####
# `|` (Piping symbol) used to represent your "union" in maths set. No side effect occurs
# Prints out elements in both sets. Doesn't duplicate values present in multiple sets.
# Example.: print(s1 | s2); also print(s1.union(s2)) // prints value of both sets (no duplicates)
#
# `|=` (pipe-equals to Symbol) used to update a set with the values of another set (Also known as union_intersection).
# Example.: print(s1.update(s2)); also print(s1 |= s2) @below
# // s1 becomes the value of s1 and s2(no duplicates). s2 remains the same
#
# `&` (am-passant Symbol) used to represent "intersection" in maths. It presents the
# elements common to both(or more) sets
# Example.: print(s1.intersection(s2)); also print(s1 & s2)
#
# `&=` (am-passant-equals to Symbol) also called "intersection_update". Used to update a set with the
# intersection values of that set (s1) and the other provided set(s?)
# Example.: print(s1.intersection_update(s2)); also print(s1 &= s2)
# // s1 empties and is replaced with the values of the intersection of s1 and s2
#
# `-` (minus Symbol) used to discover unique (difference), distinct values in a set that isn't in the other provided ones.
# Example.: print(s2.difference(s1)); also print(s2 - s1) // prints the values in s2 but not in s1
#
# `-=` (difference-equals to) used to update a set with values that are in a set that isn't in the other
# Example.: print(s1.difference_update(s2)); also print(s1 -= s2)
# // updates s1 with values that are in s2 but not in s2 (More or less, removes the intersections of the sets)
#
# `^` (caret Symbol) used to remove the intersects of 2 sets, more or less. So it gets the value of "(s1 - s2)" and
# "(s2 - s1)" and returns the union of both.
# Example.: print(s1.symmetric_difference(s2)); also print(s1 ^ s2) // prints all values of s1 and s2 except the intersects
#
# `^=` (caret-equals to) used to find the elements that aren't intersects in a relation and update set_1 with the value.
# Example.: print(s1.symmetric_difference_update(s2)); also print(s1 ^= s2)
# // Clears s1 and updates it with the value of both s1 and s2 except the intersects.
