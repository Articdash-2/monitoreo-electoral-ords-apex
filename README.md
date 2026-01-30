🗳️ Sistema de Monitoreo Electoral (ORDS + APEX + Python)
Este proyecto es un ecosistema completo para la captura, procesamiento y visualización de datos electorales en tiempo real, conectando una base de datos local con la nube de Oracle.

📁 Estructura del Proyecto
El repositorio está organizado en cuatro capas críticas:

1. 🗄️ /database (El Corazón)
   Aquí reside la lógica de negocio en la base de datos Oracle.

pkg_monitoreo.sql: Contiene el paquete PL/SQL encargado de procesar las actas, validar los datos y asegurar la integridad de la votación.

Acción: Define las tablas de candidatos, partidos y resultados.

2. 🔌 /apex_rest (El Puente)
   La capa de comunicación que expone nuestra base de datos al mundo.

test.app.sql: Es la exportación de los ORDS Restful Services.

Acción: Define los endpoints (URLs) que reciben los archivos JSON enviados por el agente de Python y los insertan en las tablas mediante el paquete de la base de datos.

3. 🤖 /python_agent (La Inteligencia)
   El script encargado de la automatización.

test_oracle.py: Un agente programado en Python que extrae información local, la procesa y la envía vía POST a la API de APEX.

requirements.txt: Lista de librerías necesarias (requests, cx_Oracle, etc.).

4. 🚇 /tunnel_config (El Acceso)
   La configuración de conectividad segura.

setup_tunnel.sh: Instrucciones para levantar zrok desde Kali Linux (WSL).

Acción: Permite que el tráfico de la nube de Oracle APEX llegue de forma segura a nuestro entorno local a través de un túnel público.

🚀 Flujo de Datos
El Agente Python lee los datos de la base local.

Los datos viajan por el Túnel zrok hacia la nube.

ORDS (APEX) recibe los datos y ejecuta el Paquete PL/SQL.

La información se visualiza en el Dashboard de APEX.
