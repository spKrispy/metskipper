import pandas as pd
import os
import glob2
from pandas.errors import EmptyDataError 
path1= "/media/bioinfoa/bioinfo2/cluster_vcfs/transfer_vcf"
files= os.listdir(path1)
out_path="/media/bioinfoa/bioinfo2/cluster_vcfs/slice_vcf"
os.chdir(path1)
for file in files:
    try:
        vcf_file=pd.read_csv(file,sep='\t',comment='#',header=None)
        res_vcf=vcf_file[vcf_file[0]=='chr7']
        final_df=res_vcf[(res_vcf[1]>=116411551) & (res_vcf[1] <= 116417443)]
        if not final_df.empty:
            file_names= file+'.csv'
            out_file= os.path.join(out_path, file_names)
            final_df.to_csv(out_file, index=False)
            del final_df
    except EmptyDataError:
        continue


