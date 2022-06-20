# The data we need to retrieve
import os
import csv

# Assign a variable for the file to load and th path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file path
file_to_save = os.path.join("Resources", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load, 'r') as election_data:


# To do: Read and analyze data here

# Read the file object with the reader function

    file_reader = csv.reader(election_data)

# Print each row in the csv file

    headers = next(file_reader)
    print(headers)



# # 1. The total number of votes cast
# # 2. A complete list of candidates who received votes
# # 3. The percentage of votes each candidate won
# # 4. The total number of votes each candidate won
# # 5. The winner of election based on popular vote



# # Print file object
#     print(election_data)



# file_to_save = os.path.join("analysis", "election_analysis.txt")
# open(file_to_save, "w")




























# #PRACTICEBELOW
# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Use the open statement to open the file as a text file
# with open (file_to_save, "w") as txt_file:

# # Wrtie some data to the file
#     txt_file.write("Counties in the Election\n----------------\n")
#     txt_file.write("Hello World\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")











