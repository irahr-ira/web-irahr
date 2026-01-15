# Directiva: Landing Page IRAHR

## 1. Objetivo
Construir una Landing Page de alta conversión para "IRAHR" (Agencia de Automatización de RRHH).
Objetivo principal: Conseguir agendamientos para "Auditoría de Automatización Gratuita".

## 2. Entradas
- **Nombre:** IRAHR
- **Paleta de Colores:**
    - Fondo: `#000000` (Negro Puro), `#111111` (Gris Oscuro)
    - Texto: `#FFFFFF` (Blanco)
    - Acento Primario: `#00E5FF` (Cyan Eléctrico / Tecnológico)
    - Acento Secundario: `#C0C0C0` (Plata / Metálico)
- **Tipografía:** Sans-serif moderna (Inter, Roboto, o similar).
- **Vibe:** Cyberpunk minimalista, serio, corporativo pero futurista.

## 3. Estructura del Sitio (Single Page)

### A. Header / Hero Section
- **H1:** "Automatiza tu proceso de selección y contrata talento top en tiempo récord."
- **Subtítulo:** "Ayudamos a PyMEs a filtrar candidatos y agendar entrevistas en piloto automático con IA. Deja de leer CVs, empieza a entrevistar."
- **CTA:** "Solicitar Auditoría Gratuita" (Botón con alto contraste, ej. Cyan con texto negro o borde brillante).
- **Visual:** Logo proporcionado por usuario (Imagen contiene texto "IRAHR"). No duplicar texto en HTML. Ajustar altura.
- **Barra de Integraciones:** Justo debajo del Hero. "Integramos las mejores tecnologías en tu flujo de trabajo". Logos (escala de grises): Make, ChatGPT, Calendly, LinkedIn, Slack.
- **Interactividad:** Efecto "Glow" (Resplandor Cyan/Blanco) al pasar el cursor (Hover) sobre Tarjetas y Pasos.

### B. Problem Section (Dolores)
- Tarjetas con **ICONOS LINEALES MINIMALISTAS** (SVG Wireframe, blanco o cian). NO Emojis.
    1. "Sobrecarga de CVs irrelevantes"
    2. "Lentitud en respuestas = Pérdida de talento"
    3. "Equipo de RRHH saturado con admin"

### C. Solution Section (Cómo funciona)
- Pasos 1, 2, 3:
    1. **Captura:** Centralización.
    2. **Filtro IA:** Validación automática.
    3. **Agenda:** Agendamiento automático.

### D. Benefits Section
- Ahorro de +20h/semana.
- Disponibilidad 24/7.
- Sin sesgos humanos iniciales.

### E. FAQ Section
- Título: "¿Dudas sobre automatizar tu reclutamiento?"
- Formato: Acordeón (Desplegable).
- Preguntas: IA reemplaza humanos (No), Difícil implementación (No), Pocos CVs (Sirve), RGPD (Cumple).

### F. Contact Section (Formulario)
- **Título:** "Solicitar Auditoría" o "¿Listo para recuperar tus 20 horas semanales?"
- **Funcionalidad:** FormSubmit.
    - Action: `https://formsubmit.co/irazabalbeitia@irarh.com`
    - Method: POST
- **Campos:**
    1. Nombre completo (Required)
    2. Email corporativo (Required, type="email")
    3. Empresa (Opcional)
    4. Mensaje/Desafío (Textarea)
    5. Hidden: `_next` (Redirección a home o thank you), `_subject` ("Nuevo Lead desde Web IRAHR").
- **Botón:** "Enviar Solicitud y Agendar".
- **Estilo:** Inputs oscuros (#111), borde fino, focus Cyan Eléctrico.

### G. Footer
- "IRAHR - Inteligencia aplicada al Capital Humano".
- Links de contacto.
- **Legales:** Aviso Legal, Política de Privacidad (Debe enlazar a página dedicada).

### G. Privacy Policy Page (privacy.html)
- **Título:** Política de Privacidad - IRAHR
- **Estilo:** Mismo "Dark Mode" que la landing principal.
- **Contenido:**
    1. Responsable: IRAHR (info@irahr.com).
    2. Finalidad: Gestionar auditoría y comunicaciones.
    3. Legitimación: Consentimiento.
    4. Destinatarios: No cesión salvo obligación/proveedores seguros.
    5. Derechos: Acceso, rectificación, supresión en info@irahr.com.
    6. Aviso Legal:
        - **Propiedad Intelectual:** Contenido propiedad exclusiva de IRAHR. Prohibida reproducción sin autorización.
        - **Responsabilidad:** No responsabilidad por uso indebido o errores por navegadores desactualizados.
- **Navegación:** Botón para "Volver al Inicio".

## 4. Requisitos Técnicos
- **Stack:** HTML5, CSS3 (Vanilla), JS (Vanilla).
- **Archivos:**
    - `index.html`: Landing Page.
    - `privacy.html`: Página de Políticas.
    - `style.css`: Estilos compartidos.

    - `script.js`: Interacciones simples (scroll suave, validación simple si hay form).
- **SEO:**
    - Meta Title: "IRAHR | Automatización de Reclutamiento y Selección con IA"
    - Meta Description: "Agencia de automatización de RRHH para PyMEs. Filtra candidatos, agenda entrevistas y ahorra costes con Inteligencia Artificial. Auditoría gratuita disponible."
    - Open Graph tags básicos.

## 5. Restricciones y Advertencias
- **Accesibilidad:** Asegurar contraste suficiente entre texto y fondo.
- **Performance:** Imágenes optimizadas (WebP).
- **Responsive:** Debe verse perfecto en móvil (Columnas se apilan).
