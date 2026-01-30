# 🗳️ Sistema de Monitoreo Electoral (E2E)
> **Arquitectura Híbrida:** Oracle DB ➡️ Python ➡️ Zrok Tunnel ➡️ Oracle APEX Cloud

![Oracle](https://img.shields.io/badge/Oracle-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![APEX](https://img.shields.io/badge/Oracle%20APEX-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![Zrok](https://img.shields.io/badge/Zrok-Tunnel-6340FF?style=for-the-badge)

## 📝 Descripción del Proyecto
Este ecosistema permite la captura de datos electorales desde una base de datos local y su transmisión segura hacia un Dashboard en la nube de **Oracle APEX**. Utiliza un agente de **Python** para la orquestación y **zrok** para superar barreras de red.

## 🏗️ Arquitectura del Sistema

```mermaid
graph TD
    subgraph Entorno_Local
        DB[Oracle Database 21c] -- "PL/SQL Package" --> AGENT[Agente Python]
        AGENT -- "JSON/REST" --> TUNNEL[zrok Tunnel]
    end

    subgraph Entorno_Nube
        TUNNEL -- "SSL/TLS" --> ORDS[ORDS REST Services]
        ORDS --> APEX[Oracle APEX Dashboard]
    end
 
```
