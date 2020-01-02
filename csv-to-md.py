# based on https://github.com/hfionte/csv_to_yaml

# Import the python library for parsing CSV files.
import csv
import glob

all_csvs = glob.glob('*.csv')

# open all CSVs
csvfile = open(all_csvs[0], 'r')

datareader = csv.reader(csvfile, delimiter=',', quotechar='"')

# Empty array for data headings, which we will fill with the first row from our CSV.
data_headings = []
# filename_column = []

# Loop through each row...
for row_index, row in enumerate(datareader):

    # If this is the first row, populate our data_headings variable.
    if row_index == 0:
        data_headings = row

    # Otherwise, create a Markdown file from the data in this row
    else:
        # Open a new file with filename based on index number of our current row.
        if row_index > 0:
            # change this integer to change what column the file name is based on
            fname = row[3]

        filename = str(fname.replace("jpg", "md")) 
        new_md = open(filename, "w")
        meta_separator = str("---")

        # Empty string that we will fill with md formatted text based on data extracted from our CSV.
        md_text = ""

        # Loop through each cell in this row...
        # skip tags
        for cell_index, cell in enumerate(row[:5]):

            if cell_index == 3:
                print(cell)

            # Compile a line of md text from our headings list and the text of the current cell, followed by a linebreak.
            # Heading text is converted to lowercase. Spaces are converted to underscores and hyphens are removed.

            # In the cell text, line endings are replaced with commas.
            # need to format tags correctly
            cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")
            cell_text = cell_heading + ": " + cell.replace("\n", ", ") + "\n"

            # Add this line of text to the current md string.
            md_text += cell_text

        for cell_index, cell in enumerate(row[+6:]):

            cell_heading = data_headings[cell_index].lower().replace(" ", "_").replace("-", "")
            # this is a pretty janky way to do this
            tag_text = cell_heading + ": " + cell.replace(" -", "\n" + "\t" + "- ") + "\n"


            print(tag_text)


            md_text += tag_text

        # Write our md string to the new text file and close it.
        new_md.write(meta_separator + "\n" + md_text + meta_separator +"\n")
        new_md.close()

# We're done! Close the CSV file.
csvfile.close()