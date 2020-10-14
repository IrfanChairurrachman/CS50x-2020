#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            candidates[i].votes += 1;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO
    int votwin, n;
    string namewin;

    for (int i = 1; i < candidate_count; i++)
    {
        votwin = candidates[i].votes;
        namewin = candidates[i].name;
        n = i - 1;
        while (n >= 0 && candidates[n].votes > votwin)
        {
            candidates[n + 1].name = candidates[n].name;
            candidates[n + 1].votes = candidates[n].votes;
            n = n - 1;
        }
        candidates[n + 1].name = namewin;
        candidates[n + 1].votes = votwin;
    }

    int x = 0;
    string winner[candidate_count];
    winner[0] = candidates[candidate_count - 1].name;

    for (int i = candidate_count - 1; i >= 0; i--)
    {
        if (candidates[i].votes == candidates[i - 1].votes)
        {
            x += 1;
            winner[x] = candidates[i - 1].name;

        }

    }

    for (int i = 0; i <= x; i++)
    {
        printf("%s\n", winner[i]);
    }
}

