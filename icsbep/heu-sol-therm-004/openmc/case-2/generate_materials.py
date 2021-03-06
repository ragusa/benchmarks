import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "UO2F2/D2O Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 1.2415e-05)
mat.add_nuclide('U235', 1.1350e-03)
mat.add_nuclide('U238', 6.3782e-05)
mat.add_nuclide('F19', 2.4224e-03)
mat.add_element('O', 3.2898e-02)
mat.add_nuclide('H2', 6.0768e-02)
mat.add_nuclide('H1', 1.8285e-04)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "321 Stainless Steel"
mat.set_density('sum')
mat.add_element('Fe', 5.9355e-02)
mat.add_element('Cr', 1.6511e-02)
mat.add_element('Ni', 7.7203e-03)
mat.add_element('Mn', 1.7363e-03)
mat.add_element('Si', 1.6982e-03)
mats.append(mat)

mat = openmc.Material(3)
mat.name = "Heavy Water"
mat.set_density('sum')
mat.add_nuclide('H2', 6.6078e-02)
mat.add_nuclide('H1', 3.9886e-04)
mat.add_element('O', 3.3238e-02)
mats.append(mat)

mats.export_to_xml()
