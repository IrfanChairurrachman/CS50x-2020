#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;

            int gray = round((red + green + blue) / 3);

            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtBlue = gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // get pixels
            float red = image[i][j].rgbtRed;
            float green = image[i][j].rgbtGreen;
            float blue = image[i][j].rgbtBlue;

            // generate new pixel
            int sred = round(.393 * red + .769 * green + .189 * blue);
            int sgreen = round(.349 * red + .686 * green + .168 * blue);
            int sblue = round(.272 * red + .534 * green + .131 * blue);

            if (sred > 255)
            {
                sred = 255;
            }
            if (sgreen > 255)
            {
                sgreen = 255;
            }
            if (sblue > 255)
            {
                sblue = 255;
            }

            image[i][j].rgbtRed = sred;
            image[i][j].rgbtGreen = sgreen;
            image[i][j].rgbtBlue = sblue;
        }
    }
    return;
}


// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int k = 0;

    // reflect pixel
    for (int i = 0; i < height; i++)
    {
        k = width - 1;
        for (int j = 0; j < width / 2; j++)
        {
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            int blue = image[i][j].rgbtBlue;

            image[i][j].rgbtRed = image[i][k].rgbtRed;
            image[i][j].rgbtGreen = image[i][k].rgbtGreen;
            image[i][j].rgbtBlue = image[i][k].rgbtBlue;

            image[i][k].rgbtRed = red;
            image[i][k].rgbtGreen = green;
            image[i][k].rgbtBlue = blue;

            k--;
        }
    }

    return;
}

// create struct to store pixel
typedef struct
{
    int redd;
    int greenn;
    int bluee;
}
bllur;
// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    bllur blurred[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // get new pixel and the neighbor pixel
            float red[9];
            float green[9];
            float blue[9];

            int c = 0;

            for (int l = -1; l < 2; l++)
            {
                for (int m = -1; m < 2; m++)
                {
                    int a = i + l;
                    int b = j + m;

                    if ((a >= 0 && a < height) && (b >= 0 && b < width))
                    {
                        red[c] = image[a][b].rgbtRed;
                        green[c] = image[a][b].rgbtGreen;
                        blue[c] = image[a][b].rgbtBlue;
                        c++;
                    }
                }
            }

            for (int l = 1; l < c; l++)
            {
                red[0] += red[l];
                green[0] += green[l];
                blue[0] += blue[l];
            }

            int bred = round(red[0] / c);
            int bgreen = round(green[0] / c);
            int bblue = round(blue[0] / c);

            // store new pixel to external struct
            blurred[i][j].redd = bred;
            blurred[i][j].greenn = bgreen;
            blurred[i][j].bluee = bblue;

        }
    }

    // generate new pixel to image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = blurred[i][j].redd;
            image[i][j].rgbtGreen = blurred[i][j].greenn;
            image[i][j].rgbtBlue = blurred[i][j].bluee;
        }
    }

    return;
}
