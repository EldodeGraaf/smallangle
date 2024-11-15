import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def small_group():
    pass

@small_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of values of sin.",
    show_default=True, 
)
def sin(number):
    """Calculates the sin of x-values, with x between 0 and 2pi.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@small_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Number of values of tan.",
    show_default=True, 
)
def tan(number):
    """Calculates the tan of x-values, with x between 0 and 2pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    small_group()