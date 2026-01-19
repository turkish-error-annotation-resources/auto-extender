import pandas as pd
from sklearn.metrics import cohen_kappa_score


# evaluation of combined Cohen's Kappa score for manual annotations
def calculate_combined_kappa(file1_path, file2_path):
    # loading excel files
    # header=0 -> assumes the first row is the header.
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)

    # data validation (Are row counts equal?)
    if len(df1) != len(df2):
        print(f"Warning: File row counts are not equal! ({len(df1)} vs {len(df2)})")
        return

    # target column indices (0-based indexing: 8, 9, 10, 11, 12)
    # 8: POS, 9: Inflectional Feature, 10: Lexical Feature, 11: Unit, 12: Phenomenon
    target_columns_indices = [8, 9, 10, 11, 12]

    # data pre-processing
    # selecting relevant columns for both files and concatenate them into a single string.
    # combined labels for Annotator 1
    annotator1_labels = df1.iloc[:, target_columns_indices].astype(str).agg('-'.join, axis=1)
    # combined labels for Annotator 2
    annotator2_labels = df2.iloc[:, target_columns_indices].astype(str).agg('-'.join, axis=1)

    # calculating Cohen's Kappa
    kappa_score = cohen_kappa_score(annotator1_labels, annotator2_labels)

    # Simple Agreement Rate (Accuracy) - What percentage is exactly the same?
    agreement_count = (annotator1_labels == annotator2_labels).sum()
    agreement_ratio = agreement_count / len(df1)

    # Print Results
    print("-" * 30)
    print(f"Total Data Count: {len(df1)}")
    print(f"Exact Match Row Count: {agreement_count}")
    print(f"Simple Agreement Rate (Agreement %): {agreement_ratio:.4f}")
    print("-" * 30)
    print(f"Global Cohen's Kappa Score: {kappa_score:.4f}")
    print("-" * 30)
    print("#######################################################")

# evaluation of system outputs against human annotations (facet-wise)
def eval_facet_wise_accuracy(file_path_tool_annotated, file_path_human_annotated, col_idx, show_diffs):
    # loading excel files
    df1 = pd.read_excel(file_path_tool_annotated)
    df2 = pd.read_excel(file_path_human_annotated)

    # selecting the target columns and handling missing values
    # replacing NaNs with a string placeholder "_NaN_" because normally np.nan != np.nan in Python
    col1 = df1.iloc[:, col_idx].fillna("_NaN_")
    col2 = df2.iloc[:, col_idx].fillna("_NaN_")

    # calculating the number of mismatches
    difference_count = (col1 != col2).sum()

    if show_diffs:
        print("#######################################################")
        # creating a boolean mask for rows where the values differ
        diff_mask = col1 != col2
        differences = pd.DataFrame({
            "Index": df1.index[diff_mask],
            "System Output": col1[diff_mask],
            "Human Output": col2[diff_mask]
            })
        print(differences.to_string(index=False))
    
    # showing statistics
    print(f"Number of total rows: ", len(col1))
    print(f"Number of mismatched cells in column {col_idx}: ", difference_count)

    acc = (len(col1) - difference_count) / len(col1)
    print(f"Accuracy: ", acc)
    print("#######################################################")

    return acc

# evaluation of system outputs against human annotations (exact-match)
def eval_exact_match_accuracy(file_path_tool_annotated, file_path_human_annotated, col_idxs):
    # loading excel files
    df1 = pd.read_excel(file_path_tool_annotated)
    df2 = pd.read_excel(file_path_human_annotated)

    # selecting the target columns and handling missing values
    # replacing NaNs with a string placeholder "_NaN_" because normally np.nan != np.nan in Python
    col1 = df1.iloc[:, col_idxs].fillna("_NaN_")
    col2 = df2.iloc[:, col_idxs].fillna("_NaN_")

    # checking if any facet differs in each row
    row_diff_mask = (col1 != col2).any(axis=1)

    total_rows = len(col1)
    diff_rows = row_diff_mask.sum()

    print(f"Number of total rows: ", len(col1))
    print(f"Number of annotations with at least one facet difference: {diff_rows}")
    print(f"Annotation-level exact match count: {total_rows - diff_rows}")
    print(f"Annotation-level accuracy: {(total_rows - diff_rows) / total_rows:.4f} ({(1 - diff_rows/total_rows)*100:.2f}%)")


if __name__ == "__main__":
    
    # paths to the manual annotation excel files for two annotators
    file1 = "/Users/tolgahanturker/Desktop/auto-filler/taxonomy-auto-filler/eval/manual_annotation_annotator1.xlsx"
    file2 = "/Users/tolgahanturker/Desktop/auto-filler/taxonomy-auto-filler/eval/manual_annotation_annotator4.xlsx"
    calculate_combined_kappa(file1, file2)
    
    # evaluation of system outputs against human annotations (facet-wise)
    system_output_file = "/Users/tolgahanturker/Desktop/auto-filler/taxonomy-auto-filler/eval/system_output.xlsx"
    human_annotation_file = "/Users/tolgahanturker/Desktop/auto-filler/taxonomy-auto-filler/eval/manual_annotation_annotator1.xlsx" # expert annotator
    # col_idx: 8-POS, 9-IF, 10-LF, 11-UNIT, 12-PHENOMENON
    acc8 = eval_facet_wise_accuracy(system_output_file, human_annotation_file, col_idx=8, show_diffs=False)
    acc9 = eval_facet_wise_accuracy(system_output_file, human_annotation_file, col_idx=9, show_diffs=False)
    acc10 = eval_facet_wise_accuracy(system_output_file, human_annotation_file, col_idx=10, show_diffs=False)
    acc11 = eval_facet_wise_accuracy(system_output_file, human_annotation_file, col_idx=11, show_diffs=False)
    acc12 = eval_facet_wise_accuracy(system_output_file, human_annotation_file, col_idx=12, show_diffs=False)
    macro_avg = (acc8 + acc9 + acc10 + acc11 + acc12) / 5
    print(f"Macro Average Accuracy across facets: {macro_avg:.4f}")
    print("#######################################################")

    # evaluation of system outputs against human annotations (exact-match)
    eval_exact_match_accuracy(system_output_file, human_annotation_file, col_idxs=[8,9,10,11,12])