# Pregunta 1

### Single Responsibility

Cada modulo debe enfocarse en un solo objetivo y esto no se cumple especialmente en el ``` main() ``` el cual se encarga de mostrar informacion, la logica para mostrarla y ademas realiza la funcion de guardar la informacion.

***

### Open Close

En las clases ``` CinePlaneta ```y ```CineStark```al ser iguales cuando se desee ingresar un nuevo campo para un cine, se debera modificar a ambos cines por separado, o en caso se tenga que crear otro cine, se debera copiar toda la informacion cuando estas deberian tener un padre. De esta manera pueden extenderse en caso se tengan ```funciones``` distintas para cada cine pero esten cerradas para modificarse.


***

### Interface Segregation

Este principio esta muy relacionado al de **Single Responsibility** por lo que no se cumple en el ```guardar entradas``` ya que realmente no depende del cine 
