#include <stdio.h>

void grant_access() {
    printf("Access Granted!\n");
}

void deny_access() {
    printf("Access Denied!\n");
}

int main() {
    int secret_code = 0;
    printf("Enter secret code: ");
    scanf("%d", &secret_code);

    if (secret_code == 1234) {
        grant_access();
    } else {
        deny_access();
    }

    return 0;
}
