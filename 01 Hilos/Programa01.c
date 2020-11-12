/*
	- - - Creacion de hilos POSIX en Linux - - -
	#NotaImportante: 
		Para la ejecucion se debe seguir la siguiente sintaxis: 
			gcc Programa01.c -o Programa01 -lpthread
*/
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>//Aqui viven los hilos POSIX
#include <unistd.h>//Aqui vive Exit() y Wait()

void *Funcion_Hilo(void *iteracion_For);

void main (void){
	int numero_de_hilos;
	printf("\n ¿Cuantos hilos vas a querer wey?: \t");
	scanf("%d",&numero_de_hilos);

	//Variable del tipo hilo
	pthread_t hilos[numero_de_hilos];

	/*
		Para crear hilos llamamos a la funcion siguiente:
		---   pthread_create(variableHilo,Atributos,Funcion,Valores);  ---
		donde:
			- &variableHilo: Direccion de memoria del hilo que vamos a crear
			- Atributos: si es NULL el hilo se crea por defecto del sistema operativo Linux
			- Funcion: tiene que ser del tipo (void*) porque sera del tipo que yo quiera
			- Valores: parametros que le pasamos al hilo tiene que ser (void *) y ademas le agragamos &
	*/
	for(int i=0;i<numero_de_hilos;i++)
		pthread_create(&hilos[i],NULL,Funcion_Hilo,(void *)(&i) );

	/*
		Para esperar a que se terminen de ejecutar los hilos, utilizamos la siguiente funcion:
		---   pthread_join(&variableHilo,Atributos);
		donde:
			- variableHilo: Es el hilo que vamos a crear
			- Atributos: si es NULL el hilo se crea por defecto del sistema operativo Linux
	*/
	for(int i=0;i<numero_de_hilos;i++)
		pthread_join(hilos[i],NULL);

	printf("\n -- Los hilos terminarion, ya me puedo morir alv xd -- \n");
}

/*
	apuntador a void es una barbie:
		(void *): Se lo que tu quieras ser (un comodin)
	#Funcion_Hilo: va a imprimir un hola mundo por cada hilo, asi como su ID
*/
void *Funcion_Hilo(void *iteracion_For){
	int *ApuntadorEntero = (int *)iteracion_For; //Hacemos el casteo del tipo de dato que queremos
	int valor = *ApuntadorEntero; // Obtenemos el valor del apuntador
	//Forma 0
	printf("\n Hola Mundo > Soy el hilo %lu > Fui creado cuando el For tenia: %d", pthread_self() , valor );
	
	//Forma 1
	//printf("\n Hola Mundo > Soy el hilo %lu > Fui creado cuando el For tenia: %d", pthread_self() ,*( (int *)ID_Hilo ) );
	/*
		pthread_self(): Regresa el ID del hilo y es del tipo "Long Unsigned" - %lu
		X = (int *)ID_Hilo  
				Convertimos el tipo de apuntador que se recibe y lo guardamos en X

		*( X ) - Obtenemos el valor del apuntador
	*/
}