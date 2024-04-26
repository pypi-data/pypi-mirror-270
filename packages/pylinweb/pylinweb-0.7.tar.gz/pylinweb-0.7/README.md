# Pylinweb

Pylinweb es una biblioteca de pruebas funcionales simple que utiliza Python, Selenium y Chrome driver.

## Pre-requisitos

Antes de instalar Pylinweb, asegúrate de tener instalado lo siguiente:

- Python
- Node.js
- JDK

## Instalación

Puedes instalar Pylinweb usando pip:

```bash
pip install pylinweb
```

Si necesitas una versión específica de Pylinweb, puedes especificarla así:

```bash
pip install pylinweb==version
```
## Uso

Una vez instalado, puedes usar Pylinweb con varios argumentos:

| Argumento   | Descripción                                           |
|-------------|-------------------------------------------------------|
| --version   | Imprime la versión de Pylinweb.                       |
| --setup     | Copia el directorio de la aplicación e instala las dependencias. |
| --run-tests | Ejecuta las pruebas.                                  |
| --report    | Genera un informe.                                    |
| --help      | Muestra la ayuda y explica cómo usar los argumentos.  |

Por ejemplo, para imprimir la versión de Pylinweb, puedes usar:

```bash
pylinweb --version
```
Para configurar tu aplicación, puedes usar:

```bash
pylinweb --setup
```
Esto copiará el directorio de la aplicación e instalará las dependencias necesarias.

Para ejecutar las pruebas, puedes usar:

```bash
pylinweb --run-tests
```
Y para generar un informe, puedes usar:

```bash
pylinweb --report
```

Reemplaza version con la versión específica de Pylinweb que deseas instalar.