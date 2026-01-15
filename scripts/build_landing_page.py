import os

# Configuration
BASE_DIR = os.getcwd()
DIRECTIVE_PATH = os.path.join(BASE_DIR, 'directivas', 'landing_page_irahr.md')
OUTPUT_DIR = BASE_DIR

# SVG Icons
ICON_EMAIL = """<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>"""
ICON_CLOCK = """<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>"""
ICON_ADMIN = """<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><line x1="10" y1="9" x2="8" y2="9"></line></svg>"""
ICON_CHECK = """<svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>"""

# Content Definitions based on Directive
HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IRARH | Agencia de Automatización de Reclutamiento con IA</title>
    <meta name="description" content="Automatiza tu selección de personal con Inteligencia Artificial. Filtra candidatos, agenda entrevistas y ahorra +20h semanales. Tu socio tecnológico en RRHH.">
    <meta name="keywords" content="IA recursos humanos, automatización reclutamiento, agencia IA, selección de personal eficiente">
    <link rel="icon" type="image/png" href="irahr_logo.png">
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <!-- AOS Animation Library -->
    <link rel="stylesheet" href="https://unpkg.com/aos@next/dist/aos.css" />
</head>
<body>
    <header class="hero">
        <nav class="navbar">
            <div class="logo-container">
                <img src="irahr_logo.png" alt="IRARH Logo" class="logo">
            </div>
            <div class="nav-links">
                <a href="#solution" class="nav-link">Soluciones</a>
                <a href="#benefits" class="nav-link">Beneficios</a>
                <a href="#audit" class="cta-button-small">Contacto</a>
            </div>
        </nav>
        
        <div class="hero-content" data-aos="fade-up">
            <h1>Automatiza tu proceso de selección y contrata talento top en <span class="highlight">tiempo récord</span>.</h1>
            <p class="subtitle">Ayudamos a PyMEs a filtrar candidatos y agendar entrevistas en piloto automático con IA. Deja de leer CVs, empieza a entrevistar.</p>
            <a href="#audit" class="cta-button-main">Solicitar Auditoría Gratuita</a>
        </div>
    </header>

    <section class="tech-stack-bar">
        <div class="section-container">
            <p class="tech-stack-title">Potenciado por la mejor tecnología:</p>
            <div class="tech-logos">
                <span class="tech-logo">OpenAI</span>
                <span class="tech-logo">Make</span>
                <span class="tech-logo">LinkedIn</span>
                <span class="tech-logo">Google Workspace</span>
            </div>
        </div>
    </section>

    <section class="problems" data-aos="fade-up">
        <div class="section-container">
            <h2>¿Te suena familiar?</h2>
            <div class="cards-grid">
                <div class="card">
                    <div class="icon">{ICON_EMAIL}</div>
                    <h3>Sobrecarga de CVs</h3>
                    <p>¿Te ahogas en correos con CVs que no encajan con lo que buscas?</p>
                </div>
                <div class="card">
                    <div class="icon">{ICON_CLOCK}</div>
                    <h3>Procesos Lentos</h3>
                    <p>¿Pierdes talento valioso por tardar demasiado en responder?</p>
                </div>
                <div class="card">
                    <div class="icon">{ICON_ADMIN}</div>
                    <h3>Saturación Admin</h3>
                    <p>¿Tu equipo de RRHH hace trabajo administrativo en lugar de humano?</p>
                </div>
            </div>
        </div>
    </section>

    <section class="solution" id="solution" data-aos="fade-up">
        <div class="section-container">
            <h2>Cómo funciona la magia</h2>
            <div class="steps-container">
                <div class="step">
                    <div class="step-number">01</div>
                    <h3>Captura</h3>
                    <p>Centralizamos todas las postulaciones en un solo lugar inteligente.</p>
                </div>
                <div class="step">
                    <div class="step-number">02</div>
                    <h3>Filtro IA</h3>
                    <p>Nuestra automatización valida si el perfil cumple los requisitos exactos.</p>
                </div>
                <div class="step">
                    <div class="step-number">03</div>
                    <h3>Agenda</h3>
                    <p>Los mejores candidatos agendan entrevista automáticamente en tu calendario.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="benefits" id="benefits" data-aos="fade-up">
        <div class="section-container">
            <h2>Beneficios Inmediatos</h2>
            <ul class="benefits-list">
                <li><span class="check">✓</span> <span><strong>Ahorra +20 horas semanales</strong> por reclutador.</span></li>
                <li><span class="check">✓</span> <span><strong>Experiencia de candidato 24/7</strong> (nunca dejes a nadie sin respuesta).</span></li>
                <li><span class="check">✓</span> <span><strong>Reducción de sesgos humanos</strong> en el primer filtrado.</span></li>
            </ul>
        </div>
    </section>

    <section class="faq" data-aos="fade-up">
        <div class="section-container">
            <h2>¿Dudas sobre automatizar tu reclutamiento?</h2>
            <div class="faq-accordion">
                <details class="faq-item">
                    <summary>¿La IA va a elegir a mis empleados por mí?</summary>
                    <p>No. La IA solo filtra el "ruido". Elimina candidatos que no cumplen los requisitos básicos y agenda las entrevistas. La decisión final y el trato humano siempre son tuyos.</p>
                </details>
                <details class="faq-item">
                    <summary>¿Es difícil de implementar en mi empresa actual?</summary>
                    <p>Para nada. Nosotros configuramos todo "llave en mano". No necesitas equipo técnico ni instalar programas complejos. Nos integramos con lo que ya usas (correo, calendario, Excel).</p>
                </details>
                <details class="faq-item">
                    <summary>¿Sirve si recibo pocos currículums?</summary>
                    <p>Sirve para no perder tiempo. Incluso con pocos candidatos, la automatización asegura una respuesta inmediata, mejorando tu imagen de marca y evitando que el talento se vaya a la competencia por lentitud.</p>
                </details>
                <details class="faq-item">
                    <summary>¿Qué pasa con los datos de los candidatos?</summary>
                    <p>Diseñamos el sistema cumpliendo estrictamente la RGPD. Podemos programar el borrado automático de datos tras el periodo que decidas, algo que hacerlo manual es un riesgo constante.</p>
                </details>
            </div>
        </div>
    </section>

    <section class="contact-form-section" id="audit" data-aos="fade-up">
        <div class="section-container">
            <h2>Solicitar Auditoría</h2>
            <p class="subtitle-cta">¿Listo para recuperar tus 20 horas semanales? La auditoría es gratuita.</p>
            
            <form action="https://formsubmit.co/irazabalbeitia@irarh.com" method="POST" class="audit-form">
                <!-- Hidden Configuration Inputs -->
                <input type="hidden" name="_subject" value="Nuevo Lead desde Web IRAHR">
                <input type="hidden" name="_captcha" value="false">
                <input type="hidden" name="_next" value="https://irarh.com/success.html">
                
                <div class="form-grid">
                    <div class="form-group">
                        <label for="name" class="sr-only">Nombre completo</label>
                        <input type="text" id="name" name="name" placeholder="Nombre completo" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="email" class="sr-only">Email corporativo</label>
                        <input type="email" id="email" name="email" placeholder="Email corporativo" required>
                    </div>
                    
                    <div class="form-group full-width">
                        <label for="company" class="sr-only">Empresa</label>
                        <input type="text" id="company" name="company" placeholder="Empresa (Opcional)">
                    </div>
                    
                    <div class="form-group full-width">
                        <label for="message" class="sr-only">Mensaje</label>
                        <textarea id="message" name="message" placeholder="¿Cuál es tu principal desafío actual?" rows="4"></textarea>
                    </div>
                </div>
                
                <button type="submit" class="cta-button-main width-full">Enviar Solicitud y Agendar</button>
            </form>
        </div>
    </section>

    <footer id="footer">
        <div class="footer-content">
            <h2>IRARH</h2>
            <p>Inteligencia aplicada al Capital Humano</p>
            <a href="mailto:info@irarh.com" class="footer-link">info@irarh.com</a>
            <div class="footer-legal">
                <a href="legal.html" class="legal-link">Aviso Legal</a>
                <span class="separator">|</span>
                <a href="privacy.html" class="legal-link">Política de Privacidad</a>
            </div>
            <p class="copyright">© 2026 IRARH. Todos los derechos reservados.</p>
        </div>
    </footer>

    <!-- Cookie Banner -->
    <div id="cookie-banner" class="cookie-banner" style="display: none;">
        <div class="cookie-content">
            <p>Utilizamos cookies propias y de terceros para mejorar la experiencia. ¿Aceptas?</p>
            <div class="cookie-buttons">
                <button id="accept-cookies" class="cookie-btn accept">Aceptar Cookies</button>
                <button id="necessary-cookies" class="cookie-btn necessary">Solo Necesarias</button>
            </div>
        </div>
    </div>

    <script src="script.js"></script>
    <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
    <script>
      AOS.init({{
        duration: 800,
        once: true,
        offset: 100
      }});
    </script>
</body>
</html>
"""

PRIVACY_CONTENT = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Política de Privacidad - IRARH</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        .legal-content {
            max-width: 800px;
            margin: 4rem auto;
            padding: 2rem;
            text-align: left;
        }
        .legal-content h1 {
            margin-bottom: 2rem;
            color: var(--accent-primary);
        }
        .legal-content h2 {
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-size: 1.2rem;
            color: var(--text-color);
        }
        .legal-content p {
            margin-bottom: 1rem;
            color: #ccc;
        }
        .back-button {
            display: inline-block;
            margin-top: 2rem;
            color: var(--accent-primary);
            text-decoration: none;
            border: 1px solid var(--accent-primary);
            padding: 0.5rem 1.5rem;
            border-radius: 4px;
            transition: all 0.3s;
        }
        .back-button:hover {
            background-color: var(--accent-primary);
            color: var(--bg-color);
        }
    </style>
</head>
<body>
    <header class="hero" style="min-height: 20vh; height: auto;">
        <nav class="navbar">
            <div class="logo-container">
                <a href="index.html">
                    <img src="irahr_logo.png" alt="IRARH Logo" class="logo">
                </a>
            </div>
            <a href="index.html" class="cta-button-small">Volver al Inicio</a>
        </nav>
    </header>

    <main class="legal-content">
        <h1>Política de Privacidad</h1>
        
        <h2>1. Responsable del tratamiento</h2>
        <p>IRARH (info@irahr.com).</p>

        <h2>2. Finalidad</h2>
        <p>Gestionar tu solicitud de auditoría y enviar comunicaciones sobre nuestros servicios. No enviamos SPAM.</p>

        <h2>3. Legitimación</h2>
        <p>Tu consentimiento al rellenar el formulario.</p>

        <h2>4. Destinatarios</h2>
        <p>No se ceden datos a terceros salvo obligación legal o proveedores tecnológicos (encargados de tratamiento) seguros.</p>

        <h2>5. Derechos</h2>
        <p>Puedes acceder, rectificar o suprimir tus datos escribiendo a <a href="mailto:info@irahr.com" style="color: var(--accent-primary);">info@irahr.com</a>.</p>

        <a href="index.html" class="back-button">← Volver a la Home</a>
    </main>

    <footer id="footer">
        <div class="footer-content">
            <p class="copyright">© 2026 IRARH. Todos los derechos reservados.</p>
        </div>
    </footer>
</body>
</html>
"""

LEGAL_CONTENT = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aviso Legal - IRARH</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        .legal-content {
            max-width: 800px;
            margin: 4rem auto;
            padding: 2rem;
            text-align: left;
        }
        .legal-content h1 {
            margin-bottom: 2rem;
            color: var(--accent-primary);
        }
        .legal-content h2 {
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-size: 1.2rem;
            color: var(--text-color);
        }
        .legal-content p, .legal-content li {
            margin-bottom: 1rem;
            color: #ccc;
        }
        .back-button {
            display: inline-block;
            margin-top: 2rem;
            color: var(--accent-primary);
            text-decoration: none;
            border: 1px solid var(--accent-primary);
            padding: 0.5rem 1.5rem;
            border-radius: 4px;
            transition: all 0.3s;
        }
        .back-button:hover {
            background-color: var(--accent-primary);
            color: var(--bg-color);
        }
    </style>
</head>
<body>
    <header class="hero" style="min-height: 20vh; height: auto;">
        <nav class="navbar">
            <div class="logo-container">
                <a href="index.html">
                    <img src="irahr_logo.png" alt="IRARH Logo" class="logo">
                </a>
            </div>
            <a href="index.html" class="cta-button-small">Volver al Inicio</a>
        </nav>
    </header>

    <main class="legal-content">
        <h1>Aviso Legal y Condiciones de Uso</h1>
        
        <h2>1. Datos Identificativos</h2>
        <p>En cumplimiento con el deber de información recogido en la Ley 34/2002, de Servicios de la Sociedad de la Información y del Comercio Electrónico (LSSI), se reflejan los siguientes datos:</p>
        <ul>
            <li><strong>Titular:</strong> IRARH (Pendiente de Razón Social)</li>
            <li><strong>Domicilio:</strong> (Pendiente de Domicilio)</li>
            <li><strong>Email de contacto:</strong> info@irahr.com</li>
        </ul>

        <h2>2. Propiedad Intelectual</h2>
        <p>El contenido de esta web (textos, imágenes, marca IRARH) es propiedad exclusiva y está protegido por la normativa de Propiedad Intelectual e Industrial. Queda prohibida su reproducción total o parcial sin autorización expresa.</p>

        <h2>3. Exclusión de Garantías</h2>
        <p>IRARH no se hace responsable del uso indebido que los usuarios puedan hacer de los contenidos de la web, ni de los posibles errores de seguridad que se puedan producir por usar versiones de navegadores no actualizadas.</p>
        
        <h2>4. Modificaciones</h2>
        <p>IRARH se reserva el derecho de efectuar sin previo aviso las modificaciones que considere oportunas en su portal.</p>

        <a href="index.html" class="back-button">← Volver a la Home</a>
    </main>

    <footer id="footer">
        <div class="footer-content">
            <p class="copyright">© 2026 IRARH. Todos los derechos reservados.</p>
        </div>
    </footer>
</body>
</html>
"""

SUCCESS_CONTENT = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>¡Solicitud Recibida! - IRAHR</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        .success-container {
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 2rem;
        }
        .success-icon {
            width: 100px;
            height: 100px;
            color: var(--accent-primary);
            margin-bottom: 2rem;
            filter: drop-shadow(0 0 15px rgba(0, 229, 255, 0.4));
        }
        .success-title {
            font-size: 3rem;
            margin-bottom: 1rem;
            color: var(--text-color);
        }
        .success-text {
            font-size: 1.25rem;
            color: var(--text-muted);
            margin-bottom: 3rem;
            max-width: 600px;
        }
    </style>
</head>
<body>
    <div class="success-container">
        <div class="success-icon">
            <svg class="icon-svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
        </div>
        <h1 class="success-title">¡Solicitud Recibida!</h1>
        <p class="success-text">Hemos recibido tus datos. Te contactaremos en menos de 24h para tu auditoría.</p>
        <a href="index.html" class="cta-button-main">Volver al Inicio</a>
    </div>
</body>
</html>
"""

CSS_CONTENT = """/* Variables */
:root {
    --bg-color: #000000;
    --bg-secondary: #0a0a0a;
    --text-color: #FFFFFF;
    --text-muted: #888888;
    --accent-primary: #00E5FF;
    --accent-secondary: #C0C0C0;
    --font-main: 'Inter', sans-serif;
    --nav-height: 80px;
}

/* Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    background-color: var(--bg-color);
    color: var(--text-color);
    font-family: var(--font-main);
    line-height: 1.6;
    overflow-x: hidden;
}

/* Typography */
h1, h2, h3 {
    font-weight: 700;
}

.highlight {
    color: var(--accent-primary);
}

/* Layout */
.section-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 4rem 2rem;
    text-align: center;
}

/* Navbar */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: var(--nav-height);
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    z-index: 1000;
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.logo-container {
    display: flex;
    align-items: center;
}

.logo {
    height: 45px;
    width: auto;
    object-fit: contain;
    mix-blend-mode: multiply; /* Helps if logo has white bg, though PNG transparent is best */
}

.nav-links {
    display: none;
}

@media (min-width: 768px) {
    .nav-links {
        display: flex;
        gap: 2rem;
        align-items: center;
    }

    .nav-link {
        color: var(--text-color);
        text-decoration: none;
        font-weight: 500;
        font-size: 0.95rem;
        transition: color 0.3s;
    }

    .nav-link:hover {
        color: var(--accent-primary);
    }
}

/* Header / Hero */
.hero {
    background: linear-gradient(180deg, rgba(0,229,255,0.05) 0%, rgba(0,0,0,1) 100%);
    min-height: 90vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2rem;
    padding-top: calc(var(--nav-height) + 2rem);
    text-align: center;
}

.hero-content {
    max-width: 800px;
}

.hero-content h1 {
    font-size: 3.5rem;
    margin-bottom: 1.5rem;
    line-height: 1.2;
}

.subtitle {
    font-size: 1.25rem;
    color: var(--accent-secondary);
    margin-bottom: 3rem;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

/* Tech Stack Bar */
.tech-stack-bar {
    background-color: #050505; /* Very dark grey */
    border-bottom: 1px solid #1a1a1a;
    padding: 1.5rem 0;
}

.tech-stack-bar .section-container {
    padding: 0.5rem 2rem;
}

.tech-stack-title {
    font-size: 0.8rem;
    color: #555;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 1rem;
    font-weight: 600;
}

.tech-logos {
    display: flex;
    justify-content: center;
    gap: 3rem;
    flex-wrap: wrap;
    align-items: center;
}

.tech-logo {
    font-size: 1.2rem;
    font-weight: 700;
    color: #666; /* Grayscale */
    font-family: inherit;
    transition: color 0.3s;
    user-select: none;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.tech-logo:hover {
    color: #999;
}

/* Buttons */
.cta-button-main {
    display: inline-block;
    background-color: var(--accent-primary);
    color: #000;
    padding: 1rem 2.5rem;
    font-weight: 700;
    text-decoration: none;
    border-radius: 50px;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: transform 0.2s, box-shadow 0.2s;
    cursor: pointer;
    border: none;
    font-size: 1rem;
}

.cta-button-main:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 20px rgba(0, 229, 255, 0.4);
}

.width-full {
    width: 100%;
}

.cta-button-small {
    color: var(--text-color);
    text-decoration: none;
    border: 1px solid var(--accent-secondary);
    padding: 0.5rem 1.5rem;
    border-radius: 4px;
    transition: all 0.3s;
    font-size: 0.9rem;
}

.cta-button-small:hover {
    border-color: var(--accent-primary);
    color: var(--accent-primary);
}

/* Problems Section (Cards) */
.cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
}

.card {
    background-color: var(--bg-secondary);
    padding: 2.5rem 2rem;
    border-radius: 12px;
    border: 1px solid #222;
    transition: all 0.3s ease;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.card:hover {
    transform: translateY(-5px);
    border-color: var(--accent-primary);
    box-shadow: 0 0 15px rgba(0, 229, 255, 0.1);
}

.card .icon {
    width: 64px;
    height: 64px;
    margin-bottom: 1.5rem;
    color: var(--text-color);
    transition: color 0.3s;
}

.card:hover .icon {
    color: var(--accent-primary);
    filter: drop-shadow(0 0 8px var(--accent-primary));
}

.icon-svg {
    width: 100%;
    height: 100%;
}

.card h3 {
    margin-bottom: 1rem;
    color: var(--accent-primary);
    font-size: 1.25rem;
}

/* Solution Steps */
.steps-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2rem;
    margin-top: 3rem;
}

.step {
    flex: 1;
    min-width: 280px;
    text-align: left;
    padding: 2.5rem;
    border-left: 2px solid #333;
    transition: all 0.3s ease;
    background-color: rgba(255,255,255,0.02);
    border-radius: 0 12px 12px 0;
}

.step:hover {
    border-left-color: var(--accent-primary);
    background-color: rgba(255,255,255,0.04);
    box-shadow: 10px 0 20px rgba(0,0,0,0.5);
}

.step-number {
    font-size: 3rem;
    font-weight: 700;
    color: rgba(255, 255, 255, 0.05);
    margin-bottom: 0.5rem;
    line-height: 1;
    transition: color 0.3s;
}

.step:hover .step-number {
    color: rgba(0, 229, 255, 0.2);
}

.step h3 {
    font-size: 1.5rem;
    margin-bottom: 1rem;
}

/* Benefits */
.benefits {
    background-color: #0a0a0a;
}

.benefits-list {
    list-style: none;
    max-width: 700px;
    margin: 3rem auto 0;
    text-align: left;
}

.benefits-list li {
    font-size: 1.3rem;
    margin-bottom: 2rem;
    display: flex;
    align-items: flex-start;
}

.check {
    color: var(--accent-primary);
    margin-right: 1.5rem;
    font-weight: bold;
    font-size: 1.5rem;
    line-height: 1.2;
}

/* FAQ Section */
.faq {
    background-color: var(--bg-color);
}

.faq-accordion {
    max-width: 800px;
    margin: 3rem auto 0;
    text-align: left;
}

.faq-item {
    border-bottom: 1px solid #222;
    margin-bottom: 1rem;
}

.faq-item summary {
    font-size: 1.2rem;
    font-weight: 600;
    padding: 1.5rem 0;
    cursor: pointer;
    list-style: none;
    position: relative;
    padding-right: 2rem;
    transition: color 0.3s;
}

.faq-item summary:hover {
    color: var(--accent-primary);
}

.faq-item summary::-webkit-details-marker {
    display: none;
}

.faq-item summary::after {
    content: '+';
    position: absolute;
    right: 0;
    font-size: 1.5rem;
    font-weight: 300;
    color: var(--accent-primary);
}

.faq-item[open] summary::after {
    content: '-';
}

.faq-item p {
    padding-bottom: 1.5rem;
    color: #ccc;
    font-size: 1rem;
    line-height: 1.6;
}

/* Contact/Form Section */
.contact-form-section {
    padding: 6rem 2rem;
    background: radial-gradient(circle at center, rgba(30,30,30, 0.5) 0%, rgba(0,0,0,1) 80%);
    text-align: center;
}

.subtitle-cta {
    font-size: 1.5rem;
    color: var(--accent-secondary);
    margin-bottom: 3rem;
    margin-top: 1rem;
}

.audit-form {
    max-width: 600px;
    margin: 0 auto;
    text-align: left;
}

.form-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
    margin-bottom: 2rem;
}

@media (min-width: 640px) {
    .form-grid {
        grid-template-columns: 1fr 1fr;
    }
    .full-width {
        grid-column: span 2;
    }
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: var(--text-muted);
}

.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border-width: 0;
}

.form-group input,
.form-group textarea {
    width: 100%;
    background-color: #111;
    border: 1px solid #333;
    border-radius: 8px;
    padding: 1rem;
    color: var(--text-color);
    font-family: var(--font-main);
    font-size: 1rem;
    transition: all 0.3s ease;
}

.form-group input:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--accent-primary);
    box-shadow: 0 0 10px rgba(0, 229, 255, 0.2);
    background-color: #1a1a1a;
}

.form-group textarea {
    resize: vertical;
}

.form-group input::placeholder,
.form-group textarea::placeholder {
    color: #AAAAAA;
    opacity: 1;
}

.audit-form .cta-button-main {
    max-width: 450px;
    margin: 2rem auto 0;
    display: block;
}

/* Footer */
footer {
    padding: 4rem 2rem;
    text-align: center;
    border-top: 1px solid #222;
    background-color: #050505;
}

.footer-link {
    color: var(--accent-primary);
    text-decoration: none;
    font-size: 1.2rem;
    display: block;
    margin: 1rem 0;
}

.footer-legal {
    margin-top: 1.5rem;
    font-size: 0.9rem;
}

.legal-link {
    color: #888;
    text-decoration: none;
    transition: color 0.3s;
}

.legal-link:hover {
    color: #ccc;
}

.separator {
    color: #444;
    margin: 0 0.5rem;
}

.copyright {
    color: #666;
    font-size: 0.9rem;
    margin-top: 2rem;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .hero-content h1 {
        font-size: 2.5rem;
    }
    
    .navbar {
        height: auto;
        padding: 1rem;
        flex-direction: column;
        gap: 1rem;
    }

    .hero {
        padding-top: 120px; /* Adjust for taller mobile navbar if needed */
    }

    .nav-links {
        display: flex;
        gap: 1.5rem;
        font-size: 0.9rem;
    }
}

/* Cookie Banner */
.cookie-banner {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(10, 10, 10, 0.95);
    border-top: 1px solid #333;
    padding: 1.5rem;
    z-index: 9999;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: 0 -5px 20px rgba(0,0,0,0.5);
    animation: slideUp 0.5s ease-out;
}

@keyframes slideUp {
    from { transform: translateY(100%); }
    to { transform: translateY(0); }
}

.cookie-content {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 2rem;
    flex-wrap: wrap;
}

.cookie-content p {
    color: #fff;
    font-size: 0.95rem;
    flex: 1;
    min-width: 250px;
}

.cookie-buttons {
    display: flex;
    gap: 1rem;
}

.cookie-btn {
    padding: 0.6rem 1.2rem;
    border-radius: 4px;
    font-weight: 600;
    cursor: pointer;
    font-size: 0.9rem;
    transition: all 0.3s;
    border: none;
}

.cookie-btn.accept {
    background-color: var(--accent-primary);
    color: #000;
}

.cookie-btn.accept:hover {
    box-shadow: 0 0 10px rgba(0, 229, 255, 0.4);
    transform: translateY(-1px);
}

.cookie-btn.necessary {
    background-color: #333;
    color: #fff;
    border: 1px solid #444;
}

.cookie-btn.necessary:hover {
    background-color: #444;
}
"""

JS_CONTENT = """
document.addEventListener('DOMContentLoaded', () => {
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if(target){
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Simple animation on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });

    // Cookie Banner Logic
    const cookieBanner = document.getElementById('cookie-banner');
    const acceptBtn = document.getElementById('accept-cookies');
    const necessaryBtn = document.getElementById('necessary-cookies');
    
    const cookiesAccepted = localStorage.getItem('cookiesAccepted');
    
    if (!cookiesAccepted) {
        // Show banner with a small delay for smoother entrance
        setTimeout(() => {
            cookieBanner.style.display = 'block';
        }, 1000);
    }
    
    if (acceptBtn) {
        acceptBtn.addEventListener('click', () => {
            localStorage.setItem('cookiesAccepted', 'true');
            cookieBanner.style.display = 'none';
        });
    }

    if (necessaryBtn) {
        necessaryBtn.addEventListener('click', () => {
             // Treat "Necessary Only" as accepted for the purpose of hiding the banner
             // In a real implementation, this would handle consent status differently
            localStorage.setItem('cookiesAccepted', 'necessary');
            cookieBanner.style.display = 'none';
        });
    }

    // Elements to animate
    const cards = document.querySelectorAll('.card');
    const steps = document.querySelectorAll('.step');
    const faqItems = document.querySelectorAll('.faq-item');
    const formGroups = document.querySelectorAll('.form-group');

    [...cards, ...steps, ...faqItems, ...formGroups].forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});
"""

def write_file(filename, content):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {filepath}")

def main():
    print("Starting IRARH Landing Page Build...")
    write_file('index.html', HTML_CONTENT)
    write_file('privacy.html', PRIVACY_CONTENT)
    write_file('legal.html', LEGAL_CONTENT)
    write_file('style.css', CSS_CONTENT)
    write_file('success.html', SUCCESS_CONTENT)
    write_file('script.js', JS_CONTENT)
    print("Build Complete.")

if __name__ == "__main__":
    main()
