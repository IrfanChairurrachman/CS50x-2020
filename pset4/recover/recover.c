#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>
#include <string.h>

typedef uint8_t BYTE;
#define READ 512



int main(int argc, char *argv[])
{
    // check if there's argv[2]
    if (argc < 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    // create file and newfile for jpg
    FILE *file = fopen(argv[1], "r");
    FILE *newimg;
    char newfile[7];

    if (!file)
    {
        printf("File is empty\n");
        return 1;
    }

    int i = 0;
    int cont = 0;
    BYTE buffer[READ];

    // repeat for each 512 byte
    while (fread(buffer, sizeof(BYTE), READ, file))
    {
        // check if new block is jpg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // if not first jpg then close
            if (i != 0)
                fclose(newimg);

            // create new jpg file
            sprintf(newfile, "%03i.jpg", i);
            newimg = fopen(newfile, "w");

            if (!newimg)
            {
                printf("Can't create new file\n");
                return 1;
            }

            cont = 1;
            i++;
        }

        // write the jpg file if condition fullfiled
        if (cont == 1)
        {
            fwrite(buffer, sizeof(BYTE), READ, newimg);
        }

    }

    // close all the open file before return 0
    fclose(file);
    fclose(newimg);

    return 0;
}
