**Nombres y Legajos:**

Pérez Eduardo, 13244

Pérez Carlos, 13245

**TP 7 – Machine Learning**

**Cross Validation**

```{r}

set.seed(2021)

#EJERCICIO 7

#crea los dobles y guarda los indices de los elmentos de esas particiones en listas y guarda esas listas en una lista y la devuelve

create\_folds \&lt;- function(dataframe, Nfolds){

LonFolds \&lt;- ceiling(nrow(dataframe)/Nfolds)

Lista \&lt;- list()

folds \&lt;- split(dataframe[1], sample(rep(1:Nfolds,LonFolds)))

for (x in 1:Nfolds){

Lista \&lt;- append(Lista, c(folds[x]))

}

return(Lista)

}

#utiliza los dobles creado por la funcion anterior y hace el cross validation con arboles de decision, para esto agarra un doble y lo utiliza como testeo usando el resto como entrenamiento, hace los mismo con cada uno de los dobles, usando el algoritmo de arbol de decision n veces, n siendo el numero de dobles

cross\_validation \&lt;- function(dataframe, Nfolds){

folds \&lt;- create\_folds(dataframe, Nfolds)

#crea listas para guardar las metricas correspondientes en cada bucle de arvol de decision

ListAccu \&lt;- c()

ListPrec \&lt;- c()

ListSens \&lt;- c()

ListSpec \&lt;- c()

#bucle for para el cross validation

for (x in 1:Nfolds){

train \&lt;- dataframe[-unlist(folds[x]),]

validation \&lt;- dataframe[unlist(folds[x]),]

train \&lt;-train %\&gt;% mutate(inclinacion\_peligrosa=ifelse(inclinacion\_peligrosa==&#39;1&#39;,&#39;si&#39;,&#39;no&#39;))

train$inclinacion\_peligrosa \&lt;-as.factor(train$inclinacion\_peligrosa)

validation \&lt;- validation %\&gt;% mutate(inclinacion\_peligrosa=ifelse(inclinacion\_peligrosa==&#39;1&#39;,&#39;si&#39;,&#39;no&#39;))

validation$inclinacion\_peligrosa \&lt;-as.factor(validation$inclinacion\_peligrosa)

train\_formula \&lt;- formula(inclinacion\_peligrosa~ altura + circ\_tronco\_cm + lat + long)

tree\_model \&lt;- rpart(train\_formula, train)

prediction \&lt;- predict(tree\_model, validation, type=&#39;prob&#39;)

prediction\_normal \&lt;- ifelse(prediction[,2] \&gt;=0.5,&#39;si&#39;,&#39;no&#39;)

resultados\_validation\&lt;-data.frame(inclinacion\_peligrosa=prediction\_normal)

#Toma las metricas de la matriz de consunsion y la guarda en las listas

Matriz \&lt;- confusionMatrix(as.factor(resultados\_validation$inclinacion\_peligrosa), as.factor(validation$inclinacion\_peligrosa))

ListAccu \&lt;- append(ListAccu, Matriz$overall[&quot;Accuracy&quot;])

ListPrec \&lt;- append(ListPrec, Matriz$byClass[&quot;Precision&quot;])

ListSens \&lt;- append(ListSens, Matriz$byClass[&quot;Sensitivity&quot;])

ListSpec \&lt;- append(ListSpec, Matriz$byClass[&quot;Specifitivy&quot;])

}

#calcula las medias y derivadas estandar de las metricas y las imprime

print(&quot;Medias:&quot;)

print(&quot;Accuracy: &quot;)

print(mean(ListAccu))

print(&quot;Precision: &quot;)

print(mean(ListPrec))

print(&quot;Sensitivity: &quot;)

print(mean(ListSens))

print(&quot;Specifitivy: &quot;)

print(mean(ListSpec))

print(&quot;&quot;)

print(&quot;Desviaciones Estandar: &quot;)

print(&quot;Accuracy: &quot;)

print(sd(ListAccu))

print(&quot;Precision: &quot;)

print(sd(ListPrec))

print(&quot;Sensitivity: &quot;)

print(sd(ListSens))

print(&quot;Specifitivy: &quot;)

print(sd(ListSpec))

}

cross\_validation(dataset\_trees,10)

```

|
 | Media | Desviación estándar |
| --- | --- | --- |
| Accuracy | 0.8879128 | 0.008067727 |
| Precision | 0.8879128 | 0.008067727 |
| Sensitivity | 1 | 0 |
| Specifitivy | 0 | 0 |
