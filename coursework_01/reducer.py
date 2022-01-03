#! /usr/bin/env python3

import sys

def main():
    reducer = Reducer()
    reducer.reduce_input(sys.stdin, population=True)

class ReducerValues():
    """
    Helper class to hold the values calculated by the reducer
    """
    def __init__(self, day:str) -> None:
        self.values = []
        self.day = day
        self.max = None
        self.min = None
        self.sum = 0
        self.squared_sum = 0
        self.n = 0

    def add_value(self, value:int) -> None:
        """
        Add a value to the value collection
        """
        # add the value to the collection
        self.values.append(value)

        # update the max and min values
        if self.max is None:
            # initialize the max and min values
            self.max = value
            self.min = value
        else:
            if value > self.max: self.max = value
            if value < self.min: self.min = value

        # update the "running" values
        self.n += 1
        self.sum += value
        self.squared_sum += value * value

    def get_median(self) -> float:
        """
        Get the median value in the values collections.

        Returns
        -------
        median : float
        """
        self.values.sort()
        middle = int(self.n / 2)

        if self.n % 2 == 0:
            return (self.values[middle - 1] + self.values[middle]) / 2.0
        else:
            return self.values[middle]

    def get_variance(self, population:bool=True) -> float:
        """
        Calculate and return the variance of the values collections.

        Parameters
        ----------
        population : bool
            Should the formula for the sample or population variance be used.
        """
        mean = self.sum / float(self.n)

        # please not that I personally think the sample variation should be calculated instead
        #    but the formula as per the course work specification is used (population=True).
        if population:
            return  1.0 / self.n * (self.squared_sum - self.n * mean*mean)
        else:
            return  1.0 / (self.n - 1) * (self.squared_sum - self.n * mean*mean)
        

    def print_output(self, population:bool=True) -> None:
        """
        Print the day values to stdout.

        Parameters
        ----------
        population : bool
            Should the formula for the sample or population variance be used.        
        """
        # calculate the mean
        mean = self.sum / float(self.n)

        # print the output
        print('%s,"%d,%d,%.6f,%.1f,%.6f"' % (
            self.day, 
            self.max, 
            self.min,
            mean,
            self.get_median(),
            self.get_variance(population)))

class Reducer():
    """
    This class contains the logic to summarize the temperature observations by day.
    """
    def reduce_input(self, input_stream, population:bool=True) -> None:
        """
        Reduce the output from the mapper to calculate the max, min, mean, median, and variance per day.

        Parameters
        ----------
        input_stream : iterable
            The input stream to process.
        population : bool
            Should the formula for the sample or population variance be used.
        """
        current_day = ReducerValues(None)

        for item in input_stream:
            if item:
                # get the day and temperature value
                day_value, temperature_value = item.split(',')
                temperature_value = int(temperature_value)

                if current_day.day == day_value:
                    current_day.add_value(temperature_value)
                else:
                    # if the current day exist show the output
                    if current_day.day:
                        current_day.print_output(population)

                    # the current day have changed, create the new day
                    current_day = ReducerValues(day_value)
                    current_day.add_value(temperature_value)

        # print the last day processed
        if current_day.day == day_value:
            current_day.print_output(population)

if __name__=="__main__":
    main()