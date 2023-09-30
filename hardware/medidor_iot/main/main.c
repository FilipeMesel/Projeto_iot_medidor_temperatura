#include <stdio.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "nvs_flash.h"
#include "my_data.h"
#include "wifi.h"
#include "sensor.h"

// Defina o tamanho da fila para os valores a serem enviados
#define QUEUE_SIZE 10

// Declare a fila global com capacidade suficiente
QueueHandle_t data_queue;

// Task para postar dados
void post_task(void *pvParameters)
{
    
    
    nvs_flash_init();
    wifi_connection();

    vTaskDelay(2000 / portTICK_PERIOD_MS);
    printf("WIFI was initiated ...........\n\n");

    double valor;
    while (1)
    {
        // Tente obter os dados da fila sem esperar
        if (xQueueReceive(data_queue, &valor, 0) == pdTRUE)
        {
            // Execute a função de postagem com o valor
            post_rest_function(valor);
        }

        // Espere por um segundo antes de verificar novamente
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}

// Task para adicionar dados à fila
void add_data_task(void *pvParameters)
{
    double valor = 0.0;
    while (1)
    {
        // Tente adicionar os dados à fila sem esperar
        if (xQueueSend(data_queue, &valor, 0) == pdTRUE)
        {
            // Incrementa o valor para a próxima iteração
            valor = sensor_get_dados();
        }

        // Espere por um segundo antes de adicionar mais dados
        vTaskDelay(1000 / portTICK_PERIOD_MS);
    }
}

void app_main(void)
{
    // Inicialize a fila com capacidade suficiente
    data_queue = xQueueCreate(QUEUE_SIZE, sizeof(double));
    
    // Crie as tasks
    xTaskCreate(&post_task, "post_task", (4*1024), NULL, 4, NULL);
    xTaskCreate(&add_data_task, "add_data_task", (4*1024), NULL, 5, NULL);
}
