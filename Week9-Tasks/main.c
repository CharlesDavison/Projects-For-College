#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "stringHandling.h"
#include "sorting.h"

int main()
{
    char* str = validateString();
    char* array[100];
    int arrayLen = 0;

    char* token = strtok(str, " ");

    while (token != NULL) {
        array[arrayLen] = token;
        token = strtok(NULL, " ");
        arrayLen++;
    }

    char** newArray = alphaBubbleSort(array, arrayLen);


    for (int j = 0; j < arrayLen; j++){
        printf("%s\n", newArray[j]);
    }

    printf("\n");
    
    newArray = lenBubbleSort(array, arrayLen);
    for (int j = 0; j < arrayLen; j++){
        printf("%s\n", newArray[j]);
    }

    free(str);

    return 0;
}
