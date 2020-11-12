/*
	- - - Creacion de hijos de los hilos con POSIX en Linux - - -
	#NotaImportante: 
		Para la ejecucion se debe seguir la siguiente sintaxis: 
			gcc Programa02.c -o Programa02 -lpthread
*/
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>//Aqui viven los hilos POSIX
#include <unistd.h>//Aqui vive Exit() y Wait()

void *Funcion_Hilo(void *iteracion_For);
void *Funcion_Hijo_Hilo(void *id_hilo);

void main (void){	
	int num_hijos = 2;

	//Variable del tipo hilo
	pthread_t hilos[3];


	for(int i=0;i<3;i++)
		pthread_create(&hilos[i],NULL,Funcion_Hilo,(void *)(&num_hijos) );

	for(int i=0;i<3;i++)
		pthread_join(hilos[i],NULL);

	printf("\n -- Los hilos terminarion, ya me puedo morir alv xd -- \n");
}


void *Funcion_Hilo(void *numhilos){	
	pthread_t hilos_hijo[*((int *)numhilos)];
	printf("\n Soy el hilo %lu",pthread_self());
	long unsigned idHilo = pthread_self();
	
	for(int i=0;i<(*((int *)numhilos));i++){
		pthread_create(&hilos_hijo[i],NULL,Funcion_Hijo_Hilo,(void *)(&idHilo));		
	}

	for(int i=0;i<(*((int *)numhilos));i++)
		pthread_join(hilos_hijo[i],NULL);

}

void *Funcion_Hijo_Hilo(void *id_hilo){
	long unsigned *id_padre = (long unsigned *)id_hilo;
	printf("\n Padre %lu > Soy el hijo %lu",*id_padre,pthread_self());
}