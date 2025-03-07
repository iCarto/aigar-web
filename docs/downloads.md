---
hide:
  - navigation
  - toc
---

# Descargas

### AIGAR-Lecturas

[AIGAR-Lecturas](https://github.com/iCarto/aigar-web/releases/download/250303/250303_aigar-lecturas.apk). v250303. Aplicación móvil.

Para instalarlo en el teléfono móvil se seguirán los siguientes pasos:

1. Copiar el archivo **aigar-lecturas.apk** en el teléfono
2. Instalar la app AIGAR-Lecturas

!!! info "Requisitos tecnológicos"

      - [ ] Smartphone con Android 11.0 o superior (la cantidad dependerá de las personas realicen la revisión de consumos)
      - [ ] Cualquier marca con antigüedad de fabricación menor a 5 años

### AIGAR-Escritorio

[AIGAR-Escritorio](https://github.com/iCarto/aigar-web/releases/download/250303/250303_aigar.zip) v250303. Aplicación de escritorio.

Se sumnisitran dos archivos:

<ol>
  <li>
    <strong>aammdd_AIGAR.zip</strong>. 
    <p>Consiste en la aplicación de escritorio donde <code>aammdd</code> es la fecha de la versión. Por ejemplo <code>240126_AIGAR.zip</code> significa que es la versión de AIGAR de fecha 26 de Enero de 2024.</p>
    <p>La aplicación se descomprimirá preferiblemente en <code>C:\</code>. Para facilitar el acceso a la aplicación, se recomienda crear un acceso directo y trasladarlo al escritorio.</p>
  </li>
  <li>
    <strong>aammdd_aigar_data.zip</strong>.
    <p>Contiene la Base de Datos e información configurable para cada Junta de Agua. Se suministra una base de datos vacía con la estructura predefinida y una base de datos de prueba con un ejemplo de una Junta de Agua ficticia.</p>
    <p>Es un directorio que debemos descomprimir en la carpeta Mis Documentos. Por ejemplo en <code>C:\Usuarios\&lt;Mi Usuario&gt;\Mis Documentos\aigar_data</code>. Dentro de esta carpeta estarán los siguientes archivos:</p>
    <ul>
      <li><strong>db.sqlite3</strong>. Es la base de datos de la aplicación. Para hacer copias de seguridad, copie este fichero a USB externo.</li>
      <li><strong>plantilla_recibo.docx</strong>. Es la plantilla usada para imprimir recibos. Puede ser modificada si se conoce bien la sintaxis.</li>
      <li><strong>logo.png</strong>. Es el logo del SAPS que se usará en los recibos impresos. El fichero que se proporciona por defecto debe ser substituido por el real de la Junta de Agua, respetando el tamaño del fichero original: 191 x 191 y el formato .png.</li>
    </ul>
  </li>
</ol>

Se ejecutará la aplicación dando clic al archivo `AIGAR.exe`.

La aplicación es una herremienta asociada a una [metodología](methodology.md) para fortalecer la gestión organizativa y adminsitrativa de las Juntas de Agua. Antes de poder implementarlo se necesitará trabajar conjuntamente con la Junta de Agua para revisar los procesos adminsitrativos, el reglamento y actualizar el catastro de los socios tanto en visitas en campo como online.

!!! warning "Se recomienda [consultar](contact.md) con ASAPS para conocer el proceso de incorporación de AIGAR en tu Junta de Agua."

!!! info "Requisitos tecnológicos"

      - [ ] 1 computadora de escritorio o laptop
      - [ ] Sistema operativo Windows 7 o superior (64 bits)
      - [ ] 300MB de espacio libre en disco
      - [ ] 4GB de RAM mínimo

## Código fuente

El código fuente puede ser descargado desde el (repositorio de GitHub).

## Requisitos del Sistema de Agua

### Infraestructura Técnica

- [ ] Medidores de caudal (contadores) para registro preciso del consumo.

### Requisitos de Gestión

!!! note "Los siguientes requisitos pueden desarrollarse progresivamente durante la implementación."

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

## Documentación

Además de la aplicación y los datos de prueba, existe numerosa documentación de apoyo para implementar la aplicación:

- [Software y datos de prueba]()
- [Manual de usuario de AIGAR (Pendiente)]()
- [Video manual de AIGAR-Lecturas (Pendiente)]()
- [Video manual de AIGAR-Escritorio (Pendiente)]()
