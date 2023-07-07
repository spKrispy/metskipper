regions = [
    (116411865, 116411890, '_hotspot'),
    (116411868, 116411886, '_hotspot'),
    (116411868, 116411903, '_hotspot'),
    (116411875, 116411889, '_hotspot'),
    (116411876, 116411897, '_hotspot'),
    (116411881, 116411901, '_hotspot'),
    (116411882, 116411898, '_hotspot'),
    (116411883, 116411902, '_hotspot'),
    (116411883, 116411904, '_hotspot'),
    (116411883, 116411954, '_hotspot'),
    (116411884, 116411900, '_hotspot'),
    (116411885, 116411895, '_hotspot'),
    (116411885, 116411896, '_hotspot'),
    (116411885, 116411901, '_hotspot'),
    (116411887, 116414938, '_hotspot'),
    (116411896, 116411935, '_hotspot'),
    (116411901, 116411930, '_hotspot'),
    (116411903, 116412043, '_hotspot'),
    (116411903, 116412043, '_hotspot'),
    (116411990, 116411990, '_hotspot'),
    (116411986, 116411986, '_hotspot'),
    (116411972, 116411972, '_hotspot'),
    (116411974, 116411974, '_hotspot'),
    (116411975, 116411975, '_hotspot'),
    (116411918, 116411918, '_hotspot'),
    (116411918, 116412110, '_hotspot'),
    (116411920, 116411955, '_hotspot'),
    (116412044, 116412044, '_hotspot'),
    (116412044, 116412044, '_hotspot'),
    (116412044, 116412044, '_hotspot'),
    (116412044, 116412044, '_hotspot'),
    (116412044, 116412044, '_hotspot'),
    (116412044, 116412052, '_hotspot'),
    (116412045, 116412045, '_hotspot'),
    (116412045, 116412045, '_hotspot')
]

import pandas as pd
import os

input_path = "/media/bioinfoa/bioinfo2/cluster_vcfs/transfer_vcf/t_vcfs"
output_path = "/media/bioinfoa/bioinfo2/cluster_vcfs/slice_vcf3"

files = os.listdir(input_path)
os.chdir(input_path)

def process_file(file):
    try:
        vcf_file = pd.read_csv(file, sep='\t', comment='#', header=None)
        res_vcf = vcf_file[vcf_file[0] == 'chr7']
        
        for start, end, suffix in regions:
            final_df = res_vcf[(res_vcf[1] >= start) & (res_vcf[1] <= end)]
            
            if not final_df.empty:
                file_name = file + suffix + '.csv'
                print(f'{file_name}  - Done')
                out_file = os.path.join(output_path, file_name)
                final_df.to_csv(out_file, index=False)
        
    except pd.errors.EmptyDataError:
        pass

for file in files:
    process_file(file)

