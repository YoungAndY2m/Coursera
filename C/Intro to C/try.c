#include <stdio.h>
int myFunction(int n){
    int x = n * 2;
    int y = (x + 1) % 3;
    return y - x;
}

int g (int x, int y) {
  switch(x - y) {
  case 0:
    return x;
  case 4:
    y = y + 1;
    break;
  case 7:
    x = x - 1;
  case 9:
    return x*y;
  case 3:
    y = x + 9;
  default:
    return y - x;
  }
return y;
}

int fog (int n) {
  int ans = 0;
  for (int i = 1; i < n; i++) {
    if (i < n/2) {
      ans -= i;
    }
    else {
      ans += i;
    }
  }
  return ans;
}

void f (int x, int y) {
  while (x < y) {
    printf("%d ", y - x);
    x = x + 1;
    y = y - 1;
  }
}

int main(){
    printf("%d\n", myFunction(4));
    printf("%d\n", g(3, 0));
    f(-1, 4);
    printf("%d\n", fog(7));
    int a = 2;
    int b = 6;
    while (a <= b) {
        if (a % 2 == 1){
            printf("a is %d\n", a);
        }
        else {
            printf("b is %d\n", b);
            for (int i = 0; i < b - a; i++){
                printf("a * i + b = %d\n", a * i + b);
            }
        }
        a++;
        b--;
    }
}