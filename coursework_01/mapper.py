#! /usr/bin/env python3

import sys

def main():
    mapper = Mapper()
    mapper.map_input(sys.stdin)


class Mapper():
    """
    This class implements the logic for the mapping functionality.
    """
    def map_input(self, input_stream) -> list:
        """
        Map each item in the input stream to the output. The output is written to stdout.

        Parameters
        ----------
        input_stream : iterable
            The input stream to process.
        """
        output = []

        for item in input_stream:
            mapped_item = self.map(item)
            if mapped_item:
                print(mapped_item)

        return output

    def map(self, item:str) -> str:
        """
        Map the input string to the day the observations if for (key), and the observation temperature (value).

        Parameters
        ----------
        item : str
            The observation data to perform the mapping for.

        Returns
        -------
        output : dict
            A comma seperated string containing the `day` in the format YYYYMMDD and the 'temperature` as an integer.
        """
        # ignore the file headers
        if item.startswith('Wban Number'):
            return None

        # ignore empty lines
        if item == '\n':
            return None

        # tokenize the input line
        tokens = item.split(',')

        # get the day value
        day_value = tokens[1].strip()

        # get the temperature
        temperature_value = tokens[8].strip()
        
        # do not process empty temperature values
        if temperature_value == '-':
            return None
        elif temperature_value == '':
            return None
        else:
            temperature_value = int(temperature_value)

        # return the key and value as a comma seperated string
        return '%s,%s' % (day_value, temperature_value)
        
if __name__=="__main__":
    main()