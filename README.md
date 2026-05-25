# Corpus de Traducción Mixteco-Español

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue" alt="Python">
  <img src="https://img.shields.io/badge/uv-package%20manager-purple" alt="uv">
  <img src="https://img.shields.io/badge/DVC-data%20versioning-orange" alt="DVC">
  <img src="https://img.shields.io/badge/Ruff-linting%20%26%20formatting-red" alt="Ruff">
  <img src="https://img.shields.io/badge/Pytest-testing-green" alt="Pytest">
  <img src="https://img.shields.io/badge/Pre--commit-enabled-yellow" alt="Pre-commit">
  <img src="https://img.shields.io/badge/License-Apache%202.0-lightgrey" alt="License">
</p>

## Descripción

Este repositorio tiene como objetivo construir un corpus paralelo para traducción automática entre Mixteco y Español.

El proyecto se inspira en la iniciativa de traducción Rapanui-Español desarrollada en el contexto de CENIA, con el propósito de explorar la expansión de este tipo de esfuerzos hacia lenguas indígenas de México.

Actualmente, el proyecto se encuentra en una fase inicial de diseño, recopilación, organización y validación de datos lingüísticos.

## Instituciones colaboradoras

- CENIA
- INPI

## Objetivo del proyecto

Construir un conjunto de datos lingüístico, documentado y versionado que permita:

- recopilar frases en español;
- facilitar su traducción humana al mixteco;
- organizar variantes lingüísticas de forma trazable;
- preparar datos para futuros modelos de traducción automática;
- apoyar procesos de preservación, documentación y tecnología lingüística.

## Estado del proyecto

Fase actual:

```text
Exploración y construcción inicial del corpus
````

Actividades principales:

* definición de estructura del repositorio;
* configuración de herramientas de desarrollo;
* preparación de datos base desde FLORES-200;
* diseño de plantillas para traducción humana;
* exploración de fuentes externas como CMU Wilderness.

## Estructura del repositorio

```text
mixteco-espanol-traductor/
├── data/
├── docs/
├── notebooks/
├── src/
│   └── mixteco_espanol_traductor/
├── tests/
├── README.md
├── pyproject.toml
├── uv.lock
└── .pre-commit-config.yaml
```

## Herramientas principales

| Herramienta | Uso                               |
| ----------- | --------------------------------- |
| Python      | Desarrollo principal              |
| uv          | Gestión de dependencias           |
| DVC         | Versionamiento de datos           |
| Ruff        | Linting y formato                 |
| Pytest      | Pruebas automatizadas             |
| Pre-commit  | Validaciones antes de cada commit |

## Flujo de trabajo

El proyecto seguirá una organización basada en ramas:

```text
main      → versión estable
dev       → integración principal
feature/* → desarrollo de nuevas tareas
```

Los commits seguirán el formato:

```text
tipo(scope): descripción
```

Ejemplo:

```text
docs(readme): agregar descripción inicial del proyecto
```

## Licencia

Este proyecto se distribuirá bajo la licencia Apache 2.0.
