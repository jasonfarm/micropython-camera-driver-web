# Create an INTERFACE library for our C module.
add_library(usermod_esp32camera INTERFACE)

# Add our source files to the lib
target_sources(usermod_esp32camera INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}/modcamera.c
    ${CMAKE_CURRENT_LIST_DIR}/app_httpd.c
        ${CMAKE_CURRENT_LIST_DIR}/app_http_car.c
)

# Add the current directory as an include directory.
target_include_directories(usermod_esp32camera INTERFACE
    ${CMAKE_CURRENT_LIST_DIR}
    ${IDF_PATH}/components/esp32-camera/driver/include
    ${IDF_PATH}/components/esp32-camera/driver/private_include
    ${IDF_PATH}/components/esp32-camera/conversions/include
    ${IDF_PATH}/components/esp32-camera/conversions/private_include
    ${IDF_PATH}/components/esp32-camera/sensors/private_include

    ${IDF_PATH}/components/esp_http_server/include
    ${IDF_PATH}/components/http_parser
)

target_compile_definitions(usermod_esp32camera INTERFACE)

# Link our INTERFACE library to the usermod target.
target_link_libraries(usermod INTERFACE usermod_esp32camera)