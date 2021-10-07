**Carlos Pérez, 13245**

**CSP trabajo práctico 6:**

1. Describir en detalle una formulación CSP para el Sudoku.

**Variables:** Las casillas de la grilla del Sudoku 9x9

**Dominio:** Números enteros de 1 a 9

**Restricciones:**

- Las filas del sudoku tienen que tener todas números distintos.
- Las columnas del sudoku tienen que tener todas números distintos.
- La grilla se divide en 9 sub grillas de 3x3, las cuales no deben tener números repetidos.

2. Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial _{WA=red, V=blue}_ para el problema del colorar el mapa de Australia (Figura 5.1 AIMA 2da edición ).

Estado inicial:

![image](https://user-images.githubusercontent.com/53824547/136237983-2b4533cb-c8ca-4dcd-87ad-88ad98f0f697.png)


Por arco de consistencia de NT -> WA y SA -> WA suprimimos rojo en ambas, Y por arco de consistencia de NSW -> V y SA -> V, se suprime azul en ambos dominios

![image](https://user-images.githubusercontent.com/53824547/136238017-1b26d1b4-0a7e-4b26-992c-0d014ed46acf.png)

Debido al arco consistencia Q -> SA, NT -> SA y NSW -> SA se suprime verde de los 3 dominios.

![image](https://user-images.githubusercontent.com/53824547/136238091-dd1dbc04-0b4a-4848-aa36-a678d823f365.png)

Si Q -> NT y Q -> NSW se suprime Rojo y Azul del dominio Q, dejándolo vacio.

![image](https://user-images.githubusercontent.com/53824547/136238132-c0ba1efb-ccc1-4678-86ad-c8552f4aa858.png)

Esto es una solución inconsistente, demostrado así que se puede detectar inconsistencia de la solución WA=Rojo, V=Azul.

3. Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP. (i.e. Cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).

El peor caso de AC.3 es **O(n^2\*d^3).**

Un grafo de restricciones puede tener **n^2** arccos, Siendo n el número de variables los cuales se pueden encolar **d** veces cada uno, a una complejidad de **O(d^2)** cada verificación, y al ser un árbol tiene n-1 arcos, por lo que queda una complejidad temporal de **O((n-1)\*d^2)).**

4. AC-3 coloca de nuevo en la cola todo arco **( X****k ****, X**** i****)** cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Si por cada arco **( X****k ****,X**** i****)** se lleva cuenta del número de valores que quedan de Xi que sean consistentes con Xk. Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n2d2 )

Al suprimir un valor **Xi** , se tiene que encolar nuevamente el arco **(Xk,Xi)**, por lo que cada arco se puede añadir un máximo de **d** veces. Si además gracias al preprocesado de las restricciones tenemos que para un valor **Xi** , se conoce cuales son los valores de **Xk** que conforman el arco de consistencia, con ese valor **Xi** , podría hacerse la comprobación de consistencia de un arco **O(d)**, dejando la complejidad temporal de problema en **O(n^2\*d^2).**

5. Demostrar la correctitud del algoritmo CSP para árboles estructurados (sección 5.4, p. 172 AIMA 2da edición). Para ello, demostrar:
  a. Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica _n-consistencia_ (siendo n número total de variables)
  b. Argumentar por qué lo demostrado en a es suficiente.

**a.)** Para demostrar esto podemos elegir cualquier variable de un grafo como raíz, y se ordena de modo que el padre de cada nodo lo preceda en ese orden. Posteriormente a todas las variables se aplica arco consistencia, con arco **(Xi,Xj)**, donde **Xi** es el padre de **Xj** , suprimiendo los valores del dominio según sea necesario.

Para **j** desde **1** hasta **n** , se asigna cualquier valor **Xj** consistente con el valor de su padre. Luego de el paso anterior ya el CSP tiene 2-consistencia, por lo que asignacion del paso 3 no requiere vuelta atrás, por lo que nos aseguramos de que cualquier valor suprimido no afecte la consistencia de los arcos que ya han sido tratados, asegurando la n-consistencia.

**b.)** Es suficiente la demostración ya que todos los árboles estructurados se pueden representar del modo anteriormente descrito, y al comprobar la consistencia de arco se asegura que el problema se pueda resolver, por lo que se garantiza la n-consistencia.

6. Tiempo de ejecucion y Estados para 4, 8, 10, 12 y 15 reinas:

Tiempos backtracking:

![image](https://user-images.githubusercontent.com/53824547/136302076-dbe7278d-0a88-43ca-9d00-24f62e11b553.png).

T de ejecucion: 0.000997304916381836, 0.01595759391784668, 0.17054414749145508, 0.1855027675628662, 0.3839743137359619.

Estados backtraking:

![image](https://user-images.githubusercontent.com/53824547/136302144-f077fbf2-7416-4ee1-9fea-093df9c0f971.png).

Estados: 4,65,195,200,347.

Tiempo FC:

![image](https://user-images.githubusercontent.com/53824547/136302182-ec4ce862-c983-4571-83e0-05d1abd1a1f2.png).

T de ejecucion: 0.0009655952453613281, 0.000997304916381836, 0.0010046958923339844, 0.001020669937133789, 0.0020127296447753906.


Estados FC: 

![image](https://user-images.githubusercontent.com/53824547/136302212-d683178a-5222-4b62-b532-2f74aae71682.png).

Estados: 4,26,91,336,419.


