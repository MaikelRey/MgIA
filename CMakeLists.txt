# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION ${CMAKE_VERSION})
project(MusicGenerator C CXX)

# Check if the C++ compiler supports '$' in identifiers (This part es opcional).
include(CheckSourceCompiles)
check_source_compiles(C
"extern int dollar$(void);
int main() { return 0; }"
C_SUPPORTS_DOLLAR)

# Configura el proyecto, aquí no necesitamos crear ninguna fuente de símbolos.
add_executable(MusicGeneratorExecutable main.c)  # Cambié el nombre a "MusicGeneratorExecutable" o el nombre de tu ejecutable
set(CMAKE_SYSTEM_VERSION 8.1 CACHE STRING "Use Windows SDK 8.1")
