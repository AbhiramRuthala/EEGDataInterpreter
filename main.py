#Input your frequency value (numericallu)
userinput1 = input("What frequency are your brain waves at? ")

#Inputting confirmed frequency values for EEG brain waves. I still have to fully update this part with all the confirmed frequencies.
matrix2 = [
    ["Alpha", "1", "2"],
    ["Beta", "10", "15"],
    ["Gamma", "25", "35"],
    ["Theta", "45", "55"],
    ["Delta", "75", "85"]
]

#Using a dictionary to identify KeyValues and use that within our concatenation.
frequency = {
    "1": "Alpha",
    "10": "Beta",
    "25": "Gamma",
    "45": "Theta",
    "75": "Delta"
}

#Within the 2D list (matrix2), we look at its contents.
for list in matrix2:
    check = userinput1 in list
#If the userinput value is within the list, this function runs with the userinput value corresponding to the dictionary plus the other string concatenation.
    if check == True:
        print(frequency.get(userinput1) + " " + "waves present!")
    else:
        print("Invalid frequency input!")
