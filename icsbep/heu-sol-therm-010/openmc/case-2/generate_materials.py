import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranium Oxyfluoride Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 2.9381e-06)
mat.add_nuclide('U235', 2.4768e-04)
mat.add_nuclide('U236', 1.3241e-06)
mat.add_nuclide('U238', 1.3839e-05)
mat.add_nuclide('F19', 5.3157e-04)
mat.add_element('O', 3.3255e-02)
mat.add_nuclide('H1', 6.5447e-02)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "1100 Aluminum"
mat.set_density('sum')
mat.add_element('Al', 5.9699e-02)
mat.add_element('Si', 5.5202e-04)
mat.add_element('Cu', 5.1364e-05)
mat.add_element('Zn', 2.4958e-05)
mat.add_element('Mn', 1.4853e-05)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Water Reflector at 39.5 C"
mat.set_density('sum')
mat.add_nuclide('H1', 6.6348e-02)
mat.add_element('O', 3.3174e-02)
mats.append(mat)

mats.export_to_xml()
