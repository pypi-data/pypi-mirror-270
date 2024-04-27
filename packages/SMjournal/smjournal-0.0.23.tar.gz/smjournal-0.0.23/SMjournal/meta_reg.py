import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from tqdm import tqdm
from .low_level import getFullCombination,getIndexOfCol
import plotly.express as px
from IPython.display import display

class Meta_Reg:
    def __init__(self, df1,y_col,stochQ=10000,weight_col=None,control_cols=None,const_cols=None,solve_problems=False,streamlit=False):
        df = df1.copy()
        if weight_col:
            df=df.loc[df[weight_col]>0]
        if not const_cols:
            const_cols=[i for i in df.columns if ('.hol' in i.lower()) or ('.mkt' in i.lower())]
        if not control_cols:
            control_cols=[i for i in df.columns if i not in const_cols+[y_col,weight_col,'Geographies','Weeks']]
        weight=df[weight_col].to_numpy() if weight_col else None

        #pre meta reg
        x_cols=control_cols+const_cols
        X_rand=np.random.randint(2, size=[stochQ,len(control_cols)])
        X_rand=X_rand[~np.all(X_rand==0 , axis=1)]
        stochQ=len(X_rand)
        allBetas=[]
        y_miniReg=df[y_col].to_numpy()
        allLosses=[]

        if streamlit:
            progress_text = "Operation in progress. Please wait."
            my_bar = streamlit.progress(0, text=progress_text)
            counter=0
            percent_complete=0

        for i in tqdm(X_rand):
            # print(i)
            randomX_cols=getFullCombination(i,control_cols)
            # print(x_col)
            # print(getFullCombination(i,x_col))
            df_x=pd.concat([df[randomX_cols],df[const_cols]

                    ],axis=1)
            X_miniReg=df_x.to_numpy()

            #hago la regresion
            reg = LinearRegression().fit(X_miniReg, y_miniReg, weight)
            betas={df_x.columns[i]:reg.coef_[i] for i in range(len(df_x.columns))}
            allLosses.append(np.mean((reg.predict(X_miniReg)-y_miniReg)**2))

            allBetas.append(betas)
            if streamlit:
                my_bar.progress(percent_complete, text=progress_text)
                counter+=1
                percent_complete=counter/len(X_rand)
            # print(betas)
        if streamlit:
            my_bar.empty()
        if solve_problems:
        #problems with reg
            px.histogram(np.log(allLosses)).show()
            px.histogram(np.log(allLosses))
            indices=[i for i in range(len(allLosses)) if np.log(allLosses[i])<0]
            allBetas=list(np.array(allBetas)[indices])
            allLosses=list(np.array(allLosses)[indices])
            X_rand=X_rand[indices]
            px.histogram(np.log(allLosses)).show()


        df['periods']=df['Weeks'].dt.year
        # print('--------------------------here---------------')
        # print(df['periods'].unique())

        selectedPeriod=max(df['periods'].unique())
        supp_df=df.groupby(['periods']).mean()
        medias=supp_df.loc[selectedPeriod].to_dict()
        #to save
        self.allLosses=allLosses
        self.allBetas=allBetas
        self.df=df
        self.X_rand=X_rand
        self.stochQ=stochQ
        self.control_cols=control_cols
        self.const_cols=const_cols
        self.x_cols=x_cols
        self.y_miniReg=y_miniReg
        self.medias=medias
        self.streamlit=streamlit

        display(control_cols)
    
    def beta_reg(self,var,control_var=[]):
        allBetas=self.allBetas
        X_rand=self.X_rand
        allLosses=self.allLosses
        medias=self.medias
        control_cols=self.control_cols
        control_var=control_var+[var]
        # print(var)
        toHist=[]
        fast=set.intersection(*map(set,[getIndexOfCol(i,allBetas) for i in control_var]))
        for i in getIndexOfCol(var,allBetas):
            if i in fast:
                toHist.append({"betas":allBetas[i][var],"control":"controled","error":allLosses[i],'contribution':allBetas[i][var]*medias[var]*100})
            else:
                toHist.append({"betas":allBetas[i][var],"control":"non_controled","error":allLosses[i],'contribution':allBetas[i][var]*medias[var]*100})
        tograph=pd.DataFrame(toHist)

        fig0=px.histogram(tograph,x="betas",color="control",nbins=1000)
        if not self.streamlit:
            fig0.show()

        metaY=np.array([allBetas[i][var] for i in getIndexOfCol(var,allBetas)])
        metaX=X_rand[getIndexOfCol(var,allBetas)]


        #px.histogram(x=metaY,nbins=1000).show()



        metaReg = LinearRegression(fit_intercept=False).fit(metaX, metaY)




        meta_betas={control_cols[i]:metaReg.coef_[i] for i in range(len(control_cols))}
        #px.scatter(x=[np.array(allLosses)[i] for i in getIndexOfCol(var)],y=metaY).show()
        fig1=px.scatter(tograph,x="error",y="betas",color="control")
        
        fig2=px.histogram(tograph,x="contribution",color="control",nbins=1000)
        
        fig3=px.scatter(tograph,x="error",y="contribution",color="control")
        
        if not self.streamlit:
            
            fig1.show()
            fig2.show()
            fig3.show()
        # meta_betas
        #print(meta_betas[var])
        #{k: v for k, v in sorted(meta_betas.items(), key=lambda item: item[1])}
        display({k: v*medias[var]*100 for k, v in sorted(meta_betas.items(), key=lambda item: item[1])})
        #getT(metaReg,df_x,metaX,metaY)
        return fig0, fig1, fig2, fig3, {k: v*medias[var]*100 for k, v in sorted(meta_betas.items(), key=lambda item: item[1])}, {k: v for k, v in sorted(meta_betas.items(), key=lambda item: item[1])}