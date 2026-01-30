# 🗳️ Sistema de Monitoreo Electoral (E2E)
> **Arquitectura Híbrida:** Oracle DB ➡️ Python ➡️ Zrok Tunnel ➡️ Oracle APEX Cloud

![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![APEX](https://img.shields.io/badge/Oracle%20APEX-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![Zrok](https://img.shields.io/badge/Zrok-Tunnel-6340FF?style=for-the-badge)

## 📋 Descripción del Proyecto
Este ecosistema permite la captura de datos electorales desde una base de datos local y su transmisión segura hacia un Dashboard en la nube de **Oracle APEX**. Utiliza un agente de **Python** para la orquestación y **zrok** para superar barreras de red (NAT/Firewalls) mediante túneles seguros.

## 🏗️ Arquitectura del Sistema
```mermaid
graph TD
    subgraph "Entorno Local (On-Premise)"
        DB[(Oracle Database 21c)] -- "PL/SQL Package" --> AGENT[Agente Python]
        AGENT -- "JSON/REST" --> TUNNEL{zrok Tunnel}
    end

    subgraph "Entorno Nube (Oracle Cloud)"
        TUNNEL -- "SSL/TLS" --> ORDS[ORDS / REST Services]
        ORDS --> APEX[Oracle APEX Dashboard]
    end


📁 Organización del Repositorio
📂 /database: Scripts DDL y DML. Contiene el paquete pkg_monitoreo.sql que procesa la lógica de las actas.

📂 /apex_rest: Definiciones de los servicios ORDS. Aquí se mapean los Endpoints que reciben el flujo de datos.

📂 /python_agent: El cerebro del envío. Script test_oracle.py que automatiza la extracción y el POST hacia la nube.

📂 /tunnel_config: Configuraciones de conectividad para WSL (Kali Linux) y scripts de levantamiento de túnel.

🚀 Inicio Rápido
Configurar Base de Datos: Ejecutar los scripts en /database para crear la estructura de tablas y paquetes.

Levantar el Túnel (Kali Linux/WSL):

Bash
zrok share public http://localhost:8080 --backend-mode proxy
Ejecutar el Agente: Configurar la URL proporcionada por zrok en el script de Python y ejecutar:

Bash
python python_agent/test_oracle.py
Desarrollado por [Articdash-2] - Proyecto de Monitoreo Electoral en Tiempo Real.
