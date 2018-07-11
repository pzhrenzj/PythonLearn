import numpy as np
import pandas as pd
import os as os
from openpyxl import load_workbook
def loadexecl(filename,filepath,fileNum,selectColum,selectColunReam):
        # df = pd.read_excel(filename,sheet_name='aaa')
        df=pd.read_excel(filename)
        for i in range(2,fileNum):
            if len(str(i)) < 2:
                film='0'+str(i)
            else:
                film=str(i)
            print(filepath+film+'.xls')
            dtemp=pd.read_excel(filepath+film+'.xls')
            df=pd.concat([df,dtemp],axis=0)
        del dtemp
        a=selectColum
        # df1=df.pop('品名（中文）')
        df1=df.iloc[:,a[0]]
        a.pop(0)

        for i in a:
            b=df.iloc[:,i]
            df1=pd.concat([df1,b],axis=1)
            del b
        df1.columns=selectColunReam
        # df1.to_excel('f://temp.xlsx')
        # print(df1[0:50])
       # dfend=pd.pivot_table(df1,index=['品名（中文）','规格型号'],values=['结算数量','含税金额'],columns=['品名（中文）','规格型号'],aggfunc=[np.sum],fill_value=0,margins=True)
        dfend=pd.pivot_table(df1,index=['品名','规格型号'],values=['结算数量','含税金额'],aggfunc=[np.sum],fill_value=0,margins=True)
        # print(dfend.columns)
        # dfend['单价']=dfend[0,0]/dfend[0,1]
        dfend2=pd.pivot_table(df1,index=['品名'],values=['结算数量','含税金额'],aggfunc=[np.sum],fill_value=0,margins=True)
        print(dfend)
        print(dfend2)
        excelAddSheet(df1, filepath+'结果.xlsx', '原表')
        excelAddSheet(dfend, filepath+'结果.xlsx', '品名规格汇总')
        excelAddSheet(dfend2, filepath+'结果.xlsx', '品名汇总')

#enter code here
# dataframe: 需要写入excel的数�?# outfile：输出的文件地址
# name: sheet_name的文件名�?
def excelAddSheet(dataframe, outfile, name):
    writer = pd.ExcelWriter(outfile, enginge='openpyxl')
    if os.path.exists(outfile) != True:
        # dataframe.to_excel(writer, name, index=False)
        dataframe.to_excel(writer, name)
    else:
        print(writer.path)
        book = load_workbook(writer.path)
        print(book)
        writer.book = book
        # dataframe.to_excel(excel_writer=writer, sheet_name = name, index=False)
        dataframe.to_excel(excel_writer=writer, sheet_name=name)
    writer.save()
    writer.close()
sc=input('留用表格列数，用空格分开：')
scname=input('留用表格列使用名称，用空格分开：')
loadexecl(input('读取电子表格文件路径：'),input('读取电子表格序号前路径：'),int(input('输入文件总数：'))+1,[int(n) for n in sc.split()],[str(n) for n in scname.split()])