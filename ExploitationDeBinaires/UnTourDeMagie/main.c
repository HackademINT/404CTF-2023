#include<stdlib.h>
#include<stdio.h>

int main() {
    int* check = malloc(sizeof(int));
    *check = 0xcb0fcb0f;
    puts("Alors, t'es un magicien ?");
    char input[20];
    fgets(input, 200, stdin);
    
	if(*check == 0xcb0fcb0f) {
		puts("Apparemment non...");
		exit(0);
	}
    if(*check != 0xcb0fcb0f && *check != 0x50bada55) {
		puts("Pas mal, mais il en faut plus pour m'impressionner !");
		exit(0);
	}
	if(*check == 0x50bada55) {
		puts("Wow ! Respect ! Quelles paroles enchantantes ! Voilà ta récompense...");
		FILE* f = fopen("flag.txt", "r");
		if(f == NULL) {
			puts("Erreur lors de l'ouverture du flag, contactez un administrateur !");
			exit(1);
		}
		char c;
		while((c = fgetc(f)) != -1) {
			putchar(c);
		}
		fclose(f);
	}
}
