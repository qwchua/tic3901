# for visualizing data in different formats based on the input provided

#Please make sure you have the following library 
#matplotlib
#pandas
#seaborn
#install the library by running pip install <library-name> in terminal if you do not 
#else there will be warning from the import   

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import seaborn as sns

class DataVisualization:
    def __init__(self):
        pass

    def formatConversion(self, final_df, final_string, format):
        if format == "csv":
            final_df.to_csv('C:\\repos\\tic3901\\contributions.csv',index=False)
        
        elif format == "txt":
            with open("output.txt", 'a', encoding="utf-8") as f:
                f.write(final_string)
        
        elif format == "pdf":
            for (columnName, columnData) in final_df.items():
                if columnName == "author":
                    continue
                ax = sns.barplot(
                    x=columnName,
                    y="author",
                    data= final_df.nlargest(10, columnName)
                )
            
                ax.set_xlabel("number of lines")
                ax.set_ylabel(" ")
                ax.set_title(columnName)
                plt.plot()
        
            with PdfPages(r'output.pdf') as export_pdf:
        
                for col in final_df.columns:
                    if col == "author":
                        continue
                    fig = plt.figure(figsize=(11,6))
                    ax = sns.barplot(
                        x=col,
                        y="author",
                        data= final_df.nlargest(10, col)
                    )
                
                    ax.set_xlabel("Number of lines")
                    ax.set_ylabel(" ")
                    ax.set_title(col)
                    fig.tight_layout(pad=3)
                    
                    export_pdf.savefig(fig)

    def processDatatype(self, final_df, format, results):
        for result in results:
            #skip empty result
            if result == None:
                continue
        
            resultType = result.get("type")
        
            if resultType == "linecontributions":
                filename = result.get("filename")
                df = result.get("data")
        
                #if there is no data because the file has no lines
                if df.empty:
                    continue
        
                if format == "txt":
                    df = df[["commithash", "author", "date", "linenum", "content"]]
                    final_string += filename + "\n"
                    final_string += df.to_string(header=False, index=False,formatters={
                                                                                       "linenum": "{})".format,
                                                                                       "commithash": "{:.9}".format,
                                                                                       "content": "{:.180s}".format,
                                                                                       "content": "{:<s}".format,
                    })
                    # final_string += df.to_string(header=False, index=False,formatters={"content": "{:<180}".format,
                    #                                                                    "linenum": "{})".format,
                    #                                                                    "commithash": "{:.9}".format
                    # })
                    final_string += "\n" + "\n"
        
                if format == "csv" or format == "pdf":
                    df['count'] = 1
                    g1 = df.groupby("author").count()['count'].reset_index()
                    g1.rename({'count': filename},axis=1, inplace=True)
        
                    if final_df.empty:
                        final_df = g1
                    
                    else:
                        final_df = final_df.merge(g1, on='author',how='outer')
        
                pass
        return final_df, final_string

    def process(self,results,format):
        final_df = pd.DataFrame()
        final_string = ""

        final_df, final_string = self.processDatatype(final_df, format, results)

        final_df = final_df.fillna(0)
        final_df[final_df.columns[1:]] = final_df[final_df.columns[1:]].astype(int)
        final_df['Total'] = final_df.sum(numeric_only=True,axis=1)

        cols = list(final_df.columns)
        final_df = final_df[cols[0:1] + [cols[-1]] + cols[1:-1]]

        self.formatConversion(final_df, final_string, format)

            
