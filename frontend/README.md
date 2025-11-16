# FootGRX - Frontend

Una página web moderna para visualizar estadísticas deportivas de las 5 grandes ligas de Europa.

## Características

- **Diseño Moderno y Responsivo**: Adaptado para dispositivos móviles, tablets y escritorio
- **5 Ligas Europeas**: Premier League, La Liga, Serie A, Bundesliga y Ligue 1
- **Navegación Intuitiva**: Menú de navegación fijo con smooth scrolling
- **Animaciones Interactivas**: Contadores animados, tablas con animaciones on-scroll
- **Menú Móvil**: Hamburger menu para dispositivos móviles
- **Botón Scroll-to-Top**: Para facilitar la navegación en la página

## Estructura de Archivos

```
frontend/
├── index.html          # Página principal
├── css/
│   └── styles.css      # Estilos CSS
├── js/
│   └── main.js         # JavaScript funcional
└── assets/             # Recursos (imágenes, iconos, etc.)
```

## Cómo Usar

### Opción 1: Servidor Local con Python

```bash
cd frontend
python3 -m http.server 8080
```

Luego abre tu navegador en `http://localhost:8080`

### Opción 2: Servidor Local con Node.js

```bash
cd frontend
npx http-server -p 8080
```

Luego abre tu navegador en `http://localhost:8080`

### Opción 3: Abrir directamente

Simplemente abre el archivo `index.html` en tu navegador web preferido.

## Tecnologías Utilizadas

- **HTML5**: Estructura semántica moderna
- **CSS3**: Estilos avanzados con variables CSS, gradientes, animaciones
- **JavaScript ES6+**: Funcionalidad interactiva sin dependencias externas

## Secciones de la Página

1. **Home/Inicio**: Hero section con estadísticas generales
2. **Premier League**: Información y clasificación de la liga inglesa
3. **La Liga**: Información y clasificación de la liga española
4. **Serie A**: Información y clasificación de la liga italiana
5. **Bundesliga**: Información y clasificación de la liga alemana
6. **Ligue 1**: Información y clasificación de la liga francesa

## Características Técnicas

### Responsive Design
- Mobile First Approach
- Breakpoints: 768px (tablets), 480px (móviles)
- Grid y Flexbox para layouts flexibles

### Interactividad JavaScript
- Smooth scroll navigation
- Animated counters en hero section
- Mobile menu toggle
- Active navigation tracking
- Scroll-to-top button
- Intersection Observer para animaciones on-scroll

### Accesibilidad
- Marcado semántico HTML5
- ARIA labels para elementos interactivos
- Alto contraste en textos
- Navegación por teclado

## Personalización

### Colores de las Ligas
Los colores se definen en variables CSS en `styles.css`:

```css
--premier-color: #3d195b;
--laliga-color: #ff4757;
--seriea-color: #0066b2;
--bundesliga-color: #d20515;
--ligue1-color: #dfe902;
```

### Agregar Más Equipos
Edita las tablas en `index.html` en la sección correspondiente de cada liga.

### Integración con API
El archivo `main.js` incluye una función `updateStandings()` preparada para integración futura con APIs de datos deportivos.

## Navegadores Compatibles

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Licencia

© 2024 FootGRX. Todos los derechos reservados.
