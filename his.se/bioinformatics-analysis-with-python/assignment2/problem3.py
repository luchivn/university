#open the file
with open("gene_exons.txt") as file:
 #read the first line to get rid of it
 file.readline()
 #read the lines containing genes information
 genes = file.readlines()
 #iterate over the generated list and store each gene into the dictionary
 dictionary = {}
 for gene in genes:
  gene_information = gene.split()
  if gene_information[0] in dictionary:
   dictionary[gene_information[0]].append(gene_information[1])
  else:
   dictionary[gene_information[0]] = [gene_information[1]]

#implement the function
def gene_function(user_gene):
#check if user's gene is in the dictionary, if it is, display the information, else let the user know the input is invalid
 if user_gene in dictionary:
  #print the header of the table
  print(f"{user_gene} exons:")
  print("Start Stop")
  space = len("Start ")
  #iterate over each exon and print it
  for i in range(len(dictionary[user_gene])):
   exon = dictionary[user_gene][i].split(":")
   #variable we need in order to maintain an aesthetic look of columns by outputting the proper amount of spaces in the middle
   number_space = space-len(str(exon[0]))
   print(f"{exon[0]}{number_space*" "}{exon[1]}")
   i += 1
 else:
  print("The gene is not in the dictionary.")

#ask user for input
input_gene = input("Input a gene: ")
#call the function
gene_function(input_gene)
