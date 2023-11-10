from collatz_generator import CollatzGenerator

gen = CollatzGenerator(10, True)
gen.generate()
# gen.write_to_file()
# gen.create_2d_line_graph()
gen.create_3d_line_graph()