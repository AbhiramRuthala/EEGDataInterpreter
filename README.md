**Predicting brain waves using the frequency value from non-stationary data of EEG recordings**

NOTE: This system is coded using the Python3 coding language

**Input:**
When the program is run, the input is taken by the user which is a number.

**Checking The List:**
This number will be checked across the entire list (matrix2 in the code) to see if that value is within the content of the list. This will be checked as either "True" or "False" by the variable "check" in the "if" statement in the bottom. If check is equal to True, then the function will print a value by checking for the input of the user in the "frequency" dictionary.

**Dictionary:**
A dictionary is a place to store values and "KeyValues." As shown in the code, the string on the right side of the colon is the KeyValue, while the left is the string that holds it. When calling for userinput, the **get** function in the _frequency.get()_ function will check for the value inputted for userinput and will print out the KeyValue of that string.

**String Concatenation:**
The _frequency.get_ function will return a string, which will then be grouped with the "waves present!" string to give a small sentence blurb at the end summarizing the predicted brain waves based on the frequency inputted.

**Potential Applications:**
This system mainly applies to medical practitioners and neurologists who spend tons of time interpreting electroencephalogram (EEG) waves at discrete data points to conduct diagnosis or learn more about patients. This will make the process simpler by allowing for the categorization of the brain wave data within the EEG session when taking certain parts of the data (The frequency).
