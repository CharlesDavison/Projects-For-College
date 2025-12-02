#include <stdio.h>

struct Product{
        char* Names;
        int Prices;
};

int main(void){
        struct Product Products[5];

        for (int i = 0; i < 5; i++){
                printf("Please Enter The Name Of The Product");
                scanf("%s", Products[i].Names);

                printf("Please Enter The Price For That Product");
                scanf("%d", Products[i].Prices);
        }
        return 0;
}