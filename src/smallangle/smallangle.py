import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    """Do calculations and approximations for goniometric functions.
    """
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Amount of steps to slice the interval from 0 to 2 pi into. (>= 1)",
    show_default=True,  # show default in help
)
def sin(number):
    """Display a table of length NUMBER with sine values on the interval from 0 to 2 pi.

    NUMBER is an integer greater than or equal to 1.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Amount of steps to slice the interval from 0 to 2 pi into. (>= 1)",
    show_default=True,  # show default in help
)
def tan(number):
    """Display a table of length NUMBER with tangent values on the interval from 0 to 2 pi.

    NUMBER is an integer greater than or equal to 1.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Amount of steps to slice the interval from 0 to 2 pi into. (>= 1)",
    show_default=True,  # show default in help
)
def cos(number):
    """Display a table of length NUMBER with cosine values on the interval from 0 to 2 pi.

    NUMBER is an integer greater than or equal to 1.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "cos (x)": np.cos(x)})
    print(df)

@cmd_group.command()
@click.argument("accuracy", type = float)
def approx(accuracy):
    """Calculate the value x for which x differs more than a value ACCURACY from sin(x).

    ACCURACY is a floating point value greater than 0.
    """
    x = 0
    while np.abs(x - np.sin(x)) <= accuracy:
        x += 0.001
    
    print(f"For an accuracy of {accuracy}, the small-angle approximation holds up to x = {np.round(x, 3)}")

if __name__ == "__main__":
    cmd_group()