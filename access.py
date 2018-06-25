"""Read canonical dataset from *latest* folder."""

from io import StringIO
from pathlib import Path

import pandas as pd

FOLDER = Path(__file__).parent / 'data' 
             

def locate(freq):
    return FOLDER / 'df{}.csv'.format(freq)


def read_csv(source):
    """Wrapper for pd.read_csv(). Treats first column at time index.

       Returns:
           pd.DataFrame()
    """
    converter_arg = dict(converters={0: pd.to_datetime}, index_col=0)
    return pd.read_csv(source, **converter_arg)


def proxy(path):
    """A workaround for pandas problem with non-ASCII paths on Windows
       See <https://github.com/pandas-dev/pandas/issues/15086>

       Args:
           path (pathlib.Path) - CSV filepath

       Returns:
           io.StringIO with CSV content
    """
    content = Path(path).read_text()
    return StringIO(content)


def get_dataframe(freq):
    """Read dataframe from local folder"""
    path = locate(freq)
    filelike = proxy(path)
    return read_csv(filelike)


if '__main__' == __name__:   
     dfa, dfq, dfm = (get_dataframe(freq) for freq in 'aqm')