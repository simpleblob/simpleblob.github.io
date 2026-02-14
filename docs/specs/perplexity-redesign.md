# Feature: Perplexity-Inspired Website Redesign

## Requirements

### Typography
- Replace current serif fonts (Charter/Palatino) with **Inter** web font (modern geometric sans-serif, closest free alternative to FK Grotesk)
- Set base font size to 18px with line-height 1.6 for improved readability
- Implement Perplexity's font weight hierarchy:
  - Body text: font-weight 400 (normal)
  - Strong/bold: font-weight 550-600 (medium/semibold)
  - h1: font-weight 800 (extrabold)
  - h2: font-weight 500 (medium)
  - h3-h6: font-weight 600 (semibold)
- Apply negative letter-spacing (-.025rem) for tighter, modern appearance
- Use system font fallback stack: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif

### Color Scheme
- Implement dual theme support with data-color-scheme attribute
- **Light mode:**
  - Background: #FCFCF9 (warm off-white)
  - Text: #2c2823 or similar dark for readability
  - Borders: subtle gray tones
- **Dark mode:**
  - Background: #100E12 (near-black)
  - Text: light gray/white (#e5e5e5 or similar)
  - Borders: subtle light borders
- Add theme toggle button in header/navigation

### Spacing & Layout
- Increase generous whitespace using rem-based spacing system:
  - Base unit: 0.25rem, 0.5rem, 1rem, 1.5rem, 2rem
  - Heading margins: Larger top margins (h1: 2rem+, h2: 1.6rem+)
  - Paragraph spacing: 1.25em between paragraphs
- Maintain current content max-width (26rem / ~650px for reading comfort)
- Update padding/margins throughout for airier feel

### Tables
- Redesign with clean, modern styling:
  - Remove heavy borders, use subtle 1px borders
  - Generous cell padding (0.75rem to 1rem)
  - Header row with subtle background differentiation
  - Row hover states for interactivity
  - Responsive: maintain readability on mobile

### Code Blocks
- Update monospace font stack: ui-monospace, SFMono-Regular, SF Mono, Monaco, Cascadia Code, Roboto Mono, Consolas, monospace
- Adjust code block styling for both light and dark modes
- Ensure syntax highlighting works in both themes
- Maintain scrollbar styling for code overflow

### CSS Architecture
- Use CSS custom properties (variables) for all design tokens:
  - --font-base, --font-heading
  - --color-bg-light, --color-bg-dark
  - --color-text-light, --color-text-dark
  - --space-xs, --space-sm, --space-md, --space-lg, --space-xl
- Implement prefers-color-scheme media query as default
- Allow manual theme override via data-color-scheme="light|dark"

### Web Font Loading
- Add Inter font via Google Fonts or self-hosted
- Use font-display: swap for performance
- Preload font files for faster rendering

### Templates
- Update Jinja2 templates (default.html, post.html, archive.html) to include:
  - Theme toggle button/script
  - Updated CSS link
  - Meta tags for theme-color

## Acceptance Criteria

- [ ] Website loads with Inter font (or system fallback) instead of Charter/Palatino
- [ ] Base body text is 18px with 1.6 line-height and -.025rem letter-spacing
- [ ] Light mode displays with #FCFCF9 background and dark text
- [ ] Dark mode displays with #100E12 background and light text
- [ ] Theme toggle button successfully switches between light/dark modes
- [ ] Theme preference persists in localStorage across page loads
- [ ] h1 headings are font-weight 800, h2 are 500, h3-h6 are 600
- [ ] Strong/bold text uses font-weight 550-600
- [ ] Tables have clean modern styling with hover states
- [ ] Code blocks render correctly in both themes with proper monospace font
- [ ] Spacing feels generous and modern (larger margins/padding than current)
- [ ] Reading width remains at 26rem max-width
- [ ] All pages (index, archive, posts, contact, experiments) use new design
- [ ] Design is responsive and works on mobile devices
- [ ] No layout shifts or FOUT (flash of unstyled text) on page load
- [ ] Generated blog posts from Markdown maintain proper styling

## Scope

### In scope
- Complete CSS redesign (css/default.css)
- Typography system (fonts, sizes, weights, spacing)
- Color system with light/dark themes and toggle
- Table styling overhaul
- Code block styling updates
- Template updates for theme toggle functionality
- Responsive design maintenance
- All existing pages (home, archive, posts, contact, experiments)

### Out of scope
- Changing HTML structure significantly (keep current semantic markup)
- Redesigning navigation layout (keep header/nav structure)
- Adding new pages or content
- Changing the build system (sitegen.py stays as-is)
- Modifying Markdown source files
- Adding animations or transitions beyond basic hover states
- Implementing additional color themes beyond light/dark
- Changing logo or branding
- Adding new JavaScript features beyond theme toggle
- Modifying responsive breakpoints (keep current mobile strategy)

## Design System Reference

Based on Perplexity.ai analysis:

**Font Sizes (rem):**
- h1: 2.25rem
- h2: 1.5rem  
- h3: 1.25rem
- body: 1rem (18px base)
- small: 0.875rem

**Spacing Scale:**
- xs: 0.25rem
- sm: 0.5rem
- md: 1rem
- lg: 1.5rem
- xl: 2rem

**Font Weights:**
- Normal: 400
- Medium: 500
- Semibold: 600
- Bold: 700
- Extrabold: 800

**Line Heights:**
- Tight: 1.25
- Base: 1.6
- Loose: 1.75
