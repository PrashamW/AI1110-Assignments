#include <stdio.h>
#include <stdlib.h>
#include "coeffs.h"

int main()
{
    double m = mean("uni.dat");
    double v = variance("uni.dat");
    printf("Mean of the given data = %lf\n", m);
    printf("Variance of the given data = %lf\n", v);
}
// Mean = 0.500007, Variance = 0.083301