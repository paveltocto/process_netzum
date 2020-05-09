# Prueba Netzun
[![Build status](https://dev.azure.com/UGOTeam/LMS/_apis/build/status/PAO%20BACK%20CI)](https://dev.azure.com/UGOTeam/LMS/_build/latest?definitionId=6)  
This is an example file with default selectionse.
​
## Instalación
Pre requisitos:
- macOS o Linux
- Tener make instalado (si usas windows usa un terminal con bash o instala [Make](http://gnuwin32.sourceforge.net/packages/make.htm) )
​
Para instalar las dependencias del proyecto ejecute el siguiente comando:
```
make install 
```
​
## Uso
Para iniciar el proyecto
```
make start 
```
Para verificar que el servicio este levantado: http://localhost:8000
​
Para detener el proyecto 
```
make stop
```
Para para saber los demás comandos disponibles
```
make help 
```
## Construir (Docker)
Para empaquetar el proyecto y dejarlo listo par desplegar
```
make build
```
​

