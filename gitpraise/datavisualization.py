import matplotlib.pyplot as plt
import pandas as pd

class DataVisualization:
    def __init__(self):
        pass

    def process(self,results,format):
        final_df = pd.DataFrame()

        for result in results:
            resultType = result.get("type")
            if resultType == "linecontributions":
                filename = result.get("filename")
                df = result.get("data")

                if format == "txt":
                    pass

                if format == "pdf":
                    df['count'] = 1
                    g1 = df.groupby("author").count()['count'].reset_index()
                    g1.rename({'count': filename},axis=1, inplace=True)
                    if final_df.empty:
                        final_df = g1
                    
                    else:
                        final_df = final_df.merge(g1, on='author',how='outer')

                if format == "csv":
                    pass

                pass

        final_df = final_df.fillna(0)
        final_df[final_df.columns[1:]] = final_df[final_df.columns[1:]].astype(int)
        final_df['Total'] = final_df.sum(numeric_only=True,axis=1)

        cols = list(final_df.columns)
        final_df = final_df[cols[0:1] + [cols[-1]] + cols[1:-1]]
        final_df.to_csv('C:\\repos\\tic3901\\contributions.csv',index=False)

        # fig, ax = plt.subplots()
        # ax.barh(total_contributions.index,
        #         total_contributions["count"])
        # ax.set_title(f"Line Contibution For {filename}" )
        # ax.set_xlabel("Number Of Lines")
        # plt.show()
