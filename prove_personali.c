#include <stdio.h>
#include <time.h>
//average of an array with value chosen by the user
//ATTENTION for the future : IF you want to use %d, %lf, %c or other insert it "" sentence

int main() {
    clock_t time;
    time = clock();
    int i, totale;//declare a number to use the automatic version
    double media, somma  = 0.0;
    printf("Scegli quanti valori vuoi inserire : ");
    scanf("%d", &totale);
    int contenitore[totale];
    printf("Scrivi i %d valori : ", totale);
    for (i=0; i<totale; ++i) {
        scanf("%d", &contenitore[i]);
        //contenitore[i] = i+10; to use if you don't wnat the automatic program
        somma += contenitore[i];
    }
    printf("La Somma : %lf", somma);
    printf("\nIl Numero Totale : %d", totale);
    media = somma/totale;
    printf("\nLa Media : %lf", media);
    time = clock() - time;
    double time_taken = ((double)time)/CLOCKS_PER_SEC;
    printf("\nTempo usato : %f sec\n", time_taken);
    return 0;
}