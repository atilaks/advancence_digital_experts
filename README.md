# jerarquía de archivos:
  Programa
    core_department
      department
      bike
      complaint
      owner(individual)
      agent(department_manager(individual))
     exceptions 
     api_geocode
      
# tareas pendientes:
  - Api para notificación de cambio de estado.
  - Persistencia de los datos: No registra ni almacena en ninguna base de datos. Sugiero plataformas como Oracle o MySql y formatos como json o csv.
    + Metodos de Guardado y Cargado de datos.
  - Aplicación Fronend.
    + MainProgram para gobernar el código.
  - Documentación de Apis.
  - Las coordenadas podrian guardarse un un diccionario con el fin de generar en un futuro un mapa de incidencias donde localizar zonas de alta densidad.

# Nota:
  - Para utilizar Api Geocode es necesario aportar key propia.
  - Construido integramente con TDD.
