
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import pandas as pd
import numpy as np


def adjRsquare(pre_y,r,vars):
  l=len(pre_y)
  return 1 - (1-r2_score(pre_y, r)) * (l-1)/(l-len(vars)-1)
def getVIFs(vars,df):
  # result={}
  # for i in vars:
  #   pre_y=df[i].to_numpy()
  #   df_x=pd.concat([df[[j for j in vars if j!=i]],
                  
  #           ],axis=1)
  #   pre_X=df_x.to_numpy()
  #   # weight=df[weight_col].to_numpy()

  #   #hago la regresion
  #   reg = LinearRegression().fit(pre_X, pre_y)   #############OJOTA ,weight
  #   #reg = LinearRegression().fit(pre_X, pre_y)
  #   result[i]=1/(1-r2_score(pre_y, reg.predict(pre_X)) )
  #   result[i]=1/(1-adjRsquare(pre_y, reg.predict(pre_X),vars) )
  
  duff=df[vars]
  df_cor = duff.corr()
  vif_matrix=pd.DataFrame(np.linalg.inv(duff.corr().values), index = df_cor.index, columns=df_cor.columns)
  vif_diag=pd.Series(np.diag(vif_matrix), index=vif_matrix.columns)
  
  return vif_diag.to_dict()

#viffs
def getIndexOfCol3(var,allVIFs):
  counter=0
  index=[]
  for j in allVIFs: 
    if var in j.keys():
      index.append(counter)
    counter+=1
  return index
def getFullCombination(boolArray,colls):
  counter=0
  final=[]
  for j in boolArray:
    if j==1:
      final.append(colls[counter])
    counter+=1
  return final


#meta reg
def getIndexOfCol(var,allBetas):

  counter=0
  index=[]
  for j in allBetas:
    if var in j.keys():
      index.append(counter)
    counter+=1
  return index