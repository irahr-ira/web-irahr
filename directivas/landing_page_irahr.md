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
- **Visual:** Logo proporcionado ('irahr_logo_new.png'). **Altura limitada a 45px**. Si tiene fondo blanco, usar `mix-blend-mode: multiply`. Añadir **FAVICON**.
- **Barra de Stack Tecnológico:** Justo debajo del Hero. Franja gris muy oscura. Texto: "POTENCIADO POR LA MEJOR TECNOLOGÍA:". Logos/Texto: OpenAI, Make, LinkedIn, Google Workspace.
- **Navegación (Navbar):** Superior fija o semi-transparente (backdrop-filter: blur). Logo izquierda. Enlaces derecha: "Soluciones", "Beneficios", "Contacto".
- **Animaciones:** "Scroll Reveal" (AOS) fade-up en secciones principales.

### B. Problem Section (Dolores)
- Tarjetas con **ICONOS LINEALES MINIMALISTAS** (SVG Wireframe, blanco o cian). NO Emojis.
    1. "Sobrecarga de CVs irrelevantes"
    2. "Lentitud en respuestas = Pérdida de talento"
    3. "Equipo de RRHH saturado con admin"
- **Animación:** Fade-up al hacer scroll.

### C. Solution Section (Cómo funciona)
- Pasos 1, 2, 3:
    1. **Captura:** Centralización.
    2. **Filtro IA:** Validación automática.
    3. **Agenda:** Agendamiento automático.
- **Animación:** Fade-up al hacer scroll.

### D. Benefits Section
- Ahorro de +20h/semana.
- Disponibilidad 24/7.
- Sin sesgos humanos iniciales.
- **Estilo:** Resaltar en **Negrita y Blanco** la parte impactante.
- **Animación:** Fade-up al hacer scroll.

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
- **Botón:** "Enviar Solicitud y Agendar". Ancho limitado (max 450px), centrado.
- **Estilo:** Inputs oscuros (#111), borde fino, focus Cyan Eléctrico. Placeholder gris claro (#AAA) para legibilidad.

### G. Footer
- "IRARH - Inteligencia aplicada al Capital Humano".
- Links de contacto.
- **Legales:** Aviso Legal, Política de Privacidad (Debe enlazar a página dedicada).

### H. Privacy Policy Page (privacy.html)
- **Título:** Política de Privacidad - IRARH
- **Estilo:** Mismo "Dark Mode" que la landing principal.
- **Contenido:** Responsable, Finalidad, Legitimación, Destinatarios, Derechos.

### I. Legal Notice Page (legal.html)
- **Título:** Aviso Legal - IRARH
- **Estilo:** Mismo "Dark Mode".
- **Contenido:** LSSI (Datos identificativos, Propiedad Intelectual, Exclusión de Garantías).

### J. Cookie Banner
- **Posición:** Fixed bottom.
- **Estilo:** Dark mode.
- **Funcionalidad:** Botones "Aceptar" y "Solo Necesarias". Guardar preferencia en localStorage.

### K. Success Page (success.html)
- **Título:** "¡Solicitud Recibida!"
- **Mensaje:** "Hemos recibido tus datos. Te contactaremos en menos de 24h para tu auditoría."
- **Visual:** Icono de Check grande (Verde/Cian).
- **Acción:** Botón "Volver al Inicio".
- **Estilo:** Mismo Dark Mode.

## 4. Requisitos Técnicos
- **Stack:** HTML5, CSS3 (Vanilla), JS (Vanilla).
- **Archivos:**
    - `index.html`: Landing Page.
    - `privacy.html`: Página de Políticas.
    - `legal.html`: Aviso Legal.
    - `success.html`: Página de Agradecimiento.
    - `style.css`: Estilos compartidos.
    - `script.js`: Interacciones simples (scroll suave, validación simple si hay form, cookies).
- **SEO:**
    - Meta Title: "IRARH | Agencia de Automatización de Reclutamiento con IA"
    - Meta Description: "Automatiza tu selección de personal con Inteligencia Artificial. Filtra candidatos, agenda entrevistas y ahorra +20h semanales. Tu socio tecnológico en RRHH."
    - Meta Keywords: "IA recursos humanos, automatización reclutamiento, agencia IA, selección de personal eficiente"
    - Open Graph tags básicos.

## 5. Restricciones y Advertencias
- **Accesibilidad:** Asegurar contraste suficiente entre texto y fondo.
- **Performance:** Imágenes optimizadas (WebP).
- **Responsive:** Debe verse perfecto en móvil (Columnas se apilan).
