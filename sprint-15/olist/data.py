from pathlib import Path
import pandas as pd


class Olist:
    """
    The Olist class provides methods to interact with Olist's e-commerce data.

    Methods:
        get_data():
            Loads and returns a dictionary where keys are dataset names (e.g., 'sellers', 'orders')
            and values are pandas DataFrames loaded from corresponding CSV files.

        ping():
            Prints "pong" to confirm the method is callable.
    """
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """

        # $CHALLENGIFY_BEGIN
        csv_path = Path("~/.workintech/olist/data/csv").expanduser()
        file_paths = list(csv_path.iterdir())

        file_names = [f.name for f in file_paths]

        key_names = [
            key_name.replace("olist_", "").replace("_dataset", "").replace(".csv", "")
            for key_name in file_names
        ]

        # Create the dictionary
        data = {}
        for key, file_path in zip(key_names, file_paths):
            data[key] = pd.read_csv(file_path)

        return data
        # $CHALLENGIFY_END

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
