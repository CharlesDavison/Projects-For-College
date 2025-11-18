#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>

char* getString(){
    int size = 100;
    char* input = malloc(size);

    if (input == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }

    printf("Enter your input: ");
    
    if (fgets(input, size, stdin) != NULL) {
        int len = strlen(input);
        if (len > 0 && input[len - 1] == '\n') {
            input[len - 1] = '\0';
        }
        for (int i = 0; input[i] != '\0'; i++) {
            input[i] = (char)tolower((unsigned char)input[i]);
        }
        return input;
    } else {
        fprintf(stderr, "Error reading input\n");
        free(input);
        return NULL;
    }
}

char* validateString(){
    char* str = NULL;
    bool valid = false;

    do {
        if (str) {
            free(str);
            str = NULL;
        }

        str = getString();
        if (str == NULL) return 1;

        valid = true;

        if (str[0] == '\0'){
            valid = false;
        }

        for (int i = 0; str[i] != '\0'; i++) {
            unsigned char c = (unsigned char)str[i];

            if (!isalpha(c) && !isspace(c)) {
                valid = false;
                break;
            }
        }

        if (!valid) {
            fprintf(stderr, "Invalid input: only letters and spaces allowed. Please try again.\n");
        }

    } while (!valid);

    return str;
}

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
