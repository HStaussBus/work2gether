# Replit.md

## Overview

This project is a web-based Item Overlap Matrix Visualization tool. It appears to be a single-page application designed to display and visualize overlapping relationships between different items in an interactive matrix format. The application uses a clean, modern web interface with responsive design principles to present complex data relationships in an easily digestible visual format.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

**Frontend Architecture**
- Pure HTML/CSS/JavaScript implementation without frameworks
- Single-page application (SPA) architecture
- Responsive design with mobile-first approach using viewport meta tags
- CSS-based styling with modern features like flexbox/grid layouts
- Component-based styling approach with modular CSS classes

**Backend Architecture (Deployment-Ready)**
- Custom Python HTTP server using `http.server` and `socketserver`
- Serves static files with proper MIME types and CORS headers
- Handles SPA routing by serving index.html for missing routes
- Port conflict resolution with automatic fallback to alternate ports
- Optimized for Replit deployment with proper error handling
- Entry point: `python main.py` on port 5000

**Visual Design System**
- Monochrome black and white theme for professional, minimal appearance
- Light grey background (#f8f9fa) for clean, neutral backdrop
- Green gradient highlighting system for connection strength visualization
- Card-based layout with shadows and rounded corners for modern appearance
- Legend system for data interpretation with green color coding
- Container-based responsive layout that handles overflow gracefully
- Network statistics section removed for cleaner interface

**Data Visualization**
- Matrix-based data presentation
- Interactive legend system for user guidance
- Scalable design that accommodates varying data sizes
- Visual hierarchy with clear typography and spacing

**Browser Compatibility**
- Standards-compliant HTML5 and CSS3
- Cross-browser compatible implementation
- No external framework dependencies ensuring fast load times

## External Dependencies

**Minimal Dependencies**
- Pure vanilla JavaScript, HTML, and CSS for frontend
- Python 3.11+ for backend server (built-in libraries only)
- No third-party libraries or frameworks required
- No external APIs or services
- Self-contained application with embedded CSV data
- No database required - data served from local CSV files
- No build tools or package managers needed

**Deployment Status**
- ✅ Ready for Replit deployment
- ✅ Web server properly configured on port 5000
- ✅ All JavaScript errors resolved
- ✅ HTTP health checks responding correctly
- ✅ Static file serving operational
- ✅ CORS headers configured for cross-origin requests

This architecture choice ensures maximum compatibility, fast loading times, and easy deployment to Replit or any web hosting service.