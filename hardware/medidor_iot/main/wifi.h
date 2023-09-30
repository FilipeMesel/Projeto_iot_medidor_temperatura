#ifndef WIFI_H
#define WIFI_H

#include "esp_http_client.h"

void wifi_connection();
esp_err_t client_event_post_handler(esp_http_client_event_handle_t evt);
void post_rest_function(double value);

#endif /* WIFI_H */
