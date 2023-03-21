import matplotlib.pyplot as plt
import pandas as pd

class DataVisualization:
    def __init__(self):
        pass

    def process(self,results,format):
        for result in results:
            resultType = result.get("type")

            if resultType == "linecontributions":
                filename = result.get("filename")
                data = result.get("data")

                if format == "pdf":
                    total_contributions = data.groupby("author").count().sort_values("linenum")

                    print(total_contributions)

                    fig, ax = plt.subplots()

                    ax.barh(total_contributions.index,
                            total_contributions["linenum"])
                    ax.set_title(f"Line Contibution For {filename}" )
                    ax.set_xlabel("Number Of Lines")
                    plt.show()
                pass
