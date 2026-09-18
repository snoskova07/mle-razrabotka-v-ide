class DataFrameReporter:
    def __init__(self, float_format='0.05f', percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df, title=None):
            if title:
                print(title)
        
            print('Количество столбцов:', df.shape[1])
            print('Количество строк:', df.shape[0])

            duplicates = df.duplicated().sum()
            print('Количество дубликатов:', duplicates)

            print('Доля дубликатов:', format(duplicates / df.shape[0], self.percent_format))

            print(df.describe(include='all' if self.include_all else None))
            print('Количество пропусков:', df.isna().sum().sum())            
            print('Доля пропусков:', format(df.isna().mean(axis=None), self.float_format))
    
import pandas as pd

data = pd.read_csv("D:/YandexDisk/ML_Inginier/Lessons/Sprint_6/Project_split_6/mle-razrabotka-v-ide/data/payments.csv")

reporter = DataFrameReporter(float_format='0.02f', percent_format='0.03%')

reporter.show_report(data, 'Отчёт в формате 1:')