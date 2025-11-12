#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>

char* getString(){
    size_t size = 100;
    char* input = malloc(size);

    if (input == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return NULL;
    }

    printf("Enter your input: ");
    
    if (fgets(input, size, stdin) != NULL) {
        size_t len = strlen(input);
        if (len > 0 && input[len - 1] == '\n') {
            input[len - 1] = '\0';
        }
        for (size_t i = 0; input[i] != '\0'; i++) {
            input[i] = (char)tolower((unsigned char)input[i]);
        }
        return input;
    } else {
        fprintf(stderr, "Error reading input\n");
        free(input);
        return NULL;
    }
}

char** bubbleSort(char** array, int arrayLen){
    bool sorted;
    for(int i = 0; i < arrayLen - 1; i++){
        sorted = true;

        for(int j = 0; j < arrayLen - 1 - i; j++){
            if(strcmp(array[j], array[j+1]) > 0){
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
    char *str = NULL;
    bool valid = false;

    do {
        if (str) {
            free(str);
            str = NULL;
        }
        str = getString();
        if (str == NULL) return 1;

        valid = true;
        for (size_t i = 0; str[i] != '\0'; i++) {
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

    char* array[100];
    int arrayLen = 0;

    char* token = strtok(str, " ");

    while (token != NULL) {
        array[arrayLen] = token;
        token = strtok(NULL, " ");
        arrayLen++;
    }

    char** newArray = bubbleSort(array, arrayLen);


    for (int j = 0; j < arrayLen; j++){
        printf("%s\n", newArray[j]);
    }

    free(str);

    return 0;
}