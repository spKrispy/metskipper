# ***METSkipper14***

### **Introduction**
METSkipper14 is a tool designed to detect MET exon 14 skipping events from RNA-seq data. The tool assumes that the Splice Junction is a region instead of just junction coordinates and checks how much the SJR and exon 14 are encompassing/overlapping each other to calculate the portion of skipped portion in reference to exon 14. An ideal proportion of skipping will be 100% with a good number of support reads. The tool takes filename.SJ.out.tab as input and generates filename.SJ.out_output.tab as output. The tool is available on GitHub, and users can fork the repository and make changes to the original code if required. METSkipper14 is a valuable tool for researchers and clinicians in the field of cancer research and treatment, as it can help identify molecular alterations like MET exon 14 skipping and personalize treatment approaches.

### **Usage**
```
python3 metskipper14.py -i samplename.SJ.out.tab
```


You can use the test data to check if the script is running fine. Please raise an issue if you face any difficulty.
