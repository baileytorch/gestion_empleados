USE gestion_empleados;

CREATE TABLE IF NOT EXISTS tipos_empleado (
    id_tipo_empleado INT NOT NULL AUTO_INCREMENT,
    tipo_empleado VARCHAR(50) NOT NULL,
    descripcion_tipo_empleado VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    PRIMARY KEY (id_tipo_empleado));

CREATE TABLE IF NOT EXISTS modulos (
    id_modulo INT NOT NULL AUTO_INCREMENT,
    codigo_modulo VARCHAR(25) NOT NULL,
    nombre_modulo VARCHAR(50) NOT NULL,
    descripcion_modulo VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    PRIMARY KEY (id_modulo));

CREATE TABLE IF NOT EXISTS roles (
    id_rol INT NOT NULL AUTO_INCREMENT,
    rol VARCHAR(50) NOT NULL,
    descripcion_rol VARCHAR(255) NOT NULL,
    permisos_rol VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    PRIMARY KEY (id_rol));

CREATE TABLE IF NOT EXISTS paises (
    codigo_pais INT NOT NULL,
    codigo_iso3_pais VARCHAR(3) NULL,
    nombre_pais VARCHAR(50) NOT NULL,
    gentilicio_pais VARCHAR(50) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    PRIMARY KEY (codigo_pais));

CREATE TABLE IF NOT EXISTS empleados (
    id_empleado INT NOT NULL AUTO_INCREMENT,
    rut_empleado VARCHAR(10) NOT NULL,
    nombre_empleado VARCHAR(255) NOT NULL,
    fecha_contrato DATE NOT NULL,
    salario_empleado FLOAT NULL,
    correo_empleado VARCHAR(255) NULL,
    telefono_empleado VARCHAR(12) NULL,
    direccion_empleado VARCHAR(255) NULL,
    fecha_nacimiento_empleado DATE NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    id_tipo_empleado INT NOT NULL,
    id_rol INT NOT NULL,
    codigo_pais INT NULL,
    PRIMARY KEY (id_empleado),
    CONSTRAINT fk_tipo_empleado FOREIGN KEY (id_tipo_empleado) REFERENCES tipos_empleado(id_tipo_empleado),
    CONSTRAINT fk_rol_empleado FOREIGN KEY (id_rol) REFERENCES roles(id_rol),
    CONSTRAINT fk_pais_empleado FOREIGN KEY (codigo_pais) REFERENCES paises(codigo_pais));

CREATE TABLE IF NOT EXISTS log_db (
    id_log INT NOT NULL AUTO_INCREMENT,
    fecha_log DATETIME NOT NULL,
    accion_log VARCHAR(25) NOT NULL,
    tabla_log VARCHAR(50) NOT NULL,
    comentario_log VARCHAR(25) NOT NULL,
    id_empleado INT NOT NULL,
    PRIMARY KEY (id_log),
    CONSTRAINT fk_empleado_log FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado));

CREATE TABLE IF NOT EXISTS departamentos (
    id_departamento INT NOT NULL AUTO_INCREMENT,
    nombre_departamento VARCHAR(50) NULL,
    descripcion_departamento VARCHAR(255) NULL,
    id_empleado INT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    PRIMARY KEY (id_departamento),
    CONSTRAINT fk_gerente_departamento FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado));

CREATE TABLE IF NOT EXISTS empleados_departamento (
    id_empleado_departamento INT NOT NULL AUTO_INCREMENT,
    id_empleado INT NOT NULL,
    id_departamento INT NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    PRIMARY KEY (id_empleado_departamento),
    CONSTRAINT fk_empleado_departamento FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado),
    CONSTRAINT fk_departamento_empleado FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento));

CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT NOT NULL AUTO_INCREMENT,
    rut_cliente VARCHAR(10) NULL,
    razon_social VARCHAR(255) NOT NULL,
    correo_contacto VARCHAR(255) NULL,
    telefono_contacto VARCHAR(12) NULL,
    direccion_cliente VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    codigo_pais INT NULL,
    PRIMARY KEY (id_cliente),
    CONSTRAINT fk_pais_cliente FOREIGN KEY (codigo_pais) REFERENCES paises(codigo_pais));

CREATE TABLE IF NOT EXISTS proyectos (
    id_proyecto INT NOT NULL AUTO_INCREMENT,
    nombre_proyecto VARCHAR(50) NULL,
    descripcion_proyecto VARCHAR(255) NULL,
    fecha_inicio_proyecto DATE NOT NULL,
    fecha_fin_proyecto DATE NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    id_cliente INT NOT NULL,
    id_departamento INT NOT NULL,
    PRIMARY KEY (id_proyecto),
    CONSTRAINT fk_cliente_proyecto FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
    CONSTRAINT fk_departamento_proyecto FOREIGN KEY (id_departamento) REFERENCES departamentos(id_departamento));

CREATE TABLE IF NOT EXISTS documentos_proyecto (
    id_documento_proyecto INT NOT NULL AUTO_INCREMENT,
    nombre_documento VARCHAR(255) NOT NULL,
    ubicacion_documento VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    id_proyecto INT NOT NULL,
    PRIMARY KEY (id_documento_proyecto),
    CONSTRAINT fk_documento_proyecto FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto));

CREATE TABLE IF NOT EXISTS empleados_proyecto (
    id_empleado_proyecto INT NOT NULL AUTO_INCREMENT,
    id_empleado INT NOT NULL,
    id_proyecto INT NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    PRIMARY KEY (id_empleado_proyecto),
    CONSTRAINT fk_empleado_proyecto FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado),
    CONSTRAINT fk_proyecto_empleado FOREIGN KEY (id_proyecto) REFERENCES proyectos(id_proyecto));

CREATE TABLE IF NOT EXISTS registros_tiempo (
    id_registro_tiempo INT NOT NULL AUTO_INCREMENT,
    fecha_registro DATE NOT NULL,
    tiempo_trabajado FLOAT NOT NULL,
    tareas_realizadas VARCHAR(255) NOT NULL,
    observaciones VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    id_empleado_proyecto INT NOT NULL,
    PRIMARY KEY (id_registro_tiempo),
    CONSTRAINT fk_asignacion_empleado_proyecto FOREIGN KEY (id_empleado_proyecto) REFERENCES empleados_proyecto(id_empleado_proyecto));

CREATE TABLE IF NOT EXISTS tipos_informe (
    id_tipo_informe INT NOT NULL AUTO_INCREMENT,
    tipo_informe VARCHAR(50) NOT NULL,
    descripcion_tipo_informe VARCHAR(255) NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    PRIMARY KEY (id_tipo_informe));

CREATE TABLE IF NOT EXISTS informe (
    id_informe INT NOT NULL AUTO_INCREMENT,
    fecha_creacion DATE NOT NULL,
    ubicacion_informe VARCHAR(255) NOT NULL,
    habilitado TINYINT NOT NULL DEFAULT 1,
    id_tipo_informe INT NOT NULL,
    id_empleado INT NOT NULL,
    PRIMARY KEY (id_informe),
    CONSTRAINT fk_tipo_informe FOREIGN KEY (id_tipo_informe) REFERENCES tipos_informe(id_tipo_informe),
    CONSTRAINT fk_empleado_informe FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado));