import openmc

mats = openmc.Materials()

mat = openmc.Material(1)
mat.name = "Uranyl Nitrate Solution"
mat.set_density('sum')
mat.add_nuclide('U234', 6.0186e-07)
mat.add_nuclide('U235', 6.8143e-05)
mat.add_nuclide('U238', 5.9998e-04)
mat.add_nuclide('N14', 2.0540e-03)
mat.add_element('O', 3.7042e-02)
mat.add_nuclide('H1', 5.9802e-02)
mats.append(mat)

mat = openmc.Material(2)
mat.name = "Stainless steel"
mat.set_density('sum')
mat.add_element('Fe', 5.9088e-02)
mat.add_element('Cr', 1.6532e-02)
mat.add_element('Ni', 8.1369e-02)
mat.add_element('Mn', 1.3039e-02)
mat.add_element('Si', 1.3603e-02)
mat.add_element('Ti', 5.9844e-02)
mats.append(mat)

mats.export_to_xml()
