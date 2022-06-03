import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import numpy as np
from os import path, makedirs

A = 1.34941
x = np.linspace(-10, 10, 10**3)
y = -0.0001*(np.abs(np.sin(x) * np.sin(A) * np.exp(np.abs(100-np.sqrt(x ** 2 + A ** 2) / np.pi))) + 1) ** 0.1


data = ET.Element('data')
data_x = ET.SubElement(data, 'row')
data_y = ET.SubElement(data, 'row')
for i in range(x.size):
    _x = ET.SubElement(data_x, 'x')
    _x.text = str(x[i])
    _y = ET.SubElement(data_y, 'y')
    _y.text = str(y[i])
xml_data = ET.ElementTree(data)

if not path.exists('results'):
    makedirs('results')

with open("results/Res.xml", 'wb') as out:
    xml_data.write(out, encoding='utf-8')
    out.close()

plt.plot(x, y)
plt.show()