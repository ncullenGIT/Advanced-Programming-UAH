import pandas as pd # imports pandas
import matplotlib.pyplot as plt # imports matplotlib

filePath = "/Users/nicholascullen/Downloads/Electric_Vehicle_Population_Data.csv" # file
file = pd.read_csv(filePath) # use pandas to read file in

def plotEVmodels(make): # plots count vs model
    filteredData = file[file["Make"].str.lower() == make.lower()] # converts all values to lower case and stores the correct location of the row
    
    if filteredData.empty: # checks if the file contains model
        print("No data found for input make. Please type a valid make") # notifies user that the make was not found
        return
    
    modelQty = filteredData["Model"].value_counts() # counts how many times a model occurred 

    plt.figure(figsize=(10, 4)) # size of the figure
    modelQty.plot(kind = 'bar', color = 'red') # sets plots to red bars
    plt.title(f"Number of Electric Vehicle Models for {make} registered in Washington State") # chart title
    plt.xlabel("Model(s)") # chart x axis
    plt.ylabel("Count") # chart y axis
    plt.xticks(rotation = 35) # rotation of model labels
    plt.show() # shows plot 

def plotTopCounties(make): # plots top 5 counties with most registrations for given make
    filteredData = file[file["Make"].str.lower() == make.lower()] # converts all values to lower case and stores the correct location of the row
    
    if filteredData.empty: # checks if file is empty
        return
    
    countyQty = filteredData["County"].value_counts().nlargest(5) # gets top 5 counties
    
    plt.figure(figsize=(10, 4))
    countyQty.plot(kind = 'bar', color = 'green') # blue bars for county data
    plt.title(f"Top 5 Counties for {make} EV Registrations")
    plt.xlabel("Counties")
    plt.ylabel("Count")
    plt.xticks(rotation=35)
    plt.show()

def main():
    compare = "Yes" # sets default for if comparison
    while True: # loop to control make comparisons
        if (compare == "Yes"): # checks if user wants to compare a brand
            make = input("Enter the EV brand (make) you are interested in: ") # asks user to enter a make
            plotEVmodels(make) # calls function to plot ev models
            plotTopCounties(make) # calls function to plot top counties
        elif (compare == "No"): # checks if user wants to end comparisons
            break # breaks out of loop
        else: # default for is user does not answer with a valid respinse
            print("Please answer 'Yes' or 'No' when prompted") # reminds user to only answer yes or no
        compare = input("Would you like to compare to another make? (Yes or No) ") # asks if the user would like to continue comparing
    
    print("Thank you for using the program") # thanks user for utilizing program

main()

# File: "/Users/nicholascullen/Downloads/Electric_Vehicle_Population_Data.csv"
# CTRL+SHIFT+J for plots