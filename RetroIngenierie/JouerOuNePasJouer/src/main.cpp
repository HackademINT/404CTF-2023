#include <switch.h>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <limits>
#include <seadRandom.h>

// Seed: 17734365728342759975

const u64 rounds[4] = {
    // Unknown1 : 3741809953062610089ul
    // Unknown2 : 18250463920478301614ul
    // Unknown3 : 6856677364424716256ul
    // Unknown4 : 10067764222108277103ul
    15323416860013248078ul,
    2038102213101842551ul,
    9039777371918867651ul,
    5323617266019954679ul
};

// "Veemo! 404CTF{Un3_s33d_s34d-[seed]}" - Une seed sead
// Le seed n'est pas spécifiée à cette étape pour assurer que le travail a été fait jusqu'au bout et que ce ne soit pas seulement le state d'origine de trouvé...
// Clé AES-256-CBC : Unknown1 à 4 en hex *LITTLE ENDIAN* mis bout à bout (a96451cd5394ed33ae2d31963dac46fde02fff15bccf275f6f9926fd37e2b78b)
const char enc[] {0x04,0x8c,0xed,0x7d,0x00,0x4c,0x2a,0xb9,0x6c,0x1c,0x37,0xeb,0x1d,0x17,0xc9,0xb3,0x88,0xb4,0x1a,0x9e,0xbd,0x9e,0x57,0xa8,0x8b,0x50,0x2c,0x71,0xbe,0x0f,0xc0,0x46,0x34,0xa4,0x4e,0xde,0xa8,0x02,0xbc,0x18,0x0a,0x09,0xc1,0x36,0x33,0xff,0x16,0x1f};
int main(int argc, char** argv) {
    consoleInit(NULL); // Initialises the screen.

    padConfigureInput(8, HidNpadStyleSet_NpadStandard);

    printf("Demarrage de S4v3Unl0ck3r...\nDeverrouillage de la sauvegarde...\n");

    for (int i = 0; i < 4; i++)
       printf("Woomy! ???????????????????????\n");
    for (int i = 0; i < 4; i++)
        printf("Woomy! %lu\n", rounds[i]);

    printf("Donnees corrompues ! Cle necessaire pour continuer\n");

    consoleUpdate(NULL);

    PadState pad;
    padInitializeAny(&pad);

    SwkbdConfig kbd;
    Result res = swkbdCreate(&kbd, 0);
    if (R_SUCCEEDED(res)) {
        swkbdConfigMakePresetDefault(&kbd);
        swkbdConfigSetInitialText(&kbd, "Entrez la cle.");
        swkbdConfigSetStringLenMax(&kbd, 20);
        swkbdConfigSetType(&kbd, SwkbdType_NumPad);
        char kbdstr[21] = {0};
        res = swkbdShow(&kbd, kbdstr, sizeof(kbdstr));
        swkbdClose(&kbd);
        if (R_SUCCEEDED(res)) {
            u64 seed = std::stoul(kbdstr);
            sead::Random rnd(seed);
            bool valid = true;
            u64 calcRounds[8];
            for (int i = 0; i < 8; i++) {
                calcRounds[i] = rnd.getU64();
                printf("Woomy! %lu\n", calcRounds[i]);
                if (i >= 4 && rounds[i-4] != calcRounds[i]) // vérification de la validité des valeurs connues
                    valid = false;
            }
            if (valid) {
                char key[32];
                char iv[32] = {0};
                char out[64] = {0};
                for (int i = 0; i < 4; i++) {
                    memcpy(key + 8*i, &calcRounds[i], sizeof(u64));
                }
                for (int i = 0; i < SHA256_HASH_SIZE; i++) {
                    printf("%02x", key[i]);
                }
                printf("\n");
                Aes256CbcContext ctx;
                aes256CbcContextCreate(&ctx, key, iv, false);
                aes256CbcDecrypt(&ctx, out, enc, sizeof(enc));
                printf("%s\n", out);
            }
            else {
                printf("Splat! Entree invalide...\n");
            }
        }
        else {
            printf("Probleme lors de l'affichage du clavier.\n");
        }
    }
    else {
        printf("Probleme lors de l'initialisation du clavier.\n");
    }

    printf("Appuyez sur + pour quitter.\n");

    while (appletMainLoop()) {
        padUpdate(&pad);
        u64 kDown = padGetButtonsDown(&pad);

        if (kDown & HidNpadButton_Plus) { break; }

        consoleUpdate(NULL);
    }

    consoleExit(NULL);
    return 0;
}