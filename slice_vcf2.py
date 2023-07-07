import pandas as pd
import os

input_path = "/media/bioinfoa/bioinfo2/cluster_vcfs/transfer_vcf/t_vcfs"
output_path = "/media/bioinfoa/bioinfo2/cluster_vcfs/slice_vcf2"

files = os.listdir(input_path)
os.chdir(input_path)

def process_file(file):
    try:
        vcf_file = pd.read_csv(file, sep='\t', comment='#', header=None)
        res_vcf = vcf_file[vcf_file[0] == 'chr7']
        
        regions = [
            (116411705, 116411711, '_13_end_AG'),
            (116411900, 116411906, '_14_start_GT'),
            (116412040, 116412046, '_14_end_AG'),
            (116414932, 116414938, '_15_start_GT')
        ]
        
        for start, end, suffix in regions:
            final_df = res_vcf[(res_vcf[1] >= start) & (res_vcf[1] <= end)]
            
            if not final_df.empty:
                file_name = file + suffix + '.csv'
                print(f'file_name - Done')
                out_file = os.path.join(output_path, file_name)
                final_df.to_csv(out_file, index=False)
        
    except pd.errors.EmptyDataError:
        pass

for file in files:
    process_file(file)
