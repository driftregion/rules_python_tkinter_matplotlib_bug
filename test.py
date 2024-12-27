import sys
print(f"interpreter: {sys.executable}")
print("_tkinter" in sys.builtin_module_names)
import tkinter
print(tkinter.TkVersion)
import _tkinter
print(_tkinter.__file__)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
