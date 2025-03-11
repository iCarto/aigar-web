---
hide:
  - navigation
  - toc
---

# Descargas

### AIGAR-Lecturas

Sigue estos pasos para instalar la aplicación AIGAR-Lecturas en tu celular.

<ol>
  <li>
    <h4>Descargar la aplicación</h4>
    <a href="https://github.com/iCarto/aigar-web/releases/download/250303/250303_aigar-lecturas.apk" class="downloads__link">
      <span class="material-symbols-outlined">download_for_offline</span> AIGAR-Lecturas v250303
    </a>
    <p>
      <strong>¿Qué es este archivo?</strong><br>
      Es un archivo APK que contiene la aplicación AIGAR-Lecturas. El código <code>aammdd</code> en el nombre indica la fecha de la versión. Por ejemplo, <code>250303_aigar-lecturas.apk</code> corresponde a la versión del 3 de marzo de 2025.
    </p>
  </li>

  <li>
    <h4>Copiar el archivo al teléfono</h4>
    <p>
      Copia el archivo <code>aigar-lecturas.apk</code> descargado en tu celular, ya sea mediante cable USB o usando una aplicación de transferencia de archivos.
    </p>
  </li>

  <li>
    <h4>Instalar la aplicación</h4>
    <p>
      Una vez copiado el archivo en tu celular, abre el archivo <code>aigar-lecturas.apk</code> para iniciar la instalación. Sigue las instrucciones en pantalla para completar el proceso.
    </p>
  </li>
</ol>

!!! info "Requisitos tecnológicos"

      - [ ] Smartphone con Android 11.0 o superior (la cantidad dependerá de las personas realicen la revisión de consumos)
      - [ ] Cualquier marca con antigüedad de fabricación menor a 5 años

### AIGAR-Escritorio

Sigue estos pasos para descargar e instalar la aplicación AIGAR en tu ordenador.

<ol>
  <li>
    <h4>Descargar la aplicación</h4>
    <a href="https://github.com/iCarto/aigar-web/releases/download/250303/250303_aigar.zip" class="downloads__link"><span class="material-symbols-outlined">download_for_offline</span> AIGAR-Escritorio v250303</a>
    <p>
      <strong>¿Qué contiene?</strong><br>
      Es un archivo comprimido (<code>aammdd_AIGAR.zip</code>) que contiene la aplicación.
      El código <code>aammdd</code> en el nombre indica la fecha de la versión.
      Por ejemplo, <code>250303_AIGAR.zip</code> corresponde a la versión del 3 de marzo de 2025.
    </p>
    <p>
      <strong>Cómo instalar</strong><br>
      1. Descarga el archivo <code>.zip</code> y descomprímelo en <code>C:\</code>.<br>
      2. Para facilitar el acceso, crea un acceso directo del archivo <code>AIGAR.exe</code> y muévelo al escritorio.
    </p>
  </li>

  <li>
    <h4>Descargar la base de datos</h4>

    <h5>Opción 1: Base de datos vacía</h5>

<a href="https://github.com/iCarto/aigar-web/releases/download/250303/aigar_data_vacia.zip" class="downloads__link"><span class="material-symbols-outlined">download_for_offline</span> Descargar base de datos vacía</a>

<p>
<strong>¿Qué contiene?</strong><br> - Una base de datos vacía, pero con la estructura lista para configurar los datos de cada Junta de Agua.<br> - Debe descomprimirse en la carpeta <strong>Mis Documentos</strong>, por ejemplo:
<code>C:\Usuarios\&lt;MiUsuario&gt;\Mis Documentos\aigar_data</code>.
</p>
<p><strong>Archivos incluidos:</strong></p>
<ul>
<li><strong>db.sqlite3</strong> → Base de datos principal. Para copias de seguridad, copiar este archivo a un USB u otro almacenamiento externo.</li>
<li><strong>plantilla_recibo.docx</strong> → Plantilla para imprimir recibos. Puede modificarse si se conoce su sintaxis.</li>
<li><strong>logo.png</strong> → Logo del SAPS para los recibos. Se debe reemplazar con el logo de la Junta de Agua, manteniendo el formato <code>.png</code> y tamaño <strong>191x191 px</strong>.</li>
</ul>

    <h5>Opción 2: Base de datos de ejemplo</h5>

<a href="https://github.com/iCarto/aigar-web/releases/download/250303/aigar_data_ejemplo.zip" class="downloads__link"><span class="material-symbols-outlined">download_for_offline</span> Descargar base de datos ficticia</a>

<p>
<strong>¿Qué contiene?</strong><br> - Un ejemplo pre-cargado de una Junta de Agua ficticia, útil para pruebas y exploración de la aplicación.
</p>

  </li>

  <li>
    <h4>Ejecutar la aplicación</h4>
    <ol>
    <li>Haz doble clic en <code>AIGAR.exe</code> dentro de la carpeta donde descomprimiste la aplicación.</li></ol>
  </li>
</ol>

!!! info "Requisitos tecnológicos"

      - [ ] 1 computadora de escritorio o laptop
      - [ ] Sistema operativo Windows 7 o superior (64 bits)
      - [ ] 300MB de espacio libre en disco
      - [ ] 4GB de RAM mínimo

!!! warning "Esta aplicación está diseñada para apoyar la gestión organizativa y administrativa de las Juntas de Agua. Antes de implementarla, se recomienda trabajar con la Junta de Agua para revisar los procesos administrativos y el reglamento y actualizar el catastro de personas socias. Para más detalles, consulta la <a href="methodology.md">metodología</a> y [contacta](contact.md) con ASAPS para definir el proceso de implantación de AIGAR en tu Junta de Agua."

## Requisitos del Sistema de Agua

### Infraestructura Técnica

- [ ] Medidores de caudal (contadores) para registro preciso del consumo.

### Requisitos de Gestión

!!! note "Los siguientes requisitos pueden desarrollarse progresivamente durante la implantación."

#### Administración

- [ ] Procesos establecidos de gestión administrativa
- [ ] Personal operativo y administrativo contratado
- [ ] Oficina del sistema establecida

#### Finanzas

- [ ] Tarifas adecuadas y niveles de morosidad controlados
- [ ] Cuenta bancaria activa para facilitar pagos y transacciones seguras

#### Registro y Control

- [ ] Catastro único y actualizado de usuarios
- [ ] Herramientas de gestión administrativa

## Documentación y código

Además de la aplicación y los datos de prueba, existe numerosa documentación de apoyo para implantar AIGAR:

- [Repositorio de Github de AIGAR-Lecturas](https://github.com/iCarto/aigar-lecturas)
- [Repositorio de Github de AIGAR-Escritorio](https://github.com/iCarto/aigar)
<!-- - [Manual de usuario de AIGAR (Pendiente)]()
- [Video manual de AIGAR-Lecturas (Pendiente)]()
- [Video manual de AIGAR-Escritorio (Pendiente)]() -->
