#include <stdio.h>
#include <stdbool.h>

#include "sorting.h"
char** alphaBubbleSort(char** array, int arrayLen){
    bool sorted;
    for(int i = 0; i < arrayLen - 1; i++){
        sorted = true;

        for(int j = 0; j < arrayLen - 1 - i; j++){
            if(strcmp(array[j], array[j+1]) > 0){
                char* tmp = array[j];
                array[j] = array[j+1];
                array[j+1] = tmp;
                sorted = false;
            }
        }
        if(sorted) break;
    }
    return array;
}

char** lenBubbleSort(char** array, int arrayLen){
    bool sorted;

    for (int i = 0; i < arrayLen - 1; i++) {
        sorted = true;

        for (int j = 0; j < arrayLen - 1 - i; j++) {
            int len_j = strlen(array[j]);
            int len_j1 = strlen(array[j+1]);

            if (len_j > len_j1 || (len_j == len_j1 && strcmp(array[j], array[j+1]) > 0)) {
                char *tmp = array[j];
                array[j] = array[j+1];
                array[j+1] = tmp;
                sorted = false;
            }
        }

        if(sorted) break;
    }

    return array;
}