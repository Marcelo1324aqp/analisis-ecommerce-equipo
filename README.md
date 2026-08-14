\# Análisis de Comportamiento en E-commerce



Laboratorio de análisis de clickstream de una tienda de ropa online (dataset 2008),

desarrollado simulando un flujo de trabajo colaborativo con Git y GitHub.



\## Integrantes y funciones desarrolladas



| Rol              | Integrante      | Funciones implementadas                                                                 |

|-------------------|-----------------|-------------------------------------------------------------------------------------------|

| Lead              | Marcelo Torres  | `cargar\_datos`, integración final de `main.py`                                            |

| Data Architect    | Marcelo Torres  | `get\_country\_name`, `clean\_currency\_data`, `segment\_by\_period`                            |

| Backend Developer | Marcelo Torres  | `calculate\_conversion\_rate`, `analyze\_price\_elasticity`, `identify\_session\_depth`, `color\_popularity\_by\_category` |

| BI Analyst        | Marcelo Torres  | `sales\_funnel\_analysis`, `price\_impact\_by\_location`, `conversion\_by\_photography\_type`     |

| QA Engineer       | Marcelo Torres  | `validate\_page\_flow`, `check\_location\_distribution`, `verify\_model\_photography`           |



> Nota: este proyecto fue desarrollado individualmente, simulando cada rol del equipo

> mediante ramas independientes (`arch-Torres`, `back-Torres`, `bi-Torres`, `qa-Torres`,

> `lead-Torres`) integradas a `main` mediante Pull Requests, para practicar el flujo de

> trabajo colaborativo de Git/GitHub de principio a fin.



\## Problemas encontrados



\- Los nombres de columnas del CSV vienen en minúsculas, pero el código de referencia

&nbsp; esperaba mayúsculas. Se resolvió estandarizando a mayúsculas dentro de `cargar\_datos`.

\- El nombre del archivo CSV debía coincidir exactamente (`e-shop clothing 2008.csv`, con

&nbsp; espacios) con lo esperado por el código.



\## Cómo ejecutar



```powershell

conda activate datalab

python .\\main.py

```

