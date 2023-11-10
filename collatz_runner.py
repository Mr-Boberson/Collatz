from collatz_generator import CollatzGenerator

gen = CollatzGenerator(5, shortcut=True)
gen.generate()
gen.write_to_file()
# gen.create_2d_line_graph()
gen.create_3d_line_graph()
del gen

gen2 = CollatzGenerator(5, shortcut=False, filename="collatz2.txt")
gen2.generate()
gen2.write_to_file()
gen2.create_3d_line_graph()