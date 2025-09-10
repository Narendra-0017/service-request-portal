# Service Portal

A modern web-based service request portal built with Flask, featuring both regular and emergency services.

## Features

### 1. Service Categories
- **Regular Services**
  - Plumbing 🚰
  - Electrical ⚡
  - Carpentry 🔨
  - Cleaning 🧹
  - Gardening 🌺
  - Automotive 🚗

- **Emergency Services** (with special highlighting)
  - Ambulance 🚑
  - Police 👮
  - Fire Fighter 🚒

### 2. User Interface
- Modern, responsive design with Bootstrap
- Light blue color scheme for professional appearance
- Interactive service cards with hover effects
- Service-specific icons for better visual representation
- Emergency services highlighted with:
  - Red pulsing buttons
  - Distinct placement at the end of the list
  - Special attention-grabbing animations

## Technical Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite
- **Icons**: Bootstrap Icons

## Project Structure

```
Service_Portal/
├── app.py              # Main Flask application
├── init_db.py          # Database initialization script
├── static/
│   └── css/
│       └── style.css   # Custom styles
├── templates/
│   ├── base.html       # Base template with common elements
│   └── index.html      # Main service listing page
└── README.md           # This file
```

## Features in Detail

1. **Service Cards**
   - Each service is presented in a card format
   - Cards include service-specific icons
   - Hover effects for better interactivity

2. **Emergency Services**
   - Positioned at the end for clear visibility
   - Red, pulsing request buttons
   - Distinct styling to draw attention

3. **Responsive Design**
   - Works on desktop and mobile devices
   - Adapts to different screen sizes
   - Maintains functionality across devices
