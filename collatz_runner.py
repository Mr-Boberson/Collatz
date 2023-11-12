"""The file used to run the Collatz generation"""
__author__ = "Mr-Boberson"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Mr-Boberson"

from collatz_generator import CollatzGenerator

gen = CollatzGenerator(20, shortcut=True)
gen.generate()
gen.write_to_file()
gen.create_2d_line_graph()
gen.create_3d_line_graph()
del gen

gen2 = CollatzGenerator(8, shortcut=False, filename="collatz2.txt")
gen2.generate()
gen2.write_to_file()
# gen2.create_3d_line_graph()
gen2.create_2d_line_graph()
del gen2