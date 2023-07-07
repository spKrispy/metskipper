import pandas as pd
import os
import glob

output_path = "/media/bioinfoa/bioinfo2/cluster_vcfs/slice_vcf2"
merged_output_file = "/media/bioinfoa/bioinfo2/cluster_vcfs/merged_output_hotspot.csv"

file_pattern = os.path.join(output_path, "*.csv")
file_list = glob.glob(file_pattern)

dfs = []
for file in file_list:
    df = pd.read_csv(file)
    filename = os.path.basename(file)
    df['Filename'] = filename
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)
merged_df.to_csv(merged_output_file, index=False)

