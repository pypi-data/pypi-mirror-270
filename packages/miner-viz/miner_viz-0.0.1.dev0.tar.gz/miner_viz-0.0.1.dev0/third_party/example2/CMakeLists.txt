project(example2)

add_library(${PROJECT_NAME} src/main.cc)

target_include_directories(${PROJECT_NAME} PUBLIC ${PROJECT_SOURCE_DIR}/include)