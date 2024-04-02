import pandas as pd

# 读取原始数据文件
data = pd.read_csv("assignment_wosparse/qje2014_2023.txt", sep="\t")

# 表1：论文基本信息
table1_columns = ["UT", "PY", "SO", "SN", "DI", "IS", "VL"]
table1 = data[table1_columns].drop_duplicates().reset_index(drop=True)

# 表2：论文摘要信息
table2_columns = ["UT", "AB"]
table2 = data[table2_columns].drop_duplicates().reset_index(drop=True)

# 表3：论文题目信息
table3_columns = ["UT", "TI"]
table3 = data[table3_columns].drop_duplicates().reset_index(drop=True)
 
# 表4：论文作者信息
table4_columns = ["UT", "AU", "AFN", "AF", "AU_ORDER"]
table4 = data[table4_columns].drop_duplicates().reset_index(drop=True)

# 表5：论文作者与单位信息
table5_columns = ["UT", "AU", "AFN", "C1", "RP", "AU_ORDER"]
table5 = data[table5_columns].drop_duplicates().reset_index(drop=True)
 
# 表6：论文参考文献信息
table6_columns = ["UT", "CR"]
table6 = data[table6_columns].drop_duplicates().reset_index(drop=True)
 
# 将每个表格保存为独立的CSV文件
table1.to_csv("table1.csv", index=False)
table2.to_csv("table2.csv", index=False)
table3.to_csv("table3.csv", index=False)
table4.to_csv("table4.csv", index=False)
table5.to_csv("table5.csv", index=False)
