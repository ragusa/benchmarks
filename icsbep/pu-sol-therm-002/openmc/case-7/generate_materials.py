import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Plutonium nitrate solution"
mat.set_density('sum')
mat.add_nuclide('Pu239', 1.8814e-04)
mat.add_nuclide('Pu240', 6.0338e-06)
mat.add_nuclide('N14', 3.4867e-03)
mat.add_nuclide('H1', 5.8109e-02)
mat.add_nuclide('O16', 3.8160e-02)
mat.add_element('Fe', 2.5556e-06)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "347 stainless steel"
mat.set_density('sum')
mat.add_element('Fe', 6.0386e-02)
mat.add_element('Cr', 1.6678e-02)
mat.add_element('Ni', 9.8504e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Water at 27 C"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6622e-02)
mat.add_nuclide('O16', 3.3311e-02)
mats.append(mat)

mats.export_to_xml()
