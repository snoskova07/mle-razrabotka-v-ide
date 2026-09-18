import pandas as pd
from src.reporter import DataFrameReporter

def main():
    data = pd.read_csv("D:/YandexDisk/ML_Inginier/Lessons/Sprint_6/Project_split_6/mle-razrabotka-v-ide/data/payments.csv")
    reporter = DataFrameReporter(float_format='0.02f', percent_format='0.03%')
    reporter.show_report(data, 'Отчёт в формате 1:')

if __name__ == '__main__': 
    main()