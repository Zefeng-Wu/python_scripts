#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None

p = "CAGCT"
q = "AGGT"
m = len(p)
n = len(q)

# 创建一个替换矩阵(build a substitution matrix)
bases = ["A","G","C","T"]
rep_arrary = np.zeros((4,4),dtype=int)
rep_matrix = df = pd.DataFrame(rep_arrary, index=bases, columns=bases)
rep_matrix["A"] = [10,-1,-3,-4] # get column values
rep_matrix["G"] = [-1,7,-5,-3]
rep_matrix["C"] = [-3,-5,9,0]
rep_matrix["T"] = [-4,-3,0,8]
gap = -5

# 打印替换矩阵（Output the substitution matrix）
print("0.Substitution matrix is:","\n",rep_matrix,"\n")

# 创建一个得分矩阵(build a score matrix)
score_arrary = np.zeros((n+1,m+1),dtype=int)
score_matrix_colnames = ["-"]+[_ for _ in p]
score_matrix_rownames = ["-"]+[_ for _ in q]
score_matrix = pd.DataFrame(score_arrary,index=score_matrix_rownames,columns=score_matrix_colnames)


# 初始化得分矩阵(initiating the score matrix)
score_matrix["-"][0] = 0
score_matrix.iloc[0] = [x*gap for x in range(m+1)] # first line
score_matrix.iloc[:,0] = [x*gap for x in range(n+1)] # first column

# 创建一个回溯矩阵(build a trace matrix)
trace_arrary = np.zeros((n+1,m+1),dtype=str)
trace_matrix_colnames = ["-"]+[_ for _ in p]
trace_matrix_rownames = ["-"]+[_ for _ in q]
trace_matrix = pd.DataFrame(trace_arrary,index=score_matrix_rownames,columns=score_matrix_colnames)
trace_matrix.iloc[0,1:] = "left_gap"
trace_matrix.iloc[1:,0] = "up_gap"

# 计算得分矩阵元素和回溯矩阵元素(Calculate the all elements of score matrix and trace matrix)
for idx_row in range(1,n+1):
    for idx_col in range(1,m+1):
        #print(idx_row,idx_col)
        w_ij =  rep_matrix.loc[score_matrix.index[idx_row],score_matrix.columns[idx_col]] # get match or mismatch score [with col and row name]
        match_path_score = score_matrix.iloc[idx_row-1,idx_col-1]+ w_ij
        horit_path_score = score_matrix.iloc[idx_row,idx_col-1] + gap
        verti_path_socre = score_matrix.iloc[idx_row-1,idx_col,] + gap
        score_matrix.iloc[idx_row,idx_col] = max(match_path_score,horit_path_score,verti_path_socre)
        
        # record best path
        if [match_path_score,horit_path_score,verti_path_socre].index(score_matrix.iloc[idx_row,idx_col])==0:
            trace_matrix.iloc[idx_row,idx_col] = "match"
        if [match_path_score,horit_path_score,verti_path_socre].index(score_matrix.iloc[idx_row,idx_col])==1:
            trace_matrix.iloc[idx_row,idx_col] = "left_gap"
        if [match_path_score,horit_path_score,verti_path_socre].index(score_matrix.iloc[idx_row,idx_col])==2:
            trace_matrix.iloc[idx_row,idx_col] = "up_gap" 
# 输出得分矩阵 (Output score matrix)            
print("1.Score matrix is:","\n",score_matrix,"\n")

# 输出回溯矩阵 (Output trace matrix)
print("2.Trace matrix is:","\n",trace_matrix,"\n")
 
# 回溯回溯矩阵，得出比对结果(Trace the trace matric and get alignment result)
p_align = []
q_align = []

temp_row_index = n
temp_col_index = m
while (temp_row_index>=1 and temp_col_index>=1):
    if trace_matrix.iloc[temp_row_index,temp_col_index]=="match":
        p_align.append(trace_matrix.columns[temp_col_index])
        q_align.append(trace_matrix.index[temp_row_index])
        temp_col_index=temp_col_index-1
        temp_row_index=temp_row_index-1 
        #print(temp_row_index,temp_col_index)
    if trace_matrix.iloc[temp_row_index,temp_col_index]=="left_gap":
        p_align.append(trace_matrix.columns[temp_col_index])
        q_align.append("-")
        temp_col_index=temp_col_index-1
        temp_row_index=temp_row_index
        #print(temp_row_index,temp_col_index)
    if trace_matrix.iloc[temp_row_index,temp_col_index]=="up_gap":
        p_align.append("-")
        q_align.append(trace_matrix.index[temp_row_index])
        temp_col_index=temp_col_index
        temp_row_index=temp_row_index-1
        #print(temp_row_index,temp_col_index)
# 输出比对结果(Output alignment results)
print("3.Final alignment is:"+"\n"+"".join(p_align[::-1])+"\n"+"".join(q_align[::-1]))

        
