"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
 tbl0 = pd.read_csv("tbl0.tsv", sep="\t") 
 return len(tbl0)
pass

def pregunta_02():
 tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
 return len(tbl0.columns)
pass


def pregunta_03():
 tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
 return tbl0['_c1'].value_counts().sort_index()
pass

def pregunta_04():
 tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
 return tbl0.groupby('_c1')['_c2'].mean()
pass


def pregunta_05():
 tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
 return tbl0.groupby('_c1')['_c2'].max()
pass



def pregunta_06():
 tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
 a= tbl1['_c4'].unique()
 a=[l.capitalize() for l in a]
 return sorted(a)
pass


def pregunta_07():
     tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
     return tbl0.groupby('_c1')['_c2'].sum()
pass


def pregunta_08():
 tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
 tbl0['suma']=tbl0['_c0']+tbl0['_c2']
 return tbl0
pass


def pregunta_09():
 tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
 tbl0['year']=tbl0['_c3'].str[:4]
 return tbl0
pass


def pregunta_10():
 aux1=list()
 tbl3=pd.DataFrame()
 tblout=pd.DataFrame(columns=['_c0','_c1'])
 tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
 a= tbl0['_c1'].unique()
 count=0
 for letra in sorted(a):
   tbl3=tbl0.groupby('_c1').get_group(letra)
   aux1=tbl3['_c2'].to_list()
   aux1.sort()
   straux=':'.join([str(l) for l in aux1])
   tblout.at[count,'_c0']=letra
   tblout.at[count,'_c1']=straux
   count=count+1
 
 return tblout

pass


def pregunta_11():
 aux1=list()
 tbl3=pd.DataFrame()
 tblout=pd.DataFrame(columns=['_c0','_c4'])
 tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
 a= tbl1['_c0'].unique()
 count=0
 for numero in sorted(a):
   tbl3=tbl1.groupby('_c0').get_group(numero)
   aux1=tbl3['_c4'].to_list()
   aux1.sort()
   straux=','.join([str(l) for l in aux1])
   tblout.at[count,'_c0']=numero
   tblout.at[count,'_c4']=straux
   count=count+1
 
 return tblout


pass


def pregunta_12():
 aux1=list()
 aux12=list()
 tbl3=pd.DataFrame()
 tblout=pd.DataFrame(columns=['_c0','_c5'])
 tbl2 = pd.read_csv("tbl2.tsv", sep="\t")
 a= tbl2['_c0'].unique()
 count=0
 for numero in sorted(a):
   straux1=str()
   straux2=str()
   tbl3=tbl2.groupby('_c0').get_group(numero)
   aux1=tbl3['_c5a'].to_list()
   aux2=tbl3['_c5b'].to_list()
   aux12=sorted(zip(aux1,aux2))
   for item in aux12:
       straux1=str(':').join([str(item[0]),str(item[1])])
       straux2=straux2+','+straux1
   tblout.at[count,'_c0']=numero
   tblout.at[count,'_c5']=straux2[1:]
   count=count+1
 
 return tblout

pass


def pregunta_13():
 tbl0=pd.read_csv("tbl0.tsv", sep="\t")
 tbl2=pd.read_csv("tbl2.tsv", sep="\t")
 tblout=pd.merge(tbl0,tbl2,on='_c0')
 
 return tblout.groupby('_c1')['_c5b'].sum()


pass