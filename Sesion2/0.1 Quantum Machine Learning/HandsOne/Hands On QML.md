



Variational Hybrid Quantum-Clasical algoritm  resuelven problemas de clasificación.


In the recent past, we have witnessed how algorithms learned to drive cars
and beat world champions in chess and Go. Machine learning is being applied to virtually every imaginable sector, from military to aerospace, from
agriculture to manufacturing, and from finance to healthcare.
But these algorithms become increasingly hard to train because they consist
of billions of parameters. Quantum computers promise to solve such problems intractable with current computing technologies. Moreover, their ability to compute multiple states simultaneously enables them to perform an
indefinite number of superposed tasks in parallel. An ability that promises
to improve and to expedite machine learning techniques.


## Machine Learning 

El machine learnign comprende diferentes técnicas:

- Clasificación: Le doy una etiqueta de algo que estoy buscando predecir por ejemplo si un animal es perro o es gato, y dado un conjunto de datos de entrada y una etiquetas, puedo responder la pregunta ¿Es un perro o gato?


- RegresiónLa regresión se trata de encontrar una función para predecir la relación entre
alguna entrada y el valor de salida continuo dependiente.


- Segmentación: El particionado de grupos en características y comportamientos similares.


El cómputo cuántico es diferente del cómputo clásico porque se vale de 3 propiedades fundamentales en física cuántica: Superposición, Entrelazamiento, Interferencia.


Superposición tiene que ver con un estado cuántico puede existir en multiples estados de manera concurrente.

Interferencia cuántica e slo que nos permitirá sesgar un sistema cuántico hacia nuestros resultados,
La idea es crear un patrón de interferencia donde los caminos lleven a respuestas incorrectas interfieran destructivamente y se cancelen, pero los caminos que llevan a respeustas correctas se refuercen entre sí.



Entrelazamiento: Una gran correlación entre dos particulas, las partículas que están entrelazadas están perfectamente correlacionadas sin importar la distancia que las separe.


## Algoritmos de Machine Learning: 

- Representación: Independiente de la arquitectura los algoritmos representan conocimiento, árboles de desición, máquinas de vectores soporte, redes neuronales.
- Evaluación: Es una función que evalúa un candidato que evalua lso parámetros, precisión, entroía, costo, margen, error cuadrado.
- Optimización: Describe la forma de generar parametrizaciones y algoritmos candidatos. Es conocido como el proceso de busqueda, por ejemplo, "optimización combinatoria, convexa, "


El primer paso en Machine Learning es el desarrollo de la arquitectura, la representaciín, esta arquitectura especifica los parámetros los cuales sus valores contendran la representación del "saber" o "conocimiento".Este paso determina que tanbien la soluciín se ajusta a resovler un problema específico.

Muchos parámetros no siempre es a mejor aproximación, un modelo lineal puede no requerir muchos parámetros y de considerarlso solo fallaría, lo contrario es cierto también, poco s parámetros podría ser insuficiente para resovler problemas complejos como el entendimiento de lenguaje natural.


![asset](assets/GeneralNotion.PNG)


Una vez la representación está lista, entrenamos nuestro algoritmo de machine learning con ejemplos, dependiente del número de parámetros neceesitaremso muchos ejemplos.

Trata de predecir la etiqueta de cada instancia. Finalmente usamos una función para evaluar que tambine el algoritmo est{a performando

El optimizador busca ajustar la representación a lso parámetros que prometen un mejor performace concerniente a la medición.

El aprendizaje sucede a pequeños pasos, no a grandes saltos. Se requieren varias iteracioens sobre el proceso de "representación, evaluación, optimización" para que la máquina pueda seleccionar de manera correcta estos "labels"



## Para qué tareas son buenos los computadores cuánticos?



Lo que hace al computo cuántico poderoso no es la velocidad ni el almacenamiento, es su complejidad.

La teoría de la complejidad es el estudio computacional del esfuerzo requerido para correr un algoritmo.


El esfuerzo de multiplicar dos números computacionalmente O(n2), estos algorimtos solucionables en tiempo polinominal.

- Mientras que una calculadora para los primeros 800 y sus factores primos tardaría más de 2000 mil años en calcualr el resultado.

- Al algoritmo de Shor usaria superposición para evaluar todos los posibles factores de un número simultáneamente, en vez de calcular un resultado realiza interferencia para combinar todos las posibles respeustas en una manera que genere una respuesta correcta.



## QML

Es el uso de cómputo cuántico para la cmputación de algoritmos de machine learning.

Entendiendo que poseemos una fase de representación, evaluación, optimización.

Por contraste tenemos que algoritmos como GTP-3 Generative Pretrained Trnasformer faciltia crear texto parecido al humano, tiene más de 170 billones de parámetros, IBQ Q posee menos de 30 qubits y almacenan más información que los bits clásicos, debido a que no es ni cero ni uno, el cómputo cuántico actual está lejos de superar la fase de representación del machine learning.


En el momento de evaluar el algoritmo de machine learning trata de predecir el label de algo, de manera clásica involucra la medición y tranformación de los data points. 

Por ejmplo las redes neuronales se basan en multiplicaciones matriciales, los computadores clásicos son buenos con estas operaciones. Sin embargo a medida que crecen los parámetros calcular la predicción de hace difícil. 


Finalmente cuando buscamos optimizar requerimos seleccionar este conjunto de parámetros que son más performantes y con más de 170 billones de parámetros los cálculos se hacen más complejos.

El problema radica en que si fueramos a entrenar un algoritmo que tenga tantos parámetros tardaríamos mucho tiempo si solo usaramos una GPU. La forma que usa ML es explotar la estructura del problema subyacente. 

La principal habilidad del computo cuántico es la de computar multiples estados concurrentemente. Un algoritmo de optimización puede combinar todos los posibles candidatos y producir aquellos que prometen buenos resultados.

Cabe aclarar que a representación, evaluación, optimización es un proceso secuencial, por lo que no solamente nos enfocamos en la optimización.

Si esperamos que el QC reduzca la complejidad de los entrenamientos de algoritmos de manera exponencialmente más rápida, entonces es entendible pensar que "estamos cerca" de una AGI artificial general Inteligence.

Un limitante del machine Learnign es que estamos en el NISQ Era.

# QML -- NISQ ERA


Computadores clásicos trabjan con 0 y 1, paso o no de corriente, estos valores estan discretizados, errores tienden a no verse, pero para aquellos dificiles de detectar tenemos métodos. El error tiene que se grande para ser visto fácilmente.

Computo cuántico necesita de ser muy preciso debido a que estos están en un estado continuo, los algoritmos cuánticos se basan en manipulacioens específicoas de parametros continuos en constante variación. Aquí los errores pueden ser pequeños e imposibles de detectar, pero aún así podrían dañar una comptuación, esto es uan vulnerabilidad al ruido del ambiente, el material del que está hecho el computador inclusive el calor.


Es decir estamos en la era en que aún tenemos ruido en el cómputo.

Noisy
Aún no cocntamos con la cantidad de quibts apropiada para una correción de errores apropiada. 

Intermediate
Porque aún no tenemos la cantidad de qubits suficientes para comptuar algorimos sofisticados, ni siquiera alcanzar la supremacía.

Los algoritmos cuanticos variacionales 
...

For instance, Variational Quantum-Classical Algorithms have become a popular way to think about quantum algorithms for near-term quantum devices.
In these algorithms, classical computers perform the overall machine learning task on information they acquire from running the hard-to-compute calculations on a quantum computer.
The quantum algorithm produces information based on a set of parameters
provided by the classical algorithm. Therefore, they are called Parameterized Quantum Circuits (PQCs). They are relatively small, short-lived, and
thus suited for NISQ-devices.
....


La promesa del cpomputo cuántico es reducir el la complejidad de un conjutno de algoritmos que presentan estos cálculos difíciles de computar. Donde un computador clásico podría tardar milenios, y computador cuántico lo haría en segundos. Nos basamos en tres propiedades fundamentales, el entrelazamiento, la sueprposición y la interferencia.


Es importante entender el contexto de la mecáncia cuántica donde acontece, es deseable poder hacer la matemática que usa, pero es crucial tener y desarrollar un sentido  sobre lo que los conceptos significan en la práctica.

Es decir es deseable saber mecánica cuántica pero más importante es entender como resovlver cierto problema.







 pip install qiskit numpy scipy matplotlib ipython pandas sympy nose seaborn 
 
 

 scikit-learn

Drawing
 pylatexenc ipywidgets qutip






-------------------------


Principales problemas de clasificaión regresión y segementación.



Superposición: ElEs el fenómeno cuántico que hbabla sorbe que un sistema puede existir estados concurrentemente, pero no existen como tal, están representados como una compleja combinación lienal  de un estado 0 y un estado 1.

La interferencia es lo que nos permite sesgar un sistema cuántico a un estado deseado.  La idea es crear patrones de interferencia donde los caminos que llevan a respeustar incorrectas interfieran destructivamente , mientras los caminos que llevana a respeustas correcta se refuerzen asi mismo

![[Pasted image 20221107173328.png]]


**Entrelazamiento:** Es una correlación extrema entre las partículas que no depende de la distancia.




---- Respect oa las ventajas del quantum

Multiplicar dos numeros no es un problema, pero la factorización de esos dos números peude tardar hasta 2000 años. El algoritmo de Shor usa la superposición para evaluar todos lso posibles factores de los numéros que factorizan al menos.
En vez de calcular el resultado, este usa la interferencia para combinar todas las posibles respuestas que produce respeustas correctas.

El cómputo cuántico promete solucionar ciertos cálculos matemáticos con complejidad reducida.


---- Respecto a QML

En machine learnign en la etapa de evaluación es necesario entrenar el modelo con una cantidad masiva de parámetros, por ehemplo con 175 billones de parámetros la cantidad de combinaciones es muy grandes. De manera clásica tambipen buscamos que el problema converja en una solución acetable en un tiempo aceptable.

La principal cracteristica de  un computador cuantodp es la habilidad que tiene de computar multiples estados conurrentemente.

Un algortimo de opitmizción cuántica puede combinar todos lo sposibles resultados y producir aquellos que prometen buenos resultados.


### Variational Quantum Eigensolver.




