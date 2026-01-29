--------------------------------------------------------
-- Archivo creado  - jueves-enero-29-2026   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Package PKG_VOTO_INTELIGENTE
--------------------------------------------------------

  CREATE OR REPLACE NONEDITIONABLE PACKAGE "SYSTEM"."PKG_VOTO_INTELIGENTE" AS
    -- Record para salida fina
    TYPE t_reporte IS RECORD (
        promedio NUMBER(10,2),
        estatus  VARCHAR2(20), -- 'CRITICO', 'NORMAL', 'EXCELENTE'
        mensaje  VARCHAR2(100)
    );

    FUNCTION obtener_analisis_completo(p_id_depto IN NUMBER) RETURN t_reporte;
END pkg_voto_inteligente;

/

  GRANT EXECUTE ON "SYSTEM"."PKG_VOTO_INTELIGENTE" TO PUBLIC;
