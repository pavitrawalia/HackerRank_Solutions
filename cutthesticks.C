#include <stdio.h>
int main() {
  int n, t, i, j, count;
  count = 0;
  scanf("%d", &n);
  int b[n];
  for (i = 0; i < n; i++) {
    scanf("%d", &b[i]);
  }
  t = b[0];
  for (i = 0; i < n; i++) {
    if (t > b[i]) {
      t = b[i];
    }
  }
  while (t > 0) {
    for (i = 0; i < n; i++) {
      b[i] = b[i] - t;
      if (b[i] >= 0) {
        count = count + 1;
      }
    }
    printf("%d\n", count);
    count = 0;
    for (j = 0; j < n; j++) {
      t = b[j];
      if (t > 0) {
        break;
      }
    }
    for (i = 0; i < n; i++) {
      if (t > b[i] && b[i] > 0) {
        t = b[i];
      }
    }
  }
}
