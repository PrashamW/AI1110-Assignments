#include <stdio.h>
#include <stdlib.h>
#include "coeffs.h"

int main()
{
    double m = mean("gau.dat");
    double v = variance("gau.dat");
    printf("Mean of the given data = %lf\n", m);
    printf("Variance of the given data = %lf\n", v);
}
// Mean = 0.000326, Variance = 0.1.000907