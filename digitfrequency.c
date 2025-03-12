#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str[1000];
    fgets(str, sizeof(str), stdin);
    int digit_count[10] = {0};
    for (int i = 0; str[i] != '\0'; i++) {
        if (isdigit(str[i])) {  
            digit_count[str[i] - '0']++;  
        }
    }
    for (int i = 0; i < 10; i++) {
        printf("%d ", digit_count[i]);
    }
    return 0;
}
