**Hill Climbing**

| Hill Climbing | 4 Reinas | 8 Reinas | 10 Reinas |
| --- | --- | --- | --- |
| Porcentaje de éxito | 30.0% | 16.6666666667% | 3.3333333333335% |
| Media del tiempo de ejecución | 0.016160 | 0.274776705106099 | 0.769151624043782 |
| Desviación estándar del tiempo de ejecución | 0.01080 | 0.126320905231522 | 0.14802065676409 |
| Media de la cantidad de estados recorridos | 700.5 | 834.0666666666667 | 966.833333333334 |
| Desviación estándar de la cantidad de estados recorridos | 465.31493 | 377.3814436654093 | 181.6613149058801 |

**Simulated Annealing**

| Hill Climbing | 4 Reinas | 8 Reinas | 10 Reinas |
| --- | --- | --- | --- |
| Porcentaje de éxito | 100.0% | 96.666666666667% | 96.666666666667% |
| Media del tiempo de ejecución | 0.00023190180461 | 0.0076596577963 | 0.021068008740743 |
| Desviación estándar del tiempo de ejecución | 0.000427570925381 | 0.01256467524616 | 0.02497763039995 |
| Media de la cantidad de estados recorridos | 10.0333333333333 | 56.2666666666666 | 93.3333333333334 |
| Desviación estándar de la cantidad de estados recorridos | 5.549049830645649 | 38.1231519243054 | 77.021865831022 |

**Genetic Algorithm:**

| Hill Climbing | 4 Reinas | 8 Reinas | 10 Reinas |
| --- | --- | --- | --- |
| Porcentaje de éxito | 100.0% | 100.0% | 6.6666666666667% |
| Media del tiempo de ejecución | 0.00468686421713 | 2.4385564883551 | 11.175613228481 |
| Desviación estándar del tiempo de ejecución | 0.00098550977637 | 1.92993791050159 | 0.7153533843358 |
| Media de la cantidad de estados recorridos | 1 | 684.9 | 2465.4 |
| Desviación estándar de la cantidad de estados recorridos | 0 | 541.3339430804562 | 131.8012087224152 |

**Gráficos de cajas de tiempo de ejecución:**

![image](https://user-images.githubusercontent.com/53824547/133863662-583f10f7-10d9-4875-9aae-869246e9d67e.png)

![image](https://user-images.githubusercontent.com/53824547/133863671-a1a599e3-936d-40d3-be03-3e3bbbc0ed15.png)

![image](https://user-images.githubusercontent.com/53824547/133863678-b3ddec2b-87e9-48eb-b3db-5419a96d1065.png)

![image](https://user-images.githubusercontent.com/53824547/133863692-b4118fd5-2209-4936-bacb-f061e0b15e3f.png)

![image](https://user-images.githubusercontent.com/53824547/133863703-d2199d90-5a69-46f2-9334-368e46c26963.png)

![image](https://user-images.githubusercontent.com/53824547/133863720-9a3e941d-0f55-49a5-a81c-9ef7d154ef6f.png)

![image](https://user-images.githubusercontent.com/53824547/133863736-6b7c7f1d-f550-446f-88a5-3928aebbfb78.png)

![image](https://user-images.githubusercontent.com/53824547/133863749-e3684aa1-c75b-4566-9dce-108cf63ff58e.png)

![image](https://user-images.githubusercontent.com/53824547/133863755-73b511af-b96f-447a-a8fe-0eab8ce8104a.png)

**B) Gráficos de H(e):**

**Hill climbing:**

![image](https://user-images.githubusercontent.com/53824547/133863768-6db1749b-5698-44b1-9e99-ccde6f3c6a7d.png)

**Simulated Annealing:**

![image](https://user-images.githubusercontent.com/53824547/133863782-097569a2-97f8-44ea-9d02-ca9d8655d25f.png)

**Genetic Algorithm:**

![image](https://user-images.githubusercontent.com/53824547/133863791-a4a1c3e0-6817-44e4-92f0-c6330e447ef7.png)

**C)** El algoritmo más óptimo para este problema es el simulated annealing, gracias a su aleatoriedad y a la probabilidad de aceptar estados peores no se queda atascado en mínimos locales como el Hill climbing, y el proceso de enfriamiento del algoritmo funciona mejor en este caso que el cruce y la mutación de algoritmo genético..
