"""
Copyright 2024 David Woodburn

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

__author__ = "David Woodburn"
__license__ = "MIT"
__date__ = "2024-04-24"
__maintainer__ = "David Woodburn"
__email__ = "david.woodburn@icloud.com"
__status__ = "Development"

import os
import time
import math
import numpy as np


class config:
    uni = True # flag to use Unicode characters
    cols = 60 # default column width
    rows = 20 # default row height
    ar = 2.1 # aspect ratio of characters


class persistent:
    t_last = None

# ------------------
# Plotting functions
# ------------------

def plot(x, y=None, label='', rows=1, cols=1, equal=0):
    """
    Create a text-based plot of the path defined by (`x`, `y`) using characters.
    If the size of the terminal can be found, that will be used for sizing the
    plot. Otherwise, the default dimensions (config.cols, config.rows) will be
    used. Note that this function does not plot connecting lines, only the
    points specified by the (`x`, `y`) pairs.

    Parameters
    ----------
    x : (K,) or (J, K) np.ndarray
        Array of x-axis values or matrix of rows of x-axis values.
    y : (K,) or (J, K) np.ndarray, default None
        Array of y-axis values or matrix of rows of y-axis values. If `y` is not
        provided, `x` will be used as the `y` array and `x` will be defined to
        be an array of indices (starting at zero).
    label : str, default ''
        Text to place at top of the plot, centered in the border.
    rows : int, default 1
        Desired number of rows if greater than 1 or fraction of existing rows if
        less than 1.
    cols : int, default 1
        Desired number of columns if greater than 1 or fraction of window
        columns if less than 1.
    equal : float, default 0
        Axis scaling, `y` to `x`. A value of 0 leaves the scaling alone. A value
        of 1 would approximate equal axis scaling. However, because the aspect
        ratio of characters in the terminal is not exactly 2 to 1, this value
        can be adjusted to compensate.

    Notes
    -----
    Non-finite values will be ignored.
    """

    # Get the terminal window size.
    try: # Try to get the true size.
        term_cols, term_rows = os.get_terminal_size()
        colorize = True
    except: # If getting terminal size fails, use default values.
        term_cols = config.cols
        term_rows = config.rows
        colorize = False
    term_rows -= 1 # Account for the prompt line.

    # Convert a fractional canvas size to columns and rows.
    if cols < 0:
        raise ValueError(f"cols should be positive: {cols}!")
    elif cols <= 1:
        cols = max(round(term_cols * cols), 3)
    if rows < 0:
        raise ValueError(f"rows should be positive: {rows}!")
    elif rows <= 1:
        rows = max(round(term_rows * rows), 3)

    # Adjust for the bounding box and ensure integer type.
    rows = int(rows) - 2
    cols = int(cols) - 2

    # Define the sub-columns and sub-rows.
    if config.uni:
        subcols = 2
        subrows = 4
    else:
        subcols = 1
        subrows = 3

    # If only `x` is provided, copy to `y`
    # and make `x` an array of integers.
    if y is None:
        y = x + 0
        if np.ndim(y) == 0:
            x = 1.0
        elif np.ndim(y) == 1:
            x = np.arange(len(y))
        elif np.ndim(y) == 2:
            J, K = y.shape
            x = np.arange(K)
            x = np.outer(np.ones(J), x)
    if isinstance(y, str):
        raise ValueError(f"y should not be a string: {y}!")

    # Ensure x and y are both 2D arrays.
    x = np.array(x)
    y = np.array(y)
    if np.ndim(x) == 0:
        x = np.array([[x]])
    elif np.ndim(x) == 1:
        x = np.array([x])
    if np.ndim(y) == 0:
        y = np.array([[y]])
    elif np.ndim(y) == 1:
        y = np.array([y])

    # Ensure x and y have compatible shapes.
    Jx, Kx = x.shape
    Jy, Ky = y.shape
    if Jx != Jy:
        if Jx == 1 and Jy > 1:
            x = np.outer(np.ones(Jy), x)
            Jx = Jy
        elif Jx > 1 and Jy == 1:
            y = np.outer(np.ones(Jx), y)
            Jy = Jx
        else:
            raise ValueError("x and y must have 1 or the same number of rows.")
    if Kx != Ky:
        raise ValueError("x and y must have the same number of columns.")
    J = Jx
    K = Kx

    # Get the limits.
    x_min = np.inf; x_max = -np.inf
    y_min = np.inf; y_max = -np.inf
    nn = np.arange(K)
    for j in range(J):
        # Get this curve.
        xj = x[j].copy()
        yj = y[j].copy()

        # Find the valid points by index.
        nn_valid = np.intersect1d(nn[np.isfinite(xj)], nn[np.isfinite(yj)])

        # Expand the limits.
        x_min = min(x_min, np.min(xj[nn_valid]))
        x_max = max(x_max, np.max(xj[nn_valid]))
        y_min = min(y_min, np.min(yj[nn_valid]))
        y_max = max(y_max, np.max(yj[nn_valid]))

    # Enforce differentiation.
    eps = 1e-16
    if x_min == x_max:
        x_min -= eps
        x_max += eps
    if y_min == y_max:
        y_min -= eps
        y_max += eps

    # Apply axis scaling.
    if equal != 0:
        x_scale = (1/config.ar)*cols/(x_max - x_min)
        y_scale = rows/(y_max - y_min)
        if x_scale*equal < y_scale:
            y_scale = x_scale*equal
            y_span = rows/y_scale
            y_mid = (y_max + y_min)*0.5
            y_min = y_mid - y_span*0.5
            y_max = y_mid + y_span*0.5
        elif y_scale < x_scale*equal:
            x_scale = y_scale/equal
            x_span = (1/config.ar)*cols/x_scale
            x_mid = (x_max + x_min)*0.5
            x_min = x_mid - x_span*0.5
            x_max = x_mid + x_span*0.5

    # Expand the limits to align zero with the nearest half row so that the zero
    # marker is true.
    if (y_min < 0) and (y_max > 0):
        idx_zero = round((rows - 1.0/subrows)
            * y_max/(y_max - y_min) - 0.5)*subrows + subrows/2
        slope = max((subrows*rows - 1 - idx_zero)/y_min,
            -idx_zero/y_max)
        y_min = (subrows*rows - 1 - idx_zero)/slope
        y_max = -idx_zero/slope
    if y_min == y_max:
        row_zero = -1
    else:
        row_zero = math.floor((rows - 1/subrows)*(y_max)/(y_max - y_min))

    # Get the ranges text.
    x_min_str = f"{x_min:0.6g}".replace("e+0", "e").replace("e-0", "e-")
    x_max_str = f"{x_max:0.6g}".replace("e+0", "e").replace("e-0", "e-")
    y_min_str = f"{y_min:0.6g}".replace("e+0", "e").replace("e-0", "e-")
    y_max_str = f"{y_max:0.6g}".replace("e+0", "e").replace("e-0", "e-")
    ranges = f"({x_min_str}:{x_max_str}, {y_min_str}:{y_max_str})"

    # Initialize the data and color matrices.
    M = np.zeros((subrows*rows, subcols*cols), dtype=int)
    if (J > 1) and (colorize):
        F = np.zeros((rows, cols), dtype=int)
        color_list = [39, 40, 220, 208, 201]
    else:
        F = None

    # For each curve, set the points and colors.
    for j in range(J):
        # Get this curve.
        xj = x[j].copy()
        yj = y[j].copy()

        # Find the valid points by index.
        nn_valid = np.intersect1d(nn[np.isfinite(xj)], nn[np.isfinite(yj)])

        # Scale the data to dots.
        X_jk = (subcols*cols - 1)*(xj[nn_valid] - x_min)/(x_max - x_min)
        Y_jk = (subrows*rows - 1)*(y_max - yj[nn_valid])/(y_max - y_min)

        # Map locations to a large matrix.
        X = np.round(X_jk).astype(int)
        Y = np.round(Y_jk).astype(int)
        M[Y, X] = 1 # Puts a 1 wherever the curve coordinates are.

        # Scale the data to dots.
        if (J > 1) and (colorize):
            u = X//subcols
            v = Y//subrows
            F[v, u] = color_list[j % 5]

    # Convert the large matrix to a smaller matrix of character values.
    C = matrix_to_braille(M) if config.uni else matrix_to_ascii(M)

    # Draw the plot.
    draw_graph(C, ranges, label, F, row_zero)


def bars(x, labels=None, cols=1, fat=False):
    """
    Create a bar graph of the data in `x` using the `labels` for each element
    of `x`.

    Parameters
    ----------
    x : float array like
        Set of values to plot as a bar graph.
    labels : string list, default None
        List of strings. This should be the same length as `x`.
    cols : int, default 1
        Desired number of columns if greater than 1 or fraction of window
        columns if less than 1.
    fat : bool, default False
        Use thicker characters for the progress bar.
    """

    # Get the terminal window size.
    try: # Try to get the true size.
        term_cols, _ = os.get_terminal_size()
        term_cols -= 1
        colorize = True
    except: # If getting terminal size fails, use default values.
        term_cols = config.cols
        colorize = False

    # Convert a fractional `cols` to columns.
    if cols <= 1:
        cols = max(round(term_cols * cols), 18)

    # Get the width of labels.
    label_width = 0
    if labels is not None:
        label_width = max([len(l) for l in labels])

    # Adjust the total width to make room for labels.
    width = cols - label_width - 2
    if width < 1:
        width = 1

    # For each value of x, print the bar.
    span = max(x) - 0
    for n in range(len(x)):
        if labels is None:
            print(" |", end='')
        else:
            sstr = " " * (label_width - len(labels[n]))
            print(f"{sstr}{labels[n]} |", end='')
        ratio = x[n]/span
        draw_bar(width*ratio, width, colorize, fat)
        print("", flush=True)


def heat(matrix):
    """
    Create a surface plot using the input `matrix`. The rows are printed in
    reverse order.
    """

    # Scale the matrix.
    m_min = np.min(matrix)
    m_max = np.max(matrix)
    M = np.round((matrix - m_min)/(m_max - m_min)*23).astype(int) + 232
    rows, cols = M.shape

    # Print the matrix.
    if config.uni:
        for row in range(0, (rows - rows%2), 2):
            for col in range(cols):
                print("\x1b[38;5;%dm\x1b[48;5;%dm\u2580" %
                        (M[row, col], M[row + 1, col]), end='', flush=True)
            print("\x1b[0m", flush=True)
        if rows % 2 == 1:
            for col in range(cols):
                print("\x1b[38;5;%dm\u2580" % (M[-1, col]), end='', flush=True)
            print("\x1b[0m", flush=True)
    else:
        for row in range(rows):
            for col in range(cols):
                print("\x1b[48;5;%dm  " % (M[row, col]), end='')
            print("\x1b[0m")


def table(matrix, head=None, left=None, width=10, sep='  '):
    """
    Print a table to the terminal.

    Parameters
    ----------
    matrix : list of lists of values
        Table of values.
    head : list of strings, default []
        List of header labels.
    left : list of strings, default []
        List of left-most column labels.
    width : int, default 10
        Width in characters of each cell.
    sep : string, default '   '
        String separating columns.
    """

    # -----------------
    # Check the inputs.
    # -----------------

    # Check the type of matrix.
    if isinstance(matrix, (str, float, int)):
        matrix = [[matrix]]
    elif isinstance(matrix, list):
        is_2d = False
        for n, datum in enumerate(matrix):
            if isinstance(datum, np.ndarray):
                is_2d = True
                matrix[n] = datum.tolist()
            elif isinstance(datum, list):
                is_2d = True
        if not is_2d:
            matrix = [matrix]
    elif isinstance(matrix, np.ndarray):
        matrix = matrix.tolist()
        if not isinstance(matrix[0], list):
            matrix = [matrix]
    else:
        raise Exception('heat: matrix must be a list!')

    # Check the type of head.
    if head is None:
        head = []
    elif isinstance(head, (str, float, int)):
        head = [head]
    elif isinstance(head, np.ndarray):
        head = head.tolist()
    elif not isinstance(head, list):
        raise Exception('heat: head must be a list!')

    # Check the type of left.
    if left is None:
        left = []
    elif isinstance(left, (str, float, int)):
        left = [left]
    elif isinstance(left, np.ndarray):
        left = left.tolist()
    elif not isinstance(left, list):
        raise Exception('heat: left must be a list!')

    # Check that width is within 3 to 30.
    if width < 6:
        width = 6
    elif width > 30:
        width = 30

    # -------------
    # Print header.
    # -------------

    def f2str(num, width=6):
        """
        Convert a floating-point number, `num`, to a string, keeping the total
        width in characters equal to `width`.
        """

        # Ensure width is not less than 6, and check if padding should not be
        # used (i.e., width was negative).
        if width < 0:
            width = -width
            skip_padding = True
        else:
            skip_padding = False
        if width < 6:
            width = 6

        # Make num non-negative but remember the minus.
        if num < 0:
            sw = 1
            s = "-"
            num = -num
            ei = int(np.floor(np.log10(num))) # integer exponent
        elif num > 0:
            sw = 0
            s = ""
            ei = int(np.floor(np.log10(num))) # integer exponent
        else:
            sw = 0
            s = ""
            ei = 0

        # Build number string without leading spaces.
        if ei >= 4:     # 10000 to inf
            f_str = s + "%.*g" % (width - 2 - len(str(ei)) - sw,
                    num*(10**(-ei)))
            if "." in f_str:
                f_str = f_str.rstrip("0").rstrip(".")
            f_str += "e%d" % (ei)
        elif ei >= 0:   # 1 to 10-
            f_str = s + "%.*f" % (width - 2 - ei - sw, num)
            if "." in f_str:
                f_str = f_str.rstrip("0").rstrip(".")
        elif ei >= -3:  # 0.001 to 1-
            f_str = s + "%.*f" % (width - 2 - sw, num)
            if "." in f_str:
                f_str = f_str.rstrip("0").rstrip(".")
        else:           # -inf to 0.001-
            f_str = s + "%.*g" % (width - 3 - len(str(-ei)) - sw,
                    num*(10**(-ei)))
            if "." in f_str:
                f_str = f_str.rstrip("0").rstrip(".")
            f_str += "e%d" % (ei)

        # Add leading spaces for padding.
        if not skip_padding:
            f_str = " "*(width - len(f_str)) + f_str

        return f_str

    def fixed_width_string(C, width=6):
        """
        Convert a string or numeric value, `C`, to a string, keeping the total
        width in characters equal to `width`.
        """

        if isinstance(C, str):
            L = len(C)
            if L > width:
                L = width - 3
                return C[:L] + '...'
            elif L == width:
                return C
            else:
                return ' '*(width-L) + C
        elif isinstance(C, float):
            return f2str(C, width)
        else:
            return f2str(float(C), width)

    if len(head) > 0:
        row_str = ""
        if len(left) > 0:
            row_str += " "*width + " | "
        for n_col, val in enumerate(head):
            if n_col > 0:
                row_str += sep
            row_str += fixed_width_string(val, width)
        print(row_str)

        row_str = ""
        if len(left) > 0:
            row_str += "-"*width + " | "
        for n_col in range(len(head)):
            if n_col > 0:
                row_str += sep
            row_str += "-"*width
        print(row_str)

    # -------------
    # Print matrix.
    # -------------

    for n_row, vals in enumerate(matrix):
        row_str = ""
        if len(left) > n_row:
            row_str += fixed_width_string(left[n_row], width) + " | "
        elif len(left) > 0:
            row_str += " "*width + " | "
        for n_col, val in enumerate(vals):
            if n_col > 0:
                row_str += sep
            row_str += fixed_width_string(val, width)
        print(row_str)


def sparsity(matrix, label=''):
    """
    Print the sparsity of a matrix. Note, if you are using SciPy sparse arrays
    or matrices, use the method `toarray()` on the input to this function.
    """

    # Convert matrix to zeros and ones.
    M = (np.abs(matrix) > 1e-30).astype(int)

    # Convert the large matrix to a smaller matrix of character values.
    C = matrix_to_braille(M) if config.uni else matrix_to_stars(M)

    # Create the shape string.
    shape_str = f"{matrix.shape[0]}x{matrix.shape[1]}"

    # Draw the plot.
    draw_graph(C, shape_str, label)


def progress(k, K, t_init=None, cols=1, fat=False):
    """
    Output a simple progress bar with percent complete to the terminal. When `k`
    equals `K - 1`, the progress bar will complete and start a new line.

    Parameters
    ----------
    k : int
        Index which should grow monotonically from 0 to K - 1.
    K : int
        Final index value of `k` plus 1.
    t_init : float, default None
        Initial process time (s). If provided, an estimated time remaining will
        be displayed. If left as None, no time will be shown. When the progress
        bar completes, the total duration will be shown.
    cols : int, default 1
        Desired width of the full string, including the percent complete, the
        bar, and the clock if greater than 1 or fraction of window columns if
        less than 1.
    fat : bool, default False
        Use thicker characters for the progress bar.
    """

    # Skip this call if the bar is not done but not enough time has passed.
    t_now = time.perf_counter()
    if (k + 1 < K) and (persistent.t_last is not None) and \
            (t_now - persistent.t_last < 0.1):
        return
    persistent.t_last = t_now

    # Get the terminal window size.
    try: # Try to get the true size.
        term_cols, _ = os.get_terminal_size()
        term_cols -= 1
        colorize = True
    except: # If getting terminal size fails, use default values.
        term_cols = config.cols
        colorize = False

    # Convert a fractional `cols` to columns.
    if cols <= 1:
        cols = max(round(term_cols * cols), 18)

    # Get the ratio.
    ratio = (k + 1)/K if k < K - 1 else 1

    # Get the clock string.
    if t_init is not None:
        t_diff = t_now - t_init
        if k + 1 == K:
            clk_str = "  " + time_str(t_diff)
        else:
            t_left = 0.0 if ratio <= 0 else t_diff*(1 - ratio)/ratio
            clk_str = " -" + time_str(t_left)
    else:
        clk_str = ""

    # Maximum length of bar
    N = cols - 5 - len(clk_str)

    # Build the progress bar.
    print(f"\r{int(100*ratio):3d}% ", end='')
    draw_bar(N*ratio, N, colorize, fat)
    if k + 1 >= K:
        print(f"{clk_str}", flush=True)
    else:
        print(f"{clk_str}", end='', flush=True)

# -----------------
# Support functions
# -----------------

def time_str(t_seconds):
    """ Convert time in seconds to a clock string of the form
    `HH:MM:SS.S`. """
    t_seconds = abs(t_seconds)
    hours = int(t_seconds/3600)
    minutes = int((t_seconds - hours*3600)//60)
    seconds = (t_seconds % 60)
    clock_str = "%02d:%02d:%04.1f" % (hours, minutes, seconds)
    return clock_str


def matrix_to_braille(M):
    # Pad the matrix with zeros.
    I, J = M.shape
    II = math.ceil(I/4)*4
    JJ = math.ceil(J/2)*2
    MM = np.zeros((II, JJ), dtype=int)
    MM[:I, :J] = M

    # Convert the matrix of ones and zeros to braille characters.
    C = (0x2800 + MM[::4, ::2] +   8*MM[::4, 1::2]
            +  2*MM[1::4, ::2] +  16*MM[1::4, 1::2]
            +  4*MM[2::4, ::2] +  32*MM[2::4, 1::2]
            + 64*MM[3::4, ::2] + 128*MM[3::4, 1::2])
    return C


def matrix_to_ascii(M):
    # Pad the matrix with zeros.
    I, J = M.shape
    II = math.ceil(I/3)*3
    MM = np.zeros((II, J), dtype=int)
    MM[:I, :J] = M[:I, :J]

    # Convert the matrix of ones and zeros to braille characters.
    glyphs = np.array([ # " `-'.!:|"
        0x20, 0x60, 0x2D, 0x27, 0x2E, 0x21, 0x3A, 0x7C])
    C = glyphs[M[::3] + 2*M[1::3] + 4*M[2::3]]
    return C


def matrix_to_stars(M):
    I, J = M.shape
    C = 0x20*np.ones((I, 2*J + 1), dtype=int)
    C[:, 1:-1:2] += 0xA*M
    return C


def draw_graph(C, left=None, right=None, F=None, row_zero=-1):
    """
    Parameters
    ----------
    C : (I, J) int np.ndarray
        Matrix of character values.
    left : string, default None
        String to place on the left of the box.
    right : string, default None
        String to place on the right of the box.
    F : (I, J) int np.ndarray, default None
        Matrix of foreground 8-bit color values.
    """

    # Define the box drawing characters.
    if config.uni:
        b = ["\u250C", "\u2500", "\u2510", "\u2502", "\u2502",
                "\u251C", "\u2524", "\u2514", "\u2518"]
    else:
        b = [".", "-", ".", "|", "|", "+", "+", "'", "'"]

    # Replace zeros with spaces.
    C = np.where(C == 0, 0x20, C)

    # Draw the top edge of the box.
    rows, cols = C.shape
    print(b[0], end='')
    for col in range(cols):
        print(b[1], end='', flush=True)
    print(b[2])

    # Draw the contents and two sides of the box.
    if F is None:
        for row in range(rows):
            if row != row_zero:
                l = b[3]
                r = b[4]
            else:
                l = b[5]
                r = b[6]
            C_row = C[row]
            print(l, end='', flush=True)
            for col in range(cols):
                print(chr(C_row[col]), end='', flush=True)
            print(r, flush=True)
    else:
        # For each row of the matrix, draw.
        for row in range(rows):
            if row != row_zero:
                l = b[3]
                r = b[4]
            else:
                l = b[5]
                r = b[6]

            # Get this row of data.
            F_row = F[row]
            C_row = C[row]

            # Draw this row.
            print(l, end='', flush=True)
            f = 0
            for col in range(cols):
                if f != F_row[col]:
                    f = F_row[col]
                    if f == 0:
                        print("\x1b[0m", end='')
                    else:
                        print(f"\x1b[38;5;{f}m", end='')
                print(chr(C_row[col]), end='', flush=True)
            if f != 0:
                print("\x1b[0m", end='')
            print(r, flush=True)

    # Draw the bottom of the box and the left and right strings.
    mid_dashes = cols - 2 - len(left) - 2 - len(right) - 2*(right != '')
    if mid_dashes >= 0:
        right = f" {right} " if right != '' else ''
        print(f"{b[7]}{b[1]} {left} ", end='', flush=True)
        for col in range(mid_dashes):
            print(b[1], end='', flush=True)
        print(f"{right}{b[1]}{b[8]}", flush=True)
    else:
        print(f"{b[7]}{b[1]*cols}{b[8]}")
        print(left + (', ' + right)*(right != ''), flush=True)


def draw_bar(n, N, colorize, fat):
    # Define the left, center, and right characters and color commands.
    if colorize:
        grey = '\x1b[100m' if config.uni and fat else '\x1b[90m'
    else:
        grey = ''
    if config.uni:
        if fat:
            l = chr(0x2588)
            frac = int(n*8) % 8 # 0 to 7
            c = ' ' if frac == 0 else chr(0x2588 + 8 - frac)
            c = grey + c
            r = ' '
        else:
            l = chr(0x2501)
            if (n) % 1 < 0.5:
                c = grey + chr(0x257A) if colorize else ' '
            else:
                c = chr(0x2578) + grey
            r = chr(0x2501) if colorize else ' '
    else:
        if fat:
            l = '/'
            c = grey + '-' if (n % 1 < 0.5) else '/' + grey
            r = '-'
        else:
            l = '='
            c = grey + '-' if (n % 1 < 0.5) else '=' + grey
            r = '-'

    # Build the progress bar.
    if n >= N:
        for j in range(N):
            print(l, end='', flush=True)
    else:
        bar_len = int(n)
        spc_len = N - 1 - bar_len
        for j in range(bar_len):
            print(l, end='', flush=True)
        print(c, end='', flush=True)
        for j in range(spc_len):
            print(r, end='', flush=True)
        if colorize:
            print('\x1b[0m', end='', flush=True)
