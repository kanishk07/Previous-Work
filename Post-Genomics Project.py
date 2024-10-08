# -*- coding: utf-8 -*-
"""Part 2.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zDH86qsRmjM_lRBDew3oTh06EY55wBC0

# 2.1
"""

import pandas as pd
binary = pd.read_csv('/content/FinalMergedMasterWithBinaryMatrix.csv')

binary.columns

binary

binary = binary.drop(columns=['chrom', 'left', 'ref_seq', 'alt_seq', 'VCF_ID_Tumor',
       'Patient_ID_Tumor', 'T#', 'VCF_ID_Normal', 'Patient_ID_Normal', 'N#'])

binary

binary_normal = binary.filter(like='Normal', axis=1)

binary_normal

sum_row_normal = binary_normal.sum()
sum_row_normal.name = 'Total_normal'
type(sum_row_normal)
#binary_normal = binary_normal.append(sum_row)
#binary_normal

binary_tumor = binary.filter(like='Tumor', axis=1)
binary_tumor

sum_row_tumor = binary_tumor.sum()
sum_row_tumor.name = 'Total_tumor'
sum_row_tumor
#binary_tumor = binary_tumor.append(sum_row_tumor)
#binary_tumor

df_normal = sum_row_normal.reset_index()
# Rename the columns appropriately
df_normal.columns = ['SNV', 'Total_normal']
df_normal['SNV'] = df_normal['SNV'].str.replace('_Normal', '')

df_normal

df_tumor = sum_row_tumor.reset_index()
# Rename the columns appropriately

df_tumor.columns = ['SNV', 'Total_tumor']
df_tumor['SNV'] = df_tumor['SNV'].str.replace('_Tumor', '')

df_combined_1 = pd.merge(df_normal, df_tumor)

df_combined_1

# Assuming df_combined_1 is your DataFrame
summary_statistics = df_combined_1.describe()

# Remove the 'count' row
summary_statistics = summary_statistics.drop('count')

# Rename '25%', '50%', '75%' with 'Q1', 'Q2', 'Q3'
summary_statistics = summary_statistics.rename(index={'25%': 'Q1', '50%': 'Q2', '75%': 'Q3', 'mean':'Mean', 'std': 'Standard Deviation', 'min': 'Minimum', 'max':'Maximum'})

summary_statistics

#df_combined_1 = pd.DataFrame({
#    'SNV': df,
#    'Total_normal': df_normal['Total_normal'],
#    'Total_tumor': df_tumor['Total_tumor']
#})

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(25, 10))

# Add log10 counts to the dataframe for plotting
df_combined_1['Log_Total_normal'] = df_combined_1['Total_normal'].apply(np.log10)
df_combined_1['Log_Total_tumor'] = df_combined_1['Total_tumor'].apply(np.log10)

# Sort the dataframe based on 'Log_Total_normal'
df_combined_sorted = df_combined_1.sort_values(by='Log_Total_tumor')

plt.figure(figsize=(25, 10))

# Scatter plot for normal samples
plt.scatter(df_combined_sorted['SNV'], df_combined_sorted['Log_Total_normal'], color='blue', label='Normal')

# Scatter plot for tumor samples
plt.scatter(df_combined_sorted['SNV'], df_combined_sorted['Log_Total_tumor'], color='red', label='Tumor')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Labelling
plt.title("Log Tumor SNV Count")
plt.xlabel('Unique SNV Name')
plt.ylabel('Log Total Count')
plt.legend()

# Show plot
plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
plt.show()

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(25, 10))

# Assume df_combined_1 has already the log columns added and sorted

# Create a sequence of numbers from 1 to the number of rows in df_combined_sorted
x_axis_values = range(1, len(df_combined_sorted) + 1)

plt.figure(figsize=(25, 10))

# Scatter plot for normal samples
plt.scatter(x_axis_values, df_combined_sorted['Log_Total_normal'], color='blue', label='Normal SNV Count')

# Scatter plot for tumor samples
plt.scatter(x_axis_values, df_combined_sorted['Log_Total_tumor'], color='red', label='Tumor SNV Count')

# Set x-axis ticks to show every index number
plt.xticks(x_axis_values)
plt.xticks(rotation=90)

# Labelling
plt.title("Total Counts for Normal vs. Tumor SNV by Patient Index")
plt.xlabel('Unique Patient ID')
plt.ylabel('Log10 SNV Total Count')
plt.legend()

# Show plot
plt.tight_layout()
plt.show()

"""# 2.1 (b)"""

import pandas as pd
binary = pd.read_csv('/content/FinalMergedMasterWithBinaryMatrix.csv')
binary

binary = binary.fillna(0)

binary.columns

binary = binary[binary.columns[0:10]]
binary = binary.drop([ 'VCF_ID_Tumor',
       'Patient_ID_Tumor', 'VCF_ID_Normal', 'Patient_ID_Normal'], axis=1)
binary.to_csv('/content/drive/MyDrive/Documents/UTEP/3rd Sem/Post-genomics/binary2.1b.csv')

binary = pd.read_csv('/content/drive/MyDrive/Documents/UTEP/3rd Sem/Post-genomics/binary2.1b.csv')
binary = binary.drop(['chrom', 'left', 'ref_seq', 'alt_seq'], axis=1)
binary

from matplotlib import pyplot as plt
plt.figure(figsize=(20, 10))
binary['T#'].plot(kind='line', figsize=(8, 4), title='T#')
binary['N#'].plot(kind='line', figsize=(8, 4), title='N#')

# Setting the axis labels as requested
plt.xlabel('SNV Count')
plt.ylabel('Patients')




# Add a title and legend
plt.title('SNV Count per Patient')
plt.legend()
plt.gca().spines[['top', 'right']].set_visible(False)

from matplotlib import pyplot as plt
import pandas as pd

# Assuming 'binary' is a DataFrame with two columns 'T#' and 'N#'
# which contain the data for 'Tumor' and 'Normal' patients respectively.

plt.figure(figsize=(20, 10))

# Create a boxplot
binary.boxplot(column=['T#', 'N#'])

# Setting the axis labels as requested
plt.xlabel('Patients')
plt.ylabel('SNV Count')

# Add a title and legend
plt.title('SNV Count per Patient')

# Hide the top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Show the plot
plt.show()

from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns  # For improved visual aesthetics

# Assuming 'binary' is a DataFrame with two columns 'T#' and 'N#'
# Replace 'binary' with the actual name of your DataFrame
# and ['T#', 'N#'] with the actual column names for tumor and normal counts.

plt.figure(figsize=(20, 10))

# Using seaborn's style for better aesthetics
sns.set(style="whitegrid")

# Create a boxplot with seaborn's enhanced visuals
sns.boxplot(data=binary[['T#', 'N#']], palette="Set2")

# Setting the axis labels and titles with more descriptive text and larger font sizes
plt.xlabel('Patient Group', fontsize=14, fontweight='bold')
plt.ylabel('SNV Count', fontsize=14, fontweight='bold')
plt.title('Boxplot of SNV Count per Patient Group', fontsize=16, fontweight='bold')

# Hide the top and right spines for a cleaner look
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Increase tick label size
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')

# Show the plot
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Assume 'data' is your DataFrame containing the necessary columns

# Set the seaborn style
sns.set(style="whitegrid")

# Choose a color palette
palette = sns.color_palette("Set2")

plt.figure(figsize=(20, 10))

# Plotting the lines with markers and using the color palette
# Replace 'T#' and 'N#' with your actual data columns
plt.plot('x_column', 'T#', data=binary['T#'], marker='o', color=palette[0], label='T#')
plt.plot('x_column', 'N#', data=binary['N#'], marker='o', color=palette[1], label='N#')

# Formatting the axes and labels
plt.xlabel('X-Axis Label', fontsize=14, fontweight='bold')
plt.ylabel('Y-Axis Label', fontsize=14, fontweight='bold')
plt.title('Your Plot Title', fontsize=16, fontweight='bold')

# Adjusting tick parameters
plt.xticks(fontsize=12, fontweight='bold')
plt.yticks(fontsize=12, fontweight='bold')

# Adding a legend
plt.legend()

# Show the plot
plt.show()

"""# 3.1"""

# Load the Fathmm CSV file
fathmm_df = pd.read_csv('/content/Fathmm_Score_Col.csv')

# Add 'chr' to the 'Chromosome' column
fathmm_df['Chromosome'] = 'chr' + fathmm_df['# Chromosome'].astype(str)

# Rename columns
fathmm_df.rename(columns={'Chromosome': 'chrom',
                          'Position': 'left',
                          'Ref. Base': 'ref_seq',
                          'Mutant Base': 'alt_seq'}, inplace=True)

fathmm_df

import pandas as pd



# Load the aml_expand CSV file
aml_expand_df = pd.read_csv('/content/AML_Expand.csv')

# Merge the two dataframes
merged_df = pd.merge(fathmm_df, aml_expand_df, on=['chrom', 'left', 'ref_seq', 'alt_seq'])

# Save the merged dataframe to a new CSV file
merged_df.to_csv('/content/drive/MyDrive/Documents/UTEP/3rd Sem/Post-genomics/merged_df.csv', index=False)

import pandas as pd

# Paths to the CSV files
normal_file = "/content/normal_Final.csv"
tumor_file = "/content/tumor_Final.csv"

# A. Subsetting and processing
# Read Normal and Tumor CSV files, select specific columns
normal_df =pd.read_csv(normal_file, usecols=["chrom", "left", "ref_seq", "alt_seq", "Patient_ID", "VCF_ID"])
tumor_df = pd.read_csv(tumor_file, usecols=["chrom", "left", "ref_seq", "alt_seq", "Patient_ID", "VCF_ID"])

#print(normal_df)
#print(tumor_df)

# i. How many unique normal patients?
total_normal_patients = normal_df["Patient_ID"]
#print(total_normal_patients)
#print("Number of total normal patients:",len(total_normal_patients))
unique_normal_patients = total_normal_patients.drop_duplicates()
#print(unique_normal_patients)
print("Number of unique normal patients:",len(unique_normal_patients))

# ii. How many unique tumor patients?
total_tumor_patients = tumor_df["Patient_ID"]
#print(total_tumor_patients)
#print("Number of total tumor patients:",len(total_tumor_patients))
unique_tumor_patients = total_tumor_patients.drop_duplicates()
#print(unique_tumor_patients)
print("Number of unique tumor patients:",len(unique_tumor_patients))

#Total number of unique patients:
Total = pd.concat([normal_df[["Patient_ID"]],tumor_df[["Patient_ID"]]],axis=0, ignore_index=False)
#print("Total of normal and tumor patients:",len(Total))
unique_patients = Total.drop_duplicates()
#print("Total number of unique patients:",len(unique_patients))

# iii. Group by variant info and aggregate other columns into lists
grouped_normal = normal_df.groupby(["chrom", "left", "ref_seq", "alt_seq"], as_index=False).agg(list)
#print(grouped_normal)
#print(len(grouped_normal))
grouped_tumor = tumor_df.groupby(["chrom", "left", "ref_seq", "alt_seq"], as_index=False).agg(list)
#print(grouped_tumor)
#print(len(grouped_tumor)) ##When printing this getting len as 1573.

# iv. Create new columns for the number of patients per variant
grouped_normal["N#"] = grouped_normal["Patient_ID"].apply(len)
grouped_tumor["T#"] = grouped_tumor["Patient_ID"].apply(len)

# v. Rename columns
grouped_normal.rename(columns={"Patient_ID": "Patient_ID_Normal", "VCF_ID": "VCF_ID_Normal"}, inplace=True)
grouped_tumor.rename(columns={"Patient_ID": "Patient_ID_Tumor", "VCF_ID": "VCF_ID_Tumor"}, inplace=True)



# B. Merging Normal and Tumor
merged_df = pd.merge(grouped_tumor, grouped_normal, on=["chrom", "left", "ref_seq", "alt_seq"], how="outer")

# Save the merged DataFrame to a CSV file named "AML"
merged_df.to_csv("AML.csv", index=False)



###STEP -I (GET Fathmm_Input)


import pandas as pd

df = pd.read_csv("D:\Post-Genomic Project\Final_Merged.csv", sep= ',')


df['numeric_chrom'] = df['chrom'].str.extract(r'(\d+|[XY])')


#normal['numeric_chrom'] = normal['chrom'].str.extract('(\d+|[XY])') #Got error

def generate_txt(df,output_file):
     with open(output_file, "w") as txt_file:
          for index, row in df.iterrows():
               txt_file.write(f"{row['numeric_chrom']},{row['left']},{row['ref_seq']},{row['alt_seq']}\n")


generate_txt(df,output_file= "D:\Post-Genomic Project\FATHMM_Input.txt")

###STEP -II (Filtering _Pathogenic_Coding_Non-Coding

import pandas as pd

# Function to filter and save data
def filter_and_save(csv_file_path, filtered_csv_path):
    # Read the CSV file
    df = pd.read_csv(csv_file_path, sep=',')

    # Convert 'Coding Score' and 'Non-Coding Score' columns to numeric (ignoring errors)
    df['Coding Score'] = pd.to_numeric(df['Coding Score'], errors='coerce')
    df['Non-Coding Score'] = pd.to_numeric(df['Non-Coding Score'], errors='coerce')

    # Filter rows based on coding-score or non-coding score greater than or equal to 0.5
    filtered_df = df[(df['Coding Score'] >= 0.5) | (df['Non-Coding Score'] >= 0.5)]

    # Save the filtered DataFrame to a new CSV file
    filtered_df.to_csv(filtered_csv_path, sep=',', index=False)

    print(f"Filtered data saved to {filtered_csv_path}")

# File paths
csv_file_path = "D:\\Post-Genomic Project\\Fathmm_Output.csv"

# Apply filtering for Fathmm Normal
filtered_csv_path = "D:\\Post-Genomic Project\\Fathmm_Filtered_Coding_Non-coding_pathogenic.csv"
filter_and_save(csv_file_path, filtered_csv_path)




###STEP -III(Total_Score_Coding_Non-Coding

import pandas as pd
import numpy as np
csv_file_path = "D:\\Post-Genomic Project\\Fathmm_Filtered_Coding_Non-coding_pathogenic.csv"
df = pd.read_csv(csv_file_path, sep=',')



df['scoreCol'] = df['Coding Score'].fillna(0) + df['Non-Coding Score'].fillna(0)
df['scoreCol'] = np.where(df['Coding Score'].notna(), df['Coding Score'], df['Non-Coding Score'].fillna(0))
df['scoreCol'] = df[['Coding Score', 'Non-Coding Score']].mean(axis=1, skipna=True)
df['scoreCol'] = df['Coding Score'].fillna('').astype(str)  + df['Non-Coding Score'].fillna('').astype(str)



print(df)
df.to_csv("D:\\Post-Genomic Project\\Fathmm_Score_Col.csv", sep=",", index=False)



###STEP -IV (Merge FATHmm_Score col file and aml expand file)
import pandas as pd

# Load the Fathmm CSV file
fathmm_df = pd.read_csv('path/to/Fathmm.csv')

# Add 'chr' to the 'Chromosome' column
fathmm_df['Chromosome'] = 'chr' + fathmm_df['Chromosome'].astype(str)

# Rename columns
fathmm_df.rename(columns={'Chromosome': 'chrom',
                          'Position': 'left',
                          'Ref.Base': 'ref_seq',
                          'Mutant Base': 'alt_seq'}, inplace=True)

# Load the aml_expand CSV file
aml_expand_df = pd.read_csv('path/to/aml_expand.csv')

# Merge the two dataframes
merged_df = pd.merge(fathmm_df, aml_expand_df, on=['chrom', 'left', 'ref_seq', 'alt_seq'])

# Save the merged dataframe to a new CSV file
merged_df.to_csv('path/to/merged_file.csv',index=False)


###STEP-V (merge merged df file and the file which has #T and #N
##3 use cut-off as 0.5

csv = "/content/merged_merge_aml.csv"
cutoff = 0.5
def Q_gene(csv, scoreCol, cutoff, inequality, output):
    # Take away the unknown values from the Column that is being scored
    csv = csv[csv[scoreCol] != "Unknown"]
    csv = csv[csv[scoreCol] != "None"]
    csv = csv[csv[scoreCol] != ""]
    csv = csv[csv["BIOTYPE"] == "protein_coding"]
    # csv = csv[csv["NonSyn_or_Syn"] == "Non-Syn"] # Project wants for all protein coding SNV

    csv[scoreCol] = csv[scoreCol].astype(float)

    # parsing the rows with cutoff value and inequality:
    if inequality == "greater":
        csv = csv[csv[scoreCol] >= cutoff]
    elif inequality == "less":
        csv = csv[csv[scoreCol] <= cutoff]
    else:
        print("Invalid inequality parameters entry, must be 'greater' or 'less' equal to.")
        return

    # First tier, unique genes with the transcript list:
    csv1 = csv[["SYMBOL", "Feature"]]

    # Second tier,
    csv0 = csv[
        ["chrom", "left", "ref_seq", "alt_seq", "Feature", "Protein_position", "CDS_position", "T#", "N#", scoreCol]]

    csv2 = csv0.groupby("Feature", as_index=False).agg(list)
    csv3 = pd.merge(csv1, csv2, how="left", on="Feature")
    csv4 = csv3.groupby("SYMBOL", as_index=False).agg(list)

    score = []
    for row in range(csv4.shape[0]):

        # number of unique transcripts per gene
        Ng = len(csv4["Feature"][row])

        # list of list that need to be iterated thorugh in next loop
        row_score = csv4[scoreCol][row]
        row_tumor = csv4["T#"][row]
        row_normal = csv4["N#"][row]
        count = 1
        if scoreCol == "Provean":
            row_length = csv4["Protein_position"][row]
        else:
            row_length = csv4["CDS_position"][row]
        sum1 = 0
        for (i, j, k, g) in zip(row_score, row_tumor, row_normal, row_length):
            sum2 = 0
            for (s, t, n, l) in zip(i, j, k, g):
                count += 1
                # temp = 0
                l = l.split("/")
                l1 = int(l[-1])
                temp = s * (t - n)
                temp = temp / math.log(l1)
                sum2 += temp
            sum1 += sum2

        score1 = sum1 / Ng

        score.append(score1)
    csv4.insert(csv4.shape[1], "Q(Gene)", score)
    csv4 = csv4[["SYMBOL", "Q(Gene)"]]
    print(csv4)

#csv4.to_csv(output, sep=",", index=False)
