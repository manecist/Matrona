# María Cisterna · Matrona ✦

![María Cisterna · Matrona](assets/logo_maria_cisterna_noche.png)

**María Cisterna Escobar · Matrona** — Salud sexual y reproductiva · Registro Superintendencia de Salud N° 561993

Portafolio de salud sexual y reproductiva y **análisis de datos**: páginas educativas interactivas, una cápsula Chile Crece Contigo con videos animados, un torpedo profesional de hormonas y métodos, tableros en Power BI y Tableau (en repositorios aparte), y una planilla de registro PAP con datos ficticios.

> **Portafolio en línea:** `https://manecist.github.io/Matrona/` (GitHub Pages)


## 📂 Qué contiene

| Carpeta | Contenido |
|---|---|
| `index.html` | **Portada del portafolio**: cielo nocturno con las cuatro guardianas, filtros por tema y acceso a todo lo demás. |
| `tesis.html` | **Mi tesis visual**: «La sexualidad no se jubila» (USS Concepción, 2017), respuestas por persona, citas, nube de palabras y quiz. |
| `capsula.html` + `capsula/` | **Cápsula Chile Crece Contigo** que creé como matrona, con todo el camino en 7 etapas: **embarazo** (controles, ecografías y exámenes por trimestre con su porqué, 23 patologías con riesgos para la mamá y la guagua, gemelares, alto riesgo obstétrico, GES, cuidados, derechos laborales y leyes: IVE, Dominga, Mila, lactancia), **parto** (bolso, bono PAD, contador y simulador de contracciones con curva), **recién nacido** (vacunas y tamizajes, ajuar, control díada de la cabeza a los pies, 17 reflejos, ictericia por zonas de Kramer, cuidados y alarmas), **tu recuperación** (puntos, cesárea, pezones, cuarentena, alarmas), **lactancia** (registro de mamadas, conservación de la leche, qué la aumenta, cuándo no dar pecho), **posparto** (todos los métodos de Chile según semanas y lactancia, aviso legal para adolescentes) y **controles y vacunas**. Valores normales interactivos y fuentes MINSAL, Manual UC 2025 y OMS. |
| `historia-cancer.html` | **Cáncer en Chile y el mundo**: mama, cuello uterino, endometrio, ovario, testículo y próstata (GLOBOCAN 2024), Chile frente al mundo, sobrevida por etapa, simulador de pesquisa, relación con VPH e ITS y calendario de controles. |
| `historia-its.html` · `historia-matronas.html` | **Historias de datos** interactivas sobre ITS en Chile y sobre embarazo no planificado y matronería. |
| `torpedo.html` | **Torpedo profesional**: ficha por marca comercial, hormonas, ventana fértil, edad gestacional y fecha probable de parto, «¿Puedo usarlo?» (CDC 2024/OMS), cáncer y seguridad, mitos vs. evidencia. |
| `guia-anticonceptivos.html` | **Guía interactiva de anticonceptivos**: buscador por marca u hormona, filtros (sin estrógeno, larga duración, sin hormonas, red pública) y ficha de cada método con eficacia, ventajas, desventajas, riesgos, cuándo conviene, cuándo no usar y marcas equivalentes. |
| `guia-anticonceptivos/` | Infografía de equivalencias de anticonceptivos en una hoja y guía de 29 láminas (PDF): ficha ilustrada de los 20 métodos (incluye implante de 3 y 5 años, condón femenino, diafragma, espermicidas, MELA, calendario, coito interrumpido, esterilización femenina y vasectomía) y todas las marcas que se venden en Chile, alerta de riesgo en los que tienen estrógeno y terapia hormonal de la menopausia. |
| `capsula/videos/` | **Ocho cápsulas animadas en video** (versión cinemática, con su portada en `capsula/videos/portadas/`), narradas por mí y visibles en la sección «Mis cápsulas en video» de `capsula.html`: cómo guardar la leche materna, masaje Shantala, sacar chanchitos, sueño seguro, cuándo ir a la maternidad, qué es el PAP, píldora del día después y mitos de la lactancia. |
| `planilla-pap/` | Planilla Excel con macros para registro y seguimiento de PAP, **con datos 100 % ficticios** (nombres, fechas, resultados, centros y profesionales). |
| `datos/` | Script en Python que genera las fichas por marca (la base de datos está en el repositorio `dashboard-anticonceptivos-chile`). |

Las imágenes de las páginas están en `assets/`.

## 📊 Tableros (cada uno en su propio repositorio)

| Repositorio | Contenido |
|---|---|
| `dashboard-anticonceptivos-chile` | Power BI y Tableau: eficacia, seguridad, «Mi pastilla» con más de 140 marcas, ¿puedo usarlo?, interacciones. |
| `dashboard-its-chile` | Power BI y Tableau: sífilis, gonorrea y VIH en Chile y el mundo, guía de cada ITS. |
| `dashboard-embarazo-matronas-chile` | Power BI y Tableau: embarazo adolescente, matronería, mortalidad materna y neonatal, propuestas. |
| `dashboard-ajuar-chile-crece-contigo` | Power BI y Tableau: entregas, cobertura, presupuesto y cadena logística del ajuar (PARN). |
| `dashboard-cancer-chile` | Power BI: cuánto aumenta el cáncer en Chile, cuál predomina, cómo prevenirlo y detectarlo a tiempo. |

Cada repositorio trae el `.pbix`, el proyecto editable de Power BI, el `.twbx` de Tableau, la base de datos `.xlsx` y la lista de fuentes.

## ✍️ Autoría

- **Contenido clínico, análisis, revisión y diseño de la planilla PAP:** María Cisterna Escobar, matrona (Universidad San Sebastián, 2018).
- **Tableros, bases de datos, diseño y programación:** María Cisterna Escobar.
- **Personajes, ilustraciones y logo:** María Cisterna Escobar (Luna Matrona: Marea, Brote, Lumen y Nido).

## 🔒 Privacidad

La planilla PAP es una copia demostrativa: nombres, identificadores, fechas de nacimiento, fechas de examen, resultados, centros de salud y profesionales son ficticios y solo muestran cómo funciona la planilla. No contiene datos de pacientes reales ni de instituciones.

## 🔎 Sobre los datos

- Todas las cifras de los tableros vienen de fuentes públicas citadas en cada uno (MINSAL, ISP, INE, DIPRES, Cenabast, OPS/OMS, ONUSIDA, ECDC, UNFPA, CDC y estudios científicos).
- Las cifras 2025 de ITS se tomaron de reportes de prensa que citan los informes MINSAL e ISP 2025; se recomienda contrastarlas con los documentos oficiales.
- Hay años sin dato público: no se inventaron cifras.
- Las proyecciones internacionales (Lancet, UNFPA) son modelos, no mediciones en Chile.

## ⚠️ Aviso

Material educativo. No reemplaza la consejería ni el control con un profesional de salud.

## ©️ Derechos

© 2026 María Cisterna Escobar, matrona · Registro Superintendencia de Salud N° 561993. **Todos los derechos reservados.** Puedes ver y compartir el enlace; no está permitido copiar, reproducir ni reutilizar el código, las ilustraciones, los personajes ni los textos sin autorización escrita. Ver [LICENSE](LICENSE).
