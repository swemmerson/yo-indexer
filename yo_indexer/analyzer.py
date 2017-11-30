"""Main module for yo_indexer"""
import csv
import os
from pkg_resources import resource_listdir

def examine_csv():
    """The main function"""
    # Gets a list of all of the files in the csv_files dir
    csv_dir = resource_listdir('yo_indexer.csv_files', '')
    
    # Initialize the Yo index to a reasonable number that's not 0
    yoIndex = 10
    
    # Loop through them
    for file_name in csv_dir:

        # If it is a .csv then do stuff
        if file_name[-4:] == '.csv':
            print('Examining - ' + file_name)

            # Get the system file path
            file_path = os.path.join(os.path.dirname(__file__), 'csv_files/' + file_name)
            # Initialize the UI options total to 0
            total = 0
            # Open the file
            with open(file_path) as csvfile:
                # Make csv reader
                reader = csv.reader(csvfile, delimiter=',', quotechar='|')

                # Output
                for row in reader:
                    for entry in row:
                        # Check if the entry is not empty
                        if len(entry) != 0:        
                            total += 1
                if file_name == 'Yo.csv':
                    # Update the Yo index value
                    yoIndex = total
           print('Yo Index: ' + total/yoIndex)
        else:
            print('Skipping - ' + file_name)
