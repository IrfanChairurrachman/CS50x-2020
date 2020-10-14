#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Initiate variabel
    int words = 0;
    int letters = 0;
    int sentences = 0;

    string text = get_string("Text: ");

    // store counts on variable
    if (text)
    {
        letters = count_letters(text);
        words = count_words(text);
        sentences = count_sentences(text);
    }

    float L = ((float) letters / (float) words) * 100;
    float S = ((float) sentences / (float) words) * 100;

    // count grade
    float grade = 0.0588 * L - 0.296 * S - 15.8;

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", (int) round(grade));
    }
}

// function for counting
int count_letters(string s)
{
    int letters = 0;
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // from uppercase to z lower
        if (s[i] >= 'A' && s[i] <= 'z')
        {
            // printf("%c", s[i] - 32);
            letters += 1;
        }
    }
    return letters;
}

int count_words(string s)
{
    int words = 1;
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // check if space
        if (s[i] == ' ')
        {
            words += 1;
        }
    }
    return words;
}
int count_sentences(string s)
{
    int sentences = 0;
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        // check if space
        if ((s[i] == '!') || (s[i] == '.') || (s[i] == '?'))
        {
            sentences += 1;
        }
    }
    return sentences;
}
