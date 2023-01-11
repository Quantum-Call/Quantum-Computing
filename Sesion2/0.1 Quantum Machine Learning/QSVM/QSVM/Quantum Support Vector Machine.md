

Si tuvieramos que clasificar 

Por ejemplo, si tuviera una caja de gaticos blancos y negros, y quisiera separarlos para distinguir entre ellos precisaría una pared que lso divida, y así cuando venga otro gatico pueda ubicarlos en uno u otro lado de la caja.

Las máquinas de soporte vectorial o [[Support Vector Machine]], son un tipo de algoritmo de clasificación binaria, puedo realizar distinción de puntos $\vec{x}$ puntos de datos en dos categorías que podemos llamar $y=\{-1,1\}$, separandolos mediante una linea recta, un plano o hiperplano cuando tenemos alta dimensionalidad, con el propósto de poder realizar una predicción de una nueva observación.

Esta línea o plano que separa nuestros datos, puede ser tambíen una función más compleja de allí que usemos "[[Kernels]]" en nuestro algoritmos.

¿Qué se requiere para realizar esta clasificaión sueprvisada en computación cuántica?


1.  Necesitamos traducir la data clásica $X$ en datapoints cuánticos dados por:
$$\ket{\Phi(\vec{x})}$$

Lo anterior es dado a su vez por un circuito:

$$V(\Phi(\vec{x}))$$

Donde $\Phi$ puedes er cualquier función clásica aplicada a la data $\vec{x}$   (Qué Funciones se peude aplicar?)

2. Requerimos de un circuito parametrizado $$W(\omega)$$ tal que los parámetros $$\omega$$ procesen la data de forma que al final podamos realizar medidas que retornen valores clásicos $y=\{-1,1\}$ por cada input $\vec{x}$ que identifica neustras etiquetas de la data clásica.


Podemos definir un [[Ansatz]] para este problema así:

$$W(\omega)V(\Phi(\vec{x}))\ket{0}$$

Estos tipos de ansatz son llamados [[Circuitos Cuánticos Variacionales]] (Ampliar Ansats y Circuitos cuanticos variacionales)


