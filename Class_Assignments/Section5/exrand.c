#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int main(void) // main function begins
{

    // random numbers
    bernoulli("ber.dat", 1000000);
    gen_Y("gen_Y.dat", 1000000, sqrt(10));
    ber_prob(1000000, sqrt(10));

    // Mean of uniform
    // printf("%lf",mean("uni.dat"));
    return 0;
}