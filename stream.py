class DataStream():
    """docstring for DataStream."""

    def __init__(self):
        """
        Initializing a hashmap for checkups
        """
        self.limiter = {}

    def should_output_data_str(self,timestamp:int, data_string:str):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.

        """
        t = self.limiter.get(data_string, 0)
        if t > timestamp:
            return False
        self.limiter[data_string] = timestamp + 5
        return True

data_stream = DataStream()
print(data_stream.should_output_data_str(timestamp=0, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=1, data_string="world"))
print(data_stream.should_output_data_str(timestamp=6, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=7, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=8, data_string="world"))
