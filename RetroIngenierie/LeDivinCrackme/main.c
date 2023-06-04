#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]){
    char buf[60];

    printf("Mot de passe ? : ");
    scanf("%60s", &buf);
    

    if (strlen(buf) == 30){
        if (!strncmp(buf+10, "Ph13_d4N5_", 10)){
            if (!strncmp(buf, "L4_pH1l0so", 10)){
                if (!strncmp(buf+20, "l3_Cr4cKm3", 10)){
                    printf("Bien joué ! Tu aurais été libre, pour cette fois...");
                    return 0;
                }
            }
        }
    } 
    printf("Navré mais c'est pas le bon mot de passe...");
    return 1;
}