
#include "sensor.h"

double dado_medido = 0;

double sensor_get_dados()
{
    dado_medido += 100;
    if(dado_medido == 1000)
    {
        dado_medido = 0;
    }
    return dado_medido;
}