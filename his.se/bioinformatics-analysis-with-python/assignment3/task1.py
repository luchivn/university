import pandas
import matplotlib.pyplot as matpl
#function for the main requirement: reads expression data file and sets the first column as an index for the dataframe
def read_file():
 filename = input("Input the name of the file with Gene Expressions: ")
 dataframe = pandas.read_csv(filename, sep='\t',index_col=0)
 return dataframe #returns the generated dataframe
#function for the first task: generates a boxplot of each column and plots them on the same figure
def plot_boxplots(dataframe):
 matpl.figure() #creates figure
 dataframe.boxplot() #generates boxplots
 matpl.title("Gene Expression Boxplots") #adds title for intuitiveness
 matpl.ylabel("Expression Level") #provides labels for the Gene Expression axis for intuitiveness
 matpl.show() #shows the plot on user's screen
#function for the third task: asks the user for a gene name and plots it
def plot_users_gene(dataframe):
 user_gene = input("Input a gene name: ")
 #Checks whether the Gene name is valid or not
 if user_gene in dataframe.index:
  #if valid, provides the user with the Gene plot
  matpl.plot(dataframe.loc[user_gene]) #generates the plot for user's Gene
  matpl.title(f"Expression Levels of {user_gene}") #adds title for intuitiveness
  matpl.ylabel("Expression Level") #adds labels for intuitiveness
  matpl.show() #shows the plot on user's screen
 else:
  #if invalid, announces the user that the Gene is not found
  print("Gene not Found")
#the following code is "main", it incorporates all the previous functions
main_dataframe = read_file()
plot_boxplots(main_dataframe)
print(main_dataframe.describe()) #fulfills the second task
plot_users_gene(main_dataframe)