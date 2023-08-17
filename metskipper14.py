#!/usr/bin/python3

import argparse
import os
import csv

# Define the boundary of MET exon 14
exon14_start = 116411903
exon14_end = 116412043


# Parse command-line arguments
import argparse
parser = argparse.ArgumentParser(description="Detect MET exon 14 skipping.")
parser.add_argument("-i", "--input", type=str, help="Input SJ file path")
args = parser.parse_args()


# Initialize variables
exon14_skipped = False
spliced_out_portions = []
splice_junction_coordinates = []
results=[]


# Create output file name
output_file = os.path.splitext(args.input)[0] + "_output.tab"

# Read the SJ.out.tab file
with open(args.input, "r") as file:
    for line in file:
        # Split the line into columns
        columns = line.strip().split("\t")
        
        # Extract relevant information
        contig = columns[0]
        splice_start = int(columns[1])
        splice_end = int(columns[2])
        unique_mapping_reads = int(columns[6])

        
        # Check if the splice junction overlaps with MET exon 14
        if contig == "chr7" and ((exon14_start <= splice_start <= exon14_end) or (exon14_start <= splice_end <= exon14_end) or (splice_start <= exon14_start and splice_end >= exon14_end)):
        
            exon14_skipped = True
            
            # Calculate the portion of exon 14 spliced out
            if splice_start <= exon14_start and splice_end >= exon14_end:
                spliced_out_portion = 1.0
            elif splice_start >= exon14_start and splice_end <= exon14_end:
                spliced_out_portion = (splice_end - splice_start + 1) / (exon14_end - exon14_start + 1)
            else:
                intersection_start = max(splice_start, exon14_start)
                intersection_end = min(splice_end, exon14_end)
                spliced_out_portion = (intersection_end - intersection_start + 1) / (exon14_end - exon14_start + 1)
            
            # Save the splice junction coordinates and spliced out portion
            splice_junction_coordinates.append(f"{splice_start}-{splice_end}")
            spliced_out_portions.append(spliced_out_portion)
            results.append([splice_start, splice_end, spliced_out_portion, unique_mapping_reads])
        
# Print the results
if exon14_skipped:
    if len(splice_junction_coordinates) > 1:
        print("MET exon 14 skipping detected in multiple hits.")
    else:
        print("MET exon 14 skipping detected in a single hit.")
    
    for i in range(len(splice_junction_coordinates)):
        print("Hit", i+1)
        print("Portion of exon 14 spliced out: {:.2%}".format(spliced_out_portions[i]))
        print("Splice Junction Coordinates: " + splice_junction_coordinates[i])
        print()
else:
    print("MET exon 14 skipping not detected.")




# Write results to the output file
with open(output_file, "w", newline="") as output:
    writer = csv.writer(output, delimiter="\t")
    
    if exon14_skipped:
        writer.writerow(["splice_start", "splice_end", "portion_spliced", "unique_mapping_reads"])
        
        for result in results:
            writer.writerow(result)
    else:
        writer.writerow(["MET exon 14 skipping not detected."])

print("Results saved in " + output_file)
