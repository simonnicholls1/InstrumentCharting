import matplotlib.pyplot as plt
from tabulate import tabulate

class Charting:

    def plot_graph(self, instrument, instrument_values):
        try:
            #Plot graph
            print("Plotting graph...")
            fig = plt.figure()
            plt.title('Value, Rolling Mean & Median for ' + instrument)
            plt.plot(instrument_values['value'], label='Value')
            plt.plot(instrument_values['rolling_mean'], label='Rolling Mean')
            plt.plot(instrument_values['rolling_median'], label='Rolling Median')
            plt.legend(loc='upper left')
            plt.ylabel('Value $')
            plt.xlabel('Date')
            print("Graph successfully plotted")
            print("")
        except Exception as ex:
            print("Error occurred while constructing chart for: " + instrument + " Error: " + str(ex))
            raise Exception("Error constructing graph for: " + instrument)

    def print_table(self, instrument, instrument_monthly_values):
        try:
            print("Printing table")
            print(tabulate(instrument_monthly_values, headers='keys', tablefmt='psql'))
            print("Table successfully printed")
            print("")
        except Exception as ex:
            print("Error occurred while constructing table for: " + instrument + " Error: " + str(ex))
            raise Exception("Error constructing table for: " + instrument)

    def show_plots(self):
        plt.show()

