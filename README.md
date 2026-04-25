⚡ Circuitos de Corriente Eléctrica

Este proyecto consiste en el desarrollo de un programa que permite analizar circuitos eléctricos simples utilizando conceptos fundamentales de física y programación.

El sistema calcula automáticamente valores eléctricos para circuitos con:

Resistores
Capacitores
Conexiones en serie y paralelo

Además, permite ingresar datos de diferentes formas, incluyendo archivos de Excel.

👥 Integrantes
- Carlos Alfredo Abea Martinez
- Andrea Johanna Duarte Guerrero
- Solieth Valentina Trejos Perez

🎯 Objetivo del Proyecto

- Aplicar conceptos de física en programación
- Comprender el comportamiento de circuitos eléctricos
- Automatizar cálculos eléctricos
- Facilitar el análisis de circuitos simples

⚙️ Tecnologías Utilizadas
- 🐍 Python 3
- 📊 Pandas (lectura de Excel)
- 📄 OpenPyXL (manejo de archivos .xlsx)
- 💻 Consola / Terminal

Instalación de dependencias:

*pip install pandas openpyxl*

⚡ Conceptos Utilizados
- 🔹 Ley de Ohm
V = I * R
- V → Voltaje (Voltios)
- I → Corriente (Amperios)
- R → Resistencia (Ohmios)
- 🔹 Capacitores
Q = C * V
- Q → Carga (Coulombs)
- C → Capacitancia (Faradios)
- V → Voltaje (Voltios)

🔗 Tipos de Circuitos
- 🔸 Serie
- Corriente igual en todos los elementos
- El voltaje se divide 
- Resistores:
Req = R1 + R2 + R3
- Capacitores:
1/Ceq = 1/C1 + 1/C2 + 1/C3

🧠 Funcionalidades del Programa

- El programa permite:

- 🔹 Resistores
- Calcular resistencia equivalente
- Calcular corriente total
- Calcular voltaje o corriente en cada resistor
- 🔹 Capacitores
- Calcular capacitancia equivalente
- Calcular carga en cada capacitor
- Calcular voltaje en cada capacitor
- 🔹 Extras
Manejo de prefijos:
- pico (p)
- nano (n)
- micro (u / µ)
- mili (m)
- kilo (k / K)
- mega (M)
- giga (G)

- Ejemplos:

- 10kΩ = 10000 Ω
- 5uF = 0.000005 F
- 53mV = 0.053 V

3️⃣ Archivo de Excel (.xlsx)

📊 Formato del archivo Excel

El archivo debe tener la siguiente estructura:

🔹 Fila 1 (configuración)

| A    | B        | C       | D        |
| ---- | -------- | ------- | -------- |
| tipo | conexion | voltaje | cantidad |

Ejemplo:

| A        | B     | C   | D |
| -------- | ----- | --- | - |
| resistor | serie | 12V | 3 |

🔹 Filas siguientes (valores)

| A    |
| ---- |
| 10kΩ |
| 5kΩ  |
| 220Ω |

📌 Ejemplo completo en Excel

| A        | B        | C   | D |
| -------- | -------- | --- | - |
| resistor | paralelo | 12V | 3 |
| 10kΩ     |          |     |   |
| 5kΩ      |          |     |   |
| 220Ω     |          |     |   |

⚠️ Reglas importantes para Excel

- Los valores deben ir en la columna A
- No dejar filas vacías
- Usar formato correcto (ej: 10kΩ, 5uF, 33pF)
- La cantidad debe coincidir con los valores


