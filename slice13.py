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
        final_df13=res_vcf[(res_vcf[1]>=116411705) & (res_vcf[1] <= 116411711)]
        final_df14start=res_vcf[(res_vcf[1]>=116411900) & (res_vcf[1] <= 116411906)]
        final_df14=final_df14start.append(res_vcf[(res_vcf[1]>=116412040) & (res_vcf[1] <= 116412046)])
        final_df15=res_vcf[(res_vcf[1]>=116414932) & (res_vcf[1] <= 116414938)]
        if not final_df13.empty:
            print(file)
            file_name13= file+'_13.csv'
            file_name14= file+'_14.csv'
            file_name15 = file + '_15.csv'
            out_file13= os.path.join(out_path, file_name13)
            out_file14=os.path.join(out_path, file_name14)
            out_file15=os.path.join(out_path, file_name15)

            final_df13.to_csv(out_file13, index=False)
            final_df14.to_csv(out_file14, index=False)
            final_df15.to_csv(out_file15,index= False)

            
            del final_df13
            del final_df14
            del final_df15
    except EmptyDataError:
        continue
