
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

typedef uint8_t BYTE;
#define READ 512;

int main(int argc, char *argv[])
{


    // Ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // Open input file
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        return 1;
    }

    int i = 0;
    int keep = 0;
    char filename[8];
    FILE *img = NULL;

    // Copy source to destination, 512 BYTEs at a time
    BYTE buffer[512];
    while (fread(buffer, sizeof(BYTE), 512, file))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Check if it is the first JPEG
            if (i != 0)
            {
                // Close previous file
                fclose(img);
            }
            else
            {
                keep = 1;
            }

            // Open output file
            sprintf(filename, "%03i.jpg", i);
            img = fopen(filename, "w");
            if (img == NULL)
            {
                fprintf(stderr, "Could not create %s.\n", filename);
                return 1;
            }
            fwrite(buffer, sizeof(BYTE), 512, img);
            i++;
        }

        // Keep writing JPEG
        if (keep == 1)
        {
            fwrite(buffer, sizeof(BYTE), 512, img);
        }
    }
    fclose(file);
    fclose(img);
    return 0;
}