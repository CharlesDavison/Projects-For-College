#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>

#include "stringHandling.h"

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
