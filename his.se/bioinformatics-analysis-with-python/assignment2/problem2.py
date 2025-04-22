#ask the user for an input
dna_sequence = input("Input a DNA sequence: ").lower()

#define counters and list
counter_g = 0
counter_c = 0
new_dna_list = []

#iterate over the sequence, convert and add the characters in the newly created list and count C's and G's
for character in dna_sequence:
 if character == "c":
  new_dna_list.append(character.upper())
  counter_c += 1
 if character == "g":
  new_dna_list.append(character.upper())
  counter_g += 1
 if character == "a" or character == "t":
  new_dna_list.append("*")

#create our final string by concatenating the list to an empty string and output the results
print("Output:", "".join(new_dna_list))
print("Number of C's:", counter_c)
print("Number of G's:", counter_g)
