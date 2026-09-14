import pandas as pd

from reporter import DataFrameReporter


def main():
    data = pd.read_csv('data/payments.csv')

    reporter = DataFrameReporter()
    reporter.show_report(data, 'Отчёт по данным о платежах:')

if __name__ == '__main__':
    main()