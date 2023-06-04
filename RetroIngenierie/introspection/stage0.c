#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//404CTF{5t3althy_f1Le$-4nD_aUt0matIon}

int main(int argc, char **argv){
    if (argc < 2){
        printf("Usage : ./introspection [MOT DE PASSE]\n");
        return 1;
    }

    if(!strcmp(argv[1], "5t3althy_f1Le$-4nD_aUt0matIon")){
        printf(":)\n");
        return 0;
    }
    printf(":(\n");
    return 0;
}