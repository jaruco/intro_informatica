from django.core.management.base import BaseCommand
from learning_app.models import Topic, Chapter


class Command(BaseCommand):
    help = 'Load sample curriculum data (3 phases with chapters)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Loading sample curriculum...'))

        # PHASE 1: Personalización
        topic1, created = Topic.objects.update_or_create(
            title="Mi Cuartel General",
            defaults={
                'description': 'Personaliza tu computadora para que refleje tu personalidad. Cambios visuales e inmediatos que te harán sentir la máquina como propia.',
                'order': 1,
            }
        )

        chapters_phase1 = [
            {
                'title': 'Cambiar Fondo de Pantalla y Colores',
                'description': 'Aprende a **personalizar el fondo** de tu escritorio y los **colores del sistema**.',
                'content': '''## Cambiar Fondo de Pantalla

El fondo de pantalla es lo primero que ves cuando enciendes tu computadora. ¡Hazlo especial!

### Pasos:
1. **Haz clic derecho** en el escritorio
2. Selecciona **"Personalizar"**
3. Elige **"Fondo"**
4. Selecciona una **imagen que te guste** (fotos de tus hobbies, videojuegos, naturaleza, etc.)
5. También puedes usar **tus propias fotos**

### Pro Tip:
Busca imágenes en sitios como **Unsplash.com** o **Pexels.com** para fondos de alta calidad.
''',
                'difficulty': 'easy',
                'estimated_time': 10,
                'xp_reward': 25,
                'order': 1,
            },
            {
                'title': 'Organiza la Barra de Tareas',
                'description': 'Aprende a **añadir, quitar y organizar** tus aplicaciones favoritas en la **barra de tareas**.',
                'content': '''## La Barra de Tareas

La barra de tareas es tu panel de control rápido. Coloca aquí tus **apps favoritas** para acceso inmediato.

### Cómo fijar apps:
1. Abre el **Menú de Inicio** (botón Windows)
2. Busca la aplicación que quieres **fijar**
3. **Haz clic derecho** y selecciona **"Fijar a la barra de tareas"**

### Cómo reordenar:
1. **Arrastra los iconos** a la posición que prefieras
2. Los **apps más usados** al principio

### Apps recomendadas para fijar:
- **Navegador** (Edge, Chrome)
- **Explorador de Archivos**
- **Word/Excel** o LibreOffice
- **Tus juegos** favoritos
''',
                'difficulty': 'easy',
                'estimated_time': 15,
                'xp_reward': 30,
                'order': 2,
            },
            {
                'title': 'Modo Oscuro/Claro y Sonidos',
                'description': 'Configura el **modo oscuro** para cuidar tus ojos y **personaliza los sonidos** del sistema.',
                'content': '''## Modo Oscuro vs Modo Claro

El modo oscuro es más cómodo para los ojos cuando trabajas por la noche. ¡Elige lo que te guste!

### Activar Modo Oscuro:
1. Abre **Configuración** (Win + I)
2. Ve a **"Personalización"**
3. Haz clic en **"Colores"**
4. Selecciona **"Oscuro"**

### Personalizar Sonidos:
1. Abre **Configuración**
2. Ve a **"Sistema"** → **"Sonido"**
3. **Ajusta el volumen** general
4. Puedes **cambiar el sonido** de notificaciones

### Pro Tip:
Usa **"Modo automático"** para que Windows cambie a oscuro cuando anochece.
''',
                'difficulty': 'easy',
                'estimated_time': 8,
                'xp_reward': 20,
                'order': 3,
            },
            {
                'title': '🏆 RETO: Navega el Menú Configuración',
                'description': 'Desafío: **Encuentra 5 opciones diferentes** en el menú de Configuración que **no conocías**.',
                'content': '''## 🎮 El Reto del Explorador

Es hora de convertirte en un explorador de Windows. Tu misión es **descubrir opciones ocultas**.

### Tu Misión:
Abre **Configuración** (Win + I) y encuentra estas **5 opciones**:
1. Encuentra dónde **cambiar tu cuenta** de usuario
2. Busca dónde **actualizar** tu computadora
3. Localiza las **opciones de privacidad**
4. Encuentra donde **ver tus apps** instaladas
5. Busca donde **cambiar el idioma** del sistema

### Bonus:
**Toma screenshots** de cada uno y colócalos en una carpeta **"Mi Exploración"**

### Habilidad Oculta Desbloqueada:
⭐ **Navegación Experta** del Menú de Configuración de Windows
''',
                'difficulty': 'hard',
                'estimated_time': 20,
                'xp_reward': 75,
                'order': 4,
            },
        ]

        for chapter_data in chapters_phase1:
            Chapter.objects.update_or_create(
                topic=topic1,
                title=chapter_data['title'],
                defaults=chapter_data
            )

        self.stdout.write(self.style.SUCCESS(f'✅ Phase 1: {topic1.title} created with {len(chapters_phase1)} chapters'))

        # PHASE 2: El Maestro de los Archivos
        topic2, created = Topic.objects.update_or_create(
            title="El Archivo Maestro",
            defaults={
                'description': 'Organiza tus archivos de forma ordenada. Aprenderás a crear carpetas, mover archivos y encontrar lo que buscas rápidamente.',
                'order': 2,
            }
        )

        chapters_phase2 = [
            {
                'title': 'Crea tu Estructura de Carpetas',
                'description': 'Aprende a **crear una estructura organizada** de carpetas para tus **hobbies y tareas**.',
                'content': '''## Organizando tu Espacio Digital

Así como ordenas tu cuarto, también debes organizar tus archivos. Una **buena estructura** hace todo más fácil.

### Crea estas carpetas principales:
1. **Juegos** - Descargas y videos de juegos
2. **Dibujos** - Tus creaciones artísticas
3. **Música** - Canciones que te gustan
4. **Tareas** - Trabajos escolares
5. **Descargas** - Archivos temporales

### Cómo crear carpetas:
1. Abre **Explorador de Archivos** (Win + E)
2. Ve a tu carpeta **Documentos**
3. **Haz clic derecho** → **"Nueva carpeta"**
4. **Dale un nombre**

### Subcarpetas:
Dentro de **"Tareas"**, puedes crear: **Matemáticas**, **Español**, **Ciencias**, etc.
''',
                'difficulty': 'easy',
                'estimated_time': 15,
                'xp_reward': 30,
                'order': 1,
            },
            {
                'title': 'Cortar, Pegar y Atajos Mágicos (Ctrl+C, Ctrl+V)',
                'description': 'Domina los **atajos de teclado** para **mover archivos rápidamente**.',
                'content': '''## Atajos Mágicos de Archivos

Estos atajos te ahorrarán toneladas de tiempo. ¡Aprenderlos ahora te hará mucho más rápido!

### Los 3 Atajos Esenciales:
- **Ctrl + C** = **Copiar** (crear una copia)
- **Ctrl + X** = **Cortar** (preparar para mover)
- **Ctrl + V** = **Pegar** (colocar el archivo)

### Cómo mover un archivo:
1. **Haz clic** en el archivo
2. Presiona **Ctrl + X** (lo cortamos)
3. **Navega** a la carpeta destino
4. Presiona **Ctrl + V** (lo pegamos)

### Otros Atajos Útiles:
- **Ctrl + Z** = **Deshacer** (si cometiste un error)
- **Ctrl + A** = **Seleccionar todo**
- **Del** = **Eliminar**
''',
                'difficulty': 'easy',
                'estimated_time': 12,
                'xp_reward': 40,
                'order': 2,
            },
            {
                'title': 'Organiza Archivos por Tipos',
                'description': 'Aprende a **mover archivos** a sus carpetas correspondientes y **nombrar correctamente**.',
                'content': '''## El Gran Limpiador

Tu carpeta **Descargas** probablemente está llena de archivos aleatorios. ¡Vamos a **organizarla**!

### Pasos para organizar:
1. Abre la carpeta **Descargas**
2. Para cada archivo, **decide dónde va** (Juegos, Música, Documentos, etc.)
3. **Corta y pega** en la carpeta correcta

### Nombres de Archivos Buenos:
- ✅ **"Trabajo_Matematicas_2025.docx"**
- ✅ **"Cancion_Favorita.mp3"**
- ❌ "jsdkjdkj.txt"
- ❌ "archivo (1) (2) (3).pdf"

### Pro Tips:
- Usa **nombres descriptivos**
- **Evita espacios** largos
- Usa **guiones** o **guiones bajos** para separar palabras
''',
                'difficulty': 'easy',
                'estimated_time': 10,
                'xp_reward': 35,
                'order': 3,
            },
            {
                'title': 'El Buscador de Windows (Win + S)',
                'description': 'Aprende a **usar la búsqueda de Windows** para **encontrar archivos rápidamente**.',
                'content': '''## Encuentra lo que Necesitas en Segundos

¿No recuerdas dónde guardaste ese archivo? Windows tiene un **buscador poderoso**.

### Cómo buscar archivos:
1. Presiona **Win + S** (o **haz clic** en la lupa en la barra de tareas)
2. **Escribe el nombre** del archivo o parte de él
3. Windows **buscará** en toda tu computadora

### Buscar por Tipo:
- Escribe **"*.mp3"** para encontrar todas las **canciones**
- Escribe **"*.docx"** para encontrar todos los **documentos** Word
- Escribe **"*.jpg"** para encontrar todas las **imágenes**

### Búsqueda Avanzada:
1. Abre **Explorador de Archivos**
2. En la **barra de búsqueda**, haz clic en **"Herramientas"**
3. Puedes **filtrar** por fecha de modificación, tamaño, tipo, etc.
''',
                'difficulty': 'easy',
                'estimated_time': 8,
                'xp_reward': 25,
                'order': 4,
            },
            {
                'title': '🏆 RETO: Búsqueda del Tesoro',
                'description': '**Encuentra un archivo oculto** en una subcarpeta profunda usando **solo el buscador de Windows**.',
                'content': '''## 🗺️ La Búsqueda del Tesoro Digital

Tu misión: **Encontrar archivos ocultos** en profundidades oscuras de tu computadora.

### Tu Tarea:
1. Abre **Explorador de Archivos**
2. Crea una carpeta llamada **"Tesoro"** en Documentos
3. Dentro, crea **subcarpetas anidadas**: **Mapa** → **Pistas** → **Final**
4. Coloca una **imagen** (cualquier foto) en la carpeta **"Final"** con nombre: **"TESORO_ENCONTRADO.jpg"**
5. Ahora usa **Win + S** y busca **"TESORO_ENCONTRADO"**
6. ¿Lo encontró?

### Bonus Challenge:
**Crea 10 carpetas** con nombres aleatorios. **Esconde 5 imágenes** en diferentes carpetas. Usa **Win + S** para encontrarlas todas en menos de **2 minutos**.

### Habilidad Oculta Desbloqueada:
⭐ **Maestría en Navegación** del Explorador de Archivos
''',
                'difficulty': 'hard',
                'estimated_time': 30,
                'xp_reward': 110,
                'order': 5,
            },
        ]

        for chapter_data in chapters_phase2:
            Chapter.objects.update_or_create(
                topic=topic2,
                title=chapter_data['title'],
                defaults=chapter_data
            )

        self.stdout.write(self.style.SUCCESS(f'✅ Phase 2: {topic2.title} created with {len(chapters_phase2)} chapters'))

        # PHASE 3: Superpoderes del Teclado
        topic3, created = Topic.objects.update_or_create(
            title="Velocidad de Hacker",
            defaults={
                'description': 'Domina el teclado y conviértete en un usuario rápido. Los atajos y la mecanografía rápida son tus superpoderes.',
                'order': 3,
            }
        )

        chapters_phase3 = [
            {
                'title': 'Juegos de Mecanografía Online',
                'description': 'Aprende a **escribir rápido** jugando **TypeRacer** y otros juegos de mecanografía.',
                'content': '''## ⚡ Escribe Más Rápido Que tus Amigos

La **velocidad al escribir** es una habilidad que impresionará a todos. ¡Y es **divertido** practicarla!

### Juegos Recomendados:
- **TypeRacer** (https://play.typeracer.com/?universe=lang_es) - ¡**Carrera de autos** escribiendo!
- **Keybr** (https://www.keybr.com/) - **Generador de palabras** aleatorias
- **Nitro Type** - **Juego competitivo** con recompensas

### Cómo Mejorar tu Velocidad:
1. **Practica 15 minutos** cada día
2. **Mantén los dedos** en la posición correcta (**ASDF** y **JKL;**)
3. **Mira la pantalla**, no el teclado
4. **Aumenta la dificultad** gradualmente

### Objetivo:
Llega a **60+ palabras por minuto**. ¡Serás más rápido que tus amigos!
''',
                'difficulty': 'easy',
                'estimated_time': 20,
                'xp_reward': 50,
                'order': 1,
            },
            {
                'title': 'Atajos Mágicos del Teclado',
                'description': 'Aprende los **atajos de teclado** que usan los **hackers y profesionales**.',
                'content': '''## 🔑 Los Atajos de los Profesionales

Estos atajos te harán parecer un hacker. ¡Y son reales, no cine!

### Atajos de Ventanas:
- **Alt + Tab** = **Cambiar** entre ventanas abiertas
- **Win + D** = **Mostrar/ocultar** escritorio
- **Win + E** = **Abrir** Explorador de Archivos
- **Win + I** = **Abrir** Configuración
- **Win + V** = **Abrir** historial del portapapeles
- **Win + X** = **Menú** avanzado

### Atajos de Gestión de Ventanas:
- **Win + ←** = **Ventana a la izquierda** (mitad pantalla)
- **Win + →** = **Ventana a la derecha** (mitad pantalla)
- **Alt + F4** = **Cerrar** ventana actual

### Super Avanzado:
- **Ctrl + Alt + Esc** = **Abre** Task Manager rápidamente
- **Win + Shift + S** = **Captura de pantalla** (dibuja selección)
''',
                'difficulty': 'easy',
                'estimated_time': 12,
                'xp_reward': 40,
                'order': 2,
            },
            {
                'title': 'Atajos Productivos (Ctrl+Z, Ctrl+S, etc)',
                'description': 'Domina los **atajos esenciales**: **guardar, deshacer, seleccionar todo** y más.',
                'content': '''## 💾 Los Atajos que Usarás TODO el Tiempo

Estos atajos funcionan en casi todas las aplicaciones. Son **ESENCIALES**.

### Los Big 5:
- **Ctrl + S** = **Guardar** (¡SIEMPRE! No pierdas tu trabajo)
- **Ctrl + Z** = **Deshacer** (si metiste la pata)
- **Ctrl + Y** = **Rehacer** (si deshiciste demasiado)
- **Ctrl + A** = **Seleccionar todo**
- **Ctrl + P** = **Imprimir**

### Copiar/Pegar (ya lo sabes, pero importante):
- **Ctrl + C** = **Copiar**
- **Ctrl + X** = **Cortar**
- **Ctrl + V** = **Pegar**

### Extra Útiles:
- **Ctrl + F** = **Buscar** en la página
- **Ctrl + T** = **Nueva pestaña** (navegador)
- **Ctrl + W** = **Cerrar** pestaña
- **Ctrl + +** = **Zoom in**
- **Ctrl + -** = **Zoom out**

### Consejo Pro:
**Practica Ctrl + S** después de cada cambio. Es tu amigo. Enserio.
''',
                'difficulty': 'easy',
                'estimated_time': 10,
                'xp_reward': 35,
                'order': 3,
            },
            {
                'title': 'Lanzador de Apps por Teclado',
                'description': 'Aprende a **abrir aplicaciones** usando **solo el teclado**. ¡Mucho más rápido!',
                'content': '''## 🚀 Abre Apps Más Rápido Que Nadie

¿Esperar a que aparezca el menú? ¡Nah! Los **profesionales** usan el **teclado**.

### Método 1: Win + Nombre del App
1. Presiona **Win** (aparece el buscador)
2. **Empieza a escribir** "chrome", "notepad", "excel", etc.
3. Presiona **Enter** cuando vea el app que buscas

**Ejemplo:** **Win** → **"spotify"** → **Enter** → Spotify abierto en 2 segundos

### Método 2: Win + X (Menú Avanzado)
Presiona **Win + X** para acceder a:
- **P** = Apagar/Reiniciar
- **A** = Administrador de tareas
- **T** = Terminal
- **D** = Administrador de dispositivos

### Atajos Directos a Apps:
También puedes **crear atajos personalizados** en la barra de tareas y acceder con **Win + número**:
- **Win + 1** = Primer app de la barra de tareas
- **Win + 2** = Segundo app
- **Win + 3** = Tercer app, etc.
''',
                'difficulty': 'medium',
                'estimated_time': 8,
                'xp_reward': 30,
                'order': 4,
            },
            {
                'title': '🏆 RETO: El Dictado Fugaz',
                'description': 'Carrera de velocidad: **Escribe rápido, abre apps sin mouse, domina el teclado**.',
                'content': '''## ⚡ El Desafío Final: Velocidad de Hacker

Es hora de probar que eres un **verdadero usuario de teclado**. ¡**Este es tu momento**!

### Reto 1: Speed Typing (5 minutos)
1. Abre **TypeRacer** (https://play.typeracer.com/?universe=lang_es)
2. **Completa al menos 3 carreras**
3. **Intenta superar 60 palabras** por minuto

### Reto 2: Speed Launching (Contra cronómetro)
¿**Quién abre estas apps más rápido**? **Solo teclado, ¡SIN mouse!**
1. Abre **Notepad** (Win + "notepad" + Enter)
2. Abre **Calculator** (Win + "calc" + Enter)
3. Abre **Chrome** (Win + "chrome" + Enter)
4. Abre **Excel** (Win + "excel" + Enter)
5. Vuelve al **Escritorio** (Win + D)

**Objetivo:** **Completar TODO en menos de 30 segundos**

### Reto 3: El Dictado de Velocidad
1. Abre **Notepad** (teclas, no mouse)
2. **Alguien te dicta** un párrafo (o lo escribes de memoria)
3. **Incluye puntuación** correcta
4. ¿**Cuántas palabras** escribes en 5 minutos?

### Bonus: Carrera Contra la Computadora
Si encuentras a alguien con mouse, **compitan**:
- **Tú:** Solo teclado
- **Ellos:** Mouse + teclado
- **Misión:** Buscar 5 archivos, abrir 3 apps, escribir un párrafo
- ¿**Quién termina primero**?

### Habilidad Oculta Desbloqueada:
⭐ **Agilidad de Teclado Profesional** + **Confianza Extrema**

### Meta Final:
¡**Completaste los 3 superpoderes**! Eres oficialmente un **"Velocidad de Hacker"**. Tus amigos quedarán impresionados cuando vean qué rápido trabajas en Windows.
''',
                'difficulty': 'hard',
                'estimated_time': 25,
                'xp_reward': 145,
                'order': 5,
            },
        ]

        for chapter_data in chapters_phase3:
            Chapter.objects.update_or_create(
                topic=topic3,
                title=chapter_data['title'],
                defaults=chapter_data
            )

        self.stdout.write(self.style.SUCCESS(f'✅ Phase 3: {topic3.title} created with {len(chapters_phase3)} chapters'))

        # PHASE 4: Seguridad y Navegación (Internet Inteligente)
        topic4, created = Topic.objects.update_or_create(
            title="Internet Inteligente",
            defaults={
                'description': 'En lugar de prohibir, enséñale a ser un "escudo humano" contra virus. Navegación segura y criterio digital.',
                'order': 4,
            }
        )

        chapters_phase4 = [
            {
                'title': 'Modo Incógnito y Bloqueo de Anuncios',
                'description': 'Aprende a **navegar privado** y a instalar **uBlock Origin** para bloquear anuncios.',
                'content': '''## 🛡️ Navegación Segura y Sin Molestias

Internet es increíble, pero los anuncios pueden ser peligrosos o molestos. ¡Toma el control!

### Modo Incógnito:
Navega sin guardar historial en tu computadora.
1. Abre el navegador
2. Presiona **Ctrl + Shift + N** (Chrome/Edge) o **Ctrl + Shift + P** (Firefox)
3. ¡Estás en modo espía!

### Bloqueo de Anuncios (uBlock Origin):
La mejor defensa contra ventanas emergentes.
1. Busca **"uBlock Origin extension"**
2. Instálalo en tu navegador
3. Verás cómo desaparecen los anuncios en YouTube y webs.
''',
                'difficulty': 'easy',
                'estimated_time': 15,
                'xp_reward': 35,
                'order': 1,
            },
            {
                'title': 'Detectives de Links: ¿Real o Falso?',
                'description': 'Aprende a identificar un **link sospechoso** o un **botón de descarga falso**.',
                'content': '''## 🔍 Detectando Trampas

No hagas clic en todo lo que brilla. Los hackers usan botones falsos.

### Cómo identificar un link falso:
1. **Pasa el mouse** sobre el link (¡SIN hacer clic!)
2. Mira la **barra inferior** del navegador
3. ¿La dirección coincide con lo que esperas?
   - ✅ `google.com/...` (Seguro)
   - ❌ `g00gle-premios.xyz/...` (¡Falso!)

### Botones de Descarga:
Si ves 5 botones de "DESCARGAR", generalmente el **verdadero es el más pequeño** y menos llamativo. Los grandes y parpadeantes suelen ser publicidad.
''',
                'difficulty': 'medium',
                'estimated_time': 12,
                'xp_reward': 40,
                'order': 2,
            },
            {
                'title': 'Windows Defender: Escaneo Rápido',
                'description': 'Usa **Windows Defender** para buscar virus y proteger tu PC.',
                'content': '''## 🩺 El Doctor de tu PC

Windows ya trae un antivirus excelente. Aprende a usarlo.

### Pasos para un chequeo:
1. Presiona **Win + S**
2. Escribe **"Seguridad de Windows"**
3. Ve a **"Protección contra virus y amenazas"**
4. Haz clic en **"Examen rápido"**
''',
                'difficulty': 'easy',
                'estimated_time': 10,
                'xp_reward': 30,
                'order': 3,
            },
            {
                'title': '🏆 RETO: Ciberseguridad Básica',
                'description': 'Demuestra tu **criterio digital** y asegura tu entorno.',
                'content': '''## 🕵️‍♂️ Auditoría de Seguridad

Es hora de verificar tus defensas.

### Tu Misión:
1. Abre una ventana en **Modo Incógnito**
2. Verifica si tienes activo **Windows Defender** (debe tener check verde)
3. Identifica un sitio seguro (candado 🔒 en la barra de dirección)

### Habilidad Oculta Desbloqueada:
⭐ **Criterio Digital** y **Escudo Humano** contra virus.
''',
                'difficulty': 'hard',
                'estimated_time': 15,
                'xp_reward': 75,
                'order': 4,
            },
        ]

        for chapter_data in chapters_phase4:
            Chapter.objects.update_or_create(
                topic=topic4,
                title=chapter_data['title'],
                defaults=chapter_data
            )

        self.stdout.write(self.style.SUCCESS(f'✅ Phase 4: {topic4.title} created with {len(chapters_phase4)} chapters'))

        # PHASE 5: Mantenimiento y Trucos
        topic5, created = Topic.objects.update_or_create(
            title="Mantenimiento y Trucos",
            defaults={
                'description': 'Enséñale que él puede arreglar cosas si la PC se pone lenta. Limpieza de motores y trucos de magia.',
                'order': 5,
            }
        )

        chapters_phase5 = [
            {
                'title': 'El Administrador de Tareas (Ctrl+Shift+Esc)',
                'description': 'Usa el **Administrador de Tareas** para cerrar apps que se traban.',
                'content': '''## 🚑 Reviviendo la PC

¿Se congeló un juego? ¿Chrome no responde? ¡No apagues el botón!

### El Truco de Magia:
Presiona **Ctrl + Shift + Esc** (todo junto con la mano izquierda).

### Qué hacer:
1. Se abre el **Administrador de Tareas**
2. Busca el programa que dice **"No responde"**
3. Clic derecho → **"Finalizar tarea"**
4. ¡Problema resuelto!
''',
                'difficulty': 'easy',
                'estimated_time': 10,
                'xp_reward': 35,
                'order': 1,
            },
            {
                'title': 'Limpieza de Motores',
                'description': 'Aprende a **vaciar la papelera** y usar el **Liberador de espacio**.',
                'content': '''## 🧹 Sacando la Basura Digital

Si tu PC está lenta, puede que tenga demasiados archivos temporales.

### Pasos de Limpieza:
1. **Vaciar Papelera:** Clic derecho en el icono del escritorio → "Vaciar papelera".
2. **Limpieza Profunda:**
   - Presiona **Win + S**
   - Escribe **"Liberador de espacio en disco"**
   - Selecciona las casillas de archivos temporales
   - Dale a "Aceptar"

¡Tu computadora se sentirá más ligera!
''',
                'difficulty': 'easy',
                'estimated_time': 15,
                'xp_reward': 30,
                'order': 2,
            },
            {
                'title': 'Capturas de Pantalla Pro (Win+Shift+S)',
                'description': 'Cómo capturar pantalla de forma pro con **Win + Shift + S**.',
                'content': '''## 📸 Capturas Perfectas

Olvídate de tomar fotos a la pantalla con el celular. Hazlo como un pro.

### El Atajo:
Presiona **Win + Shift + S**.

### Cómo funciona:
1. La pantalla se oscurece
2. **Dibuja un cuadro** sobre lo que quieres guardar
3. ¡Listo! Está copiado.
4. Ve a un chat o documento y presiona **Ctrl + V** para pegar.
''',
                'difficulty': 'easy',
                'estimated_time': 8,
                'xp_reward': 25,
                'order': 3,
            },
            {
                'title': '🏆 RETO: Mantenimiento Express',
                'description': 'Realiza una limpieza y **captura la evidencia**.',
                'content': '''## 🛠️ El Técnico de la Casa

Demuestra que puedes mantener tu equipo en forma.

### Misión:
1. Abre el **Administrador de Tareas**
2. Toma una captura (**Win + Shift + S**) de los procesos
3. Realiza una limpieza de la **Papelera**
4. ¡PC optimizada!

### Habilidad Oculta Desbloqueada:
⭐ **Autosuficiencia Técnica**
''',
                'difficulty': 'medium',
                'estimated_time': 15,
                'xp_reward': 60,
                'order': 4,
            },
        ]

        for chapter_data in chapters_phase5:
            Chapter.objects.update_or_create(
                topic=topic5,
                title=chapter_data['title'],
                defaults=chapter_data
            )

        self.stdout.write(self.style.SUCCESS(f'✅ Phase 5: {topic5.title} created with {len(chapters_phase5)} chapters'))

        self.stdout.write(self.style.SUCCESS(
            f'\n✨ Curriculum loaded successfully!\n'
            f'📚 Total Topics: 5\n'
            f'📖 Total Chapters: {len(chapters_phase1) + len(chapters_phase2) + len(chapters_phase3) + len(chapters_phase4) + len(chapters_phase5)}\n'
            f'⭐ Total XP Available: {sum([c["xp_reward"] for c in chapters_phase1 + chapters_phase2 + chapters_phase3 + chapters_phase4 + chapters_phase5])}'
        ))
