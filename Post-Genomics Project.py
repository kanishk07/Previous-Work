import pandas as pd
import os

#INSERT CODE HERE
#Homework 3.A
#(i) Merge the 5 normal CSV files together and the 5 tumor CSV files, 
#result should 2 separate Dataframes, one with Normal variants and another with Tumor variants.

folder_path = 'D:\\Documents\\UTEP\\Sem 3\\Post-Genomics\\Project\\Normal\\Normal'

merged_data = pd.DataFrame()

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        merged_data = pd.concat([merged_data, df], axis = 0, ignore_index=True)

merged_data.to_csv('merged_data_normal.csv', index=False)

folder_path_tumor = 'D:\\Documents\\UTEP\\Sem 3\\Post-Genomics\\Project\\Tumor\\Tumor'

merged_data_tumor = pd.DataFrame()

for filename in os.listdir(folder_path_tumor):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path_tumor, filename)
        df = pd.read_csv(file_path)
        merged_data_tumor = pd.concat([merged_data_tumor, df], axis = 0, ignore_index=True)

merged_data_tumor.to_csv('merged_data_tumor.csv', index=False)

#SUGGESTION: Prior to coding, create 2 empty folders, Normal_CSV and Tumor_CSV, 
#manually move the 5 normal CSVs into the Normal_CSV folder, and then move
#the 5 tumor CSVs into the Tumor_CSV folder, this can be done 
#by using the search bar in the Finder(Mac) or Folder(Windows) app. 
#The script can then point to the directory (similar to HW1) to read and merge the files within, 
#using a function within the pandas (pd) package.

#Reading in a CSV file Example:
#DataFrame1 = pd.read_csv("DataFrame1.csv")

#Merging Example:
#newDataFrame = pd.concat(DataFrame1, DataFrame2, axis=0) 

# Function adds in alt_seq column to, input is a dataframe and function returns a dataframe
def addALT_Seq(csv):
    alt = []
    for row in range(csv.shape[0]):
        ref_seq = csv["ref_seq"][row]
        if ref_seq == csv["var_seq1"][row]:
            alt.append(csv["var_seq2"][row])
        else:
            alt.append(csv["var_seq1"][row])
    csv.insert(csv.shape[1], "alt_seq", alt)
    return csv


#INSERT CODE HERE
#Homework 3.A
#(ii) Using the output from A(i), run the addALT_Seq() function:
#Example:

normal_newDataFrame_withALTseq = addALT_Seq(merged_data)
normal_newDataFrame_withALTseq

tumor_newDataFrame_withALTseq = addALT_Seq(merged_data_tumor)
tumor_newDataFrame_withALTseq


#INSERT CODE HERE
#Homework 3.A
#(iii) Using the output from A(ii), remove duplicates based on the given columns:
#[“chrom”, “left”, “ref_seq”, “alt_seq”, “Patient_ID”]
#Save the two DataFrames as: Final_Normal and Final_Tumor

normal_Final = normal_newDataFrame_withALTseq.drop_duplicates(['chrom', 'left', 'ref_seq', 'alt_seq', 'Patient_ID'])
normal_Final.to_csv('normal_Final.csv', index=False)

tumor_Final = tumor_newDataFrame_withALTseq.drop_duplicates(['chrom', 'left', 'ref_seq', 'alt_seq', 'Patient_ID'])
tumor_Final.to_csv('tumor_Final.csv', index=False)

#Remove Duplicates Example:
#Final = newDataFrame_withALTseq.drop_duplicates(columns)

unique_normal_patients = normal_Final['Patient_ID'].unique()
#unique_normal_patients = pd.DataFrame(unique_normal_patients)
print(len(unique_normal_patients))

unique_tumor_patients = tumor_Final['Patient_ID'].unique()
print(len(unique_tumor_patients))

#Merge normal_Final and tumor_Final
import pandas as pd
normal_Final = pd.read_csv('normal_Final.csv')
tumor_Final = pd.read_csv('tumor_Final.csv')

grouped_normal = normal_Final.groupby(['chrom', 'left', 'ref_seq', 'alt_seq']).agg(list).reset_index()
grouped_normal

grouped_tumor = tumor_Final.groupby(['chrom', 'left', 'ref_seq', 'alt_seq']).agg(list).reset_index()
grouped_tumor


# (iv):-
n = []
for row in range(grouped_normal.shape[0]):
        temp = len(grouped_normal['Patient_ID'][row])
        n.append(temp)
n

t = []
for row in range(grouped_tumor.shape[0]):
        temp = len(grouped_tumor['Patient_ID'][row])
        t.append(temp)
t

# Update the 'N#' column based on 'Patient_ID' counts
grouped_normal['N#'] = n
grouped_normal

# Update the 'N#' column based on 'Patient_ID' counts
grouped_tumor['T#'] = t
grouped_tumor

# (v) 
grouped_normal.rename(columns={'Patient_ID': 'Patient_ID_Normal', 'VCF_ID': 'VCF_ID_Normal'}, inplace=True)
grouped_normal.to_csv('grouped_normal.csv')

grouped_tumor.rename(columns={'Patient_ID': 'Patient_ID_Tumor', 'VCF_ID': 'VCF_ID_Tumor'}, inplace=True)
grouped_tumor.to_csv('grouped_tumor.csv')

# B 
merged_grouped =  pd.merge(grouped_tumor, grouped_normal, on=["chrom", "left", "ref_seq", "alt_seq"], how="outer")
merged_grouped
merged_grouped.to_csv('AML_C.csv')