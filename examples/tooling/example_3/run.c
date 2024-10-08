#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void secret_function() {
    printf("Congrats! You've entered the secret function!\n");
}

void vulnerable_function() {
    char buffer[64];

    printf("Enter something: ");
    fgets(buffer, sizeof(buffer), stdin);  // Vulnerable to overflow
    printf("You entered: %s\n", buffer);
}

int main() {
    vulnerable_function();
    return 0;
}
