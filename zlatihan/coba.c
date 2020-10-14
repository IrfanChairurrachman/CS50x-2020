#include <stdio.h>
#include <math.h>

// typedef struct
// {
//     int red;
//     int green;
//     int blue;
// }
// copyi;

int main()
{
    // int width = 4;
    // int height = 5;
    // int a = 2;
    // int b = 3;
    // if ((a > 0 && a < width - 1) && (b > 0 && b < height - 1))
    //     printf("Yes\n");
    // else
    //     printf("No\n");

    // int red[5];

    // red[0] = 1;
    // red[1] = 2;

    // for (int i = 0; i < 2; i++)
    //     printf("%i ", red[i]);
    int height = 5;
    int width = 5;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            printf("%i %i \n", i, j);
            int c = 0;

            for (int l = -1; l < 2; l++)
            {
                for (int m = -1; m < 2; m++)
                {
                    printf("  %i %i ", (i +l), (j + m));
                    int a = i + l;
                    int b = j + m;

                    if ((a >= 0 && a < height) && (b >= 0 && b < width))
                    {
                        printf("Yes\n");
                        c++;
                    }
                    else
                    {
                        printf("Not\n");
                    }
                }
            }
            printf("== %i ==\n", c);
        }
    }
    // int width = 5;

    // int A[5] = {0, 1, 2, 3, 4};

    // int k = width - 1;

    // printf("%i\n\n", width/2);
    // for (int i = 0; i < width/2; i++)
    // {
    //     int a = A[i];
    //     A[i] = A[k];
    //     A[k] = a;
    //     printf("%i ", A[i]);
    //     printf("%i\n", k);

    //     k--;
    // }

    // for (int i = 0; i < width; i++)
    //     printf("%i ", A[i]);

    return 0;
}