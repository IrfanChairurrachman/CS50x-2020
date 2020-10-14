#include <cs50.h>
#include <stdio.h>
int main(void)
{
    string s = "EMMA";
    printf("%p\n", &s[0]);
    printf("%c\n", *&s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
    printf("%p\n", &s[4]);
    printf("%c\n", *&s[4]);
}