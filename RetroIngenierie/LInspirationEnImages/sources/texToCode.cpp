#include <cstdlib>
#include <cstdio>
#include <string>

int main(int argc, char** argv) {
    if (argc != 3)
    {
        printf("f2bytes row file\n");
        printf("row = after how many bytes to add a new line (0 for continuous)\n");
        printf("file = the name of the input file that should be converted\n");
        printf("note: a new file with the same name but .cpp appended will be create as output");
        return EXIT_FAILURE;
    }

    int rowl = atoi(argv[1]);

    std::string fsn(argv[2]);
    std::string fdn(argv[2]);
    fdn.append(".cpp");

    FILE* fs = fopen(fsn.c_str(), "rb");
    if (!fs)
        printf("Failed to open source file %s \n", fsn.c_str());

    FILE* fd = fopen(fdn.c_str(), "w");
    if (!fd)
        printf("Failed to open destination file %s \n", fdn.c_str());

    printf("transferring from %s to %s with row length of %d", fsn.c_str(), fdn.c_str(), rowl);

    fprintf(fd, "static const unsigned char file_data[] = {");

    if (rowl != 0) fprintf(fd, "\n");

    int n = 0;
    while(!feof(fs)) {
        unsigned char c;
        if(fread(&c, 1, 1, fs) == 0) break;
        fprintf(fd, "0x%.2X,", (int)c);
        ++n;
        if(rowl !=0 && n % rowl == 0) fprintf(fd, "\n");
    }

    fprintf(fd, "};\n");

    fclose(fs);
    fclose(fd);

    return EXIT_SUCCESS;
}
