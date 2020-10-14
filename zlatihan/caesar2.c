#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

bool check(string s);

int main(int argc, string argv[])
{
    if ((argc == 2) && check(argv[1]))
    {
        int k = atoi(argv[1]);

        string text = get_string("plaintext: ");
        printf("ciphertext: ");

        for (int i = 0, n = strlen(text); i < n; i++)
        {
            // from uppercase to z lower
            if (text[i] >= 'a' && text[i] <= 'z')
            {
                printf("%c", (97 + (((text[i] - 97) + k) % 26)));
            }
            else if (text[i] >= 'A' && text[i] <= 'Z')
            {
                printf("%c", (65 + (((text[i] - 65) + k) % 26)));
            }
            else
            {
                printf("%c", text[i]);
            }
        }
        printf("\n");

        return 0;
    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

bool check(string s)
{
    int n = strlen(s);
    for (int i = 0; i < n; i++)
    {
        if (isdigit(s[i]))
        {
            continue;
        }
        else
        {
            return 0;
        }
    }
    return 1;
}
