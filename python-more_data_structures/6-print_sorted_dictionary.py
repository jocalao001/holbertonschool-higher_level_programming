#!/usr/bin/python3 
def print_sorted_dictionary(a_dictionary):
     # Loop through the sorted keys of the dictionary
    for k in sorted(a_dictionary.keys()):
        # Print the key and the value
        print("{}: {}".format(k, a_dictionary[k]))
        
