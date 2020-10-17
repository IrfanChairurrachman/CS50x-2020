// Implements a dictionary's functionality
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 65536;

// Hash table
node *table[N];

// declare variable to count word
int count = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // TODO
    int index = hash(word);

    node *cursor = table[index];

    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }

        cursor = cursor->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO
    uint32_t hash = 0;
    while (*word)
    {
        hash = (hash << 2) ^ (*word | 0x20);
        word++;
    }

    // return a value between 0 and 65535
    return (int)((hash >> 16) ^ (hash & 0xffff));

    // hash should only be used with N = 65536
    // from curiouskiwi at CS50 Discord
    // https://discord.com/channels/393846237255696385/395685061678071808/766046453750956052
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    // TODO
    // Open the dictionary file
    FILE *file = fopen(dictionary, "r");

    if (!file)
    {
        printf("Can not open file\n");
        return false;
    }

    // declare buffer
    char word[LENGTH + 1];

    // scan each word
    while (fscanf(file, "%s", word) != EOF)
    {
        // create node
        node *n = malloc(sizeof(node));

        if (n == NULL)
        {
            return false;
        }

        // copy word to node
        strcpy(n->word, word);
        n->next = NULL;

        int index = hash(n->word);

        if (table[index] == NULL)
        {
            table[index] = n;
            count++;
        }
        else
        {
            n->next = table[index];
            table[index] = n;
            count++;
        }
    }

    fclose(file);

    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    // TODO
    // iterate each array
    for (int i = 0; i < N; i++)
    {
        node *head = table[i];
        node *cursor = table[i];
        node *tmp = table[i];

        // iterate each linkedlist
        while (cursor != NULL)
        {
            cursor = cursor->next;
            free(tmp);
            tmp = cursor;
        }
    }
    return true;
}
