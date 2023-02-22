#include <stdio.h>
#include <main.h>

/**
 * main - entrypoint
 * Description: prints the alphabet, in lowercase, followed by a new line
 * Return: Always (0) Success
*/

int main(void)
{
	print_alphabet();
	return (0);
}

void print_alphabet(void)
{
    char letter = 'a';
    while (letter <= 'z') {
        printf("%c", letter);
        letter++;
    }
    printf("\n");
}
