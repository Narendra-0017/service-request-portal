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

### 3. Contact Information
- Indian format phone numbers (+91 format)
- Easy-to-access footer with contact details
- Professional email and location information

## Technical Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite
- **Icons**: Bootstrap Icons

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Service_Portal
   ```

2. **Set Up Python Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   # For Windows
   venv\Scripts\activate
   # For Unix/MacOS
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the Database**
   ```bash
   python init_db.py
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Portal**
   - Open your web browser
   - Visit: http://127.0.0.1:5000
   - The service portal should now be running locally

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

## Screenshots
[Add screenshots of your application here]

## Notes for Submission

This project demonstrates:
- Full-stack web development skills
- User interface design principles
- Emergency vs. regular service handling
- Modern web technologies implementation
- Responsive and accessible design

## Contact

For any queries regarding this project:
- Phone: +91 98765 43210
- Email: [Your Email]

---
© 2025 Service Portal. All rights reserved. 
- Display of service provider information upon submission 