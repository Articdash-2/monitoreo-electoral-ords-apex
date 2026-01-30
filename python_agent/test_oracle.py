import oracledb
import requests
import json

# --- 1. CONFIGURACIÓN DE RUTAS ---
# Esta es la URL del nuevo manejador POST en test.app
URL_API_NUBE = "https://oracleapex.com/ords/pays_off/test/monitoreo/"

# Configuración de tu base local
DB_LOCAL = {
    "user": "system",
    "pass": "", # ¡No olvides ponerla!
    "dsn": "localhost:1522/xe"
}

def ejecutar_hack():
    try:
        # --- 2. EXTRACCIÓN LOCAL ---
        # Conexión en Thin Mode (sin Thick Mode)
        conn = oracledb.connect(user=DB_LOCAL["user"], password=DB_LOCAL["pass"], dsn=DB_LOCAL["dsn"])
        cursor = conn.cursor()
        
        cursor.execute("SELECT SUM(cantidad_personas) FROM votaciones")
        total_local = cursor.fetchone()[0]
        print(f"✅ Dato detectado en SQL local: {total_local}")

        # --- 3. EL GOLPE A LA NUBE (Vía zrok/Puerto 443) ---
        # El payload p_cantidad debe coincidir con el del manejador POST
        payload = {"p_cantidad": total_local} 
        headers = {'Content-Type': 'application/json'}
        
        print(f"🚀 Enviando hack a la nube...")
        response = requests.post(URL_API_NUBE, json=payload, headers=headers)

        # --- 4. VERIFICACIÓN ---
        if response.status_code == 200 or response.status_code == 201:
            print("💎 ¡Éxito total! La nube ha procesado el 1001.")
        else:
            print(f"❌ Fallo en el túnel (Status {response.status_code})")

    except Exception as e:
        print(f"💥 Error en el agente: {e}")
    finally:
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    print("🤖 Agente iniciado. Esperando túnel zrok...")
    ejecutar_hack()