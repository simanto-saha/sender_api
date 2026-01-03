# Django API Integration Demo

A Django web application demonstrating API integration with a custom REST API for employee management.

## 🌟 Features

### 1. Employee Data API
- Custom REST API endpoint integration
- Search employees by ID
- Displays comprehensive employee information
- Validates API responses and handles errors gracefully

## 🚀 Technologies Used

- **Django**: Web framework
- **Python Requests**: HTTP library for API calls
- **OpenWeather API**: External weather data provider
- **Custom REST API**: Employee management system
- **HTML/CSS**: Frontend styling

## 📋 Prerequisites

```bash
Python 3.x
Django 4.x or higher
requests library
```

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/simanto-saha/practice.git
cd your-repo-name
```

2. Install dependencies:
```bash
pip install django requests
```

3. Configure API keys in `settings.py`:
```python
OPENWEATHER_API_KEY = 'your_api_key_here'
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Allow network access (Windows):
```cmd
netsh advfirewall firewall add rule name="Django Port 9000" dir=in action=allow protocol=TCP localport=9000
```

6. Start the development server:
```bash
python manage.py runserver 0.0.0.0:9000
```

## 🌐 API Endpoints


### Employee API Integration
- **Endpoint**: `/check-api/`
- **Method**: GET
- **Parameters**: `id` (integer)
- **Example**: `http://localhost:9000/check-api/?id=123`

## 📱 Usage


### Employee Search
1. Navigate to the employee check page
2. Enter an employee ID
3. Click "Search" to fetch employee details
4. View employee information including name, email, phone, etc.

## 🎨 Features Highlights

- **Error Handling**: Comprehensive error messages for API failures
- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Gradient backgrounds and clean interface
- **Input Validation**: Required field validation on forms
- **Network Access**: Accessible from any device on the local network

## 🔒 Security Notes

- API keys are stored in `settings.py` (not in version control)
- Use environment variables for production deployment
- `ALLOWED_HOSTS` configured for network access

## 🐛 Troubleshooting

### Cannot access from other devices
1. Ensure `ALLOWED_HOSTS = ['*']` in settings.py
2. Run server with `0.0.0.0:9000`
3. Check firewall settings
4. Verify all devices are on the same network

### API not responding
1. Verify API keys are correct
2. Check internet connection for external APIs
3. Ensure custom API server is running (port 8000)
4. Review error messages in the interface


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available.

## 👤 Author

Your Name - Simanto Saha

## 🙏 Acknowledgments

- Django documentation
- Community contributors

---

⭐ If you found this project helpful, please give it a star!
