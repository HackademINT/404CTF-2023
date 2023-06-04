#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#define LENGTH 8

using namespace std;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef unsigned char uchar;

int main(int argc, char* argv[]) {
    //vérification de la bonne utilisation de la fonction
    if (argc != 3) {
        cout << "Erreur : il faut fournir deux arguments\n\nUtilisation -> ./flagInject [flag] [key]\n\nOù\n- flag est un nombre hexadécimal de 32 bits (suite d'inputs de 7 segments, cf non.txt)\n- key est un nombre hexadécimal, d'une longueur multiple de 2 octets, maximum 8" << endl;
        return -1;
    }

    //parsing de la string d'entrée
    string const hexFlag(argv[1]);
    if (hexFlag.length() != 64) {
        cout << "Erreur : la longueur du flag doit être de 32 bits (64 chars hexadécimaux)" << endl;
        return -1;
    }
    string hexKey(argv[2]);
    if ((hexKey.length() > 8) || (hexKey.length()%2 != 0)) {
        cout << "Erreur : la longueur de la clé doit être de 2 ou 4 octets" << endl;
        return -1;
    }

    //génération du flag
    int keyLength=hexKey.length();
    int keyRepeats=64/keyLength;
    string encFlag(64,'0');
    ostringstream* tempSSef = new ostringstream(""); //parce qu'on fait les choses prore
    uchar* tempSf=new uchar(0);                      //enfin je crois ?
    uchar* tempSk=new uchar(0);
    for(uint i(0); i<64; i+=2){
        *tempSf=stoi(hexFlag.substr(i,2),nullptr,16);
        *tempSk=stoi(hexKey.substr(i%keyLength,2),nullptr,16);
        *tempSSef << setw(2) << setfill('0') << hex << (uint)(0xff&(~(*tempSf^*tempSk)));
    }
    string encryptedFlag(tempSSef->str());
    delete tempSSef;
    delete tempSf;
    delete tempSk;

    //résolution des offsets de la rom
    string r1txt(""),r2txt("");
    uint const pos1[LENGTH] {4,36,40,12,48,20,28,60};
    uint const pos2[LENGTH] {32,0,8,44,16,52,56,24};
    for (uint i(0); i<LENGTH; i++) {
        if (i%2==0 and i!=0) {
            r1txt += " ";
            r2txt += " ";
        }
        r1txt += encryptedFlag.substr(pos1[i],4);
        r2txt += encryptedFlag.substr(pos2[i],4);
    }

    //écriture dans les fichiers
    ofstream rom1("rom_1.txt");
    if (rom1) {
        rom1 << "v2.0 raw" << endl;
        rom1 << r1txt;
        cout << "rom_1.txt écrit avec succès." << endl;
    } else {
        cout << "Impossible d'utiliser le flux rom1" << endl;
        return -1;
    }

    ofstream rom2("rom_2.txt");
    if (rom2) {
        rom2 << "v2.0 raw" << endl;
        rom2 << r2txt;
        cout << "rom_2.txt écrit avec succès." << endl;
    } else {
        cout << "Impossible d'utiliser le flux rom2";
        return -1;
    }
    return 0;
}
