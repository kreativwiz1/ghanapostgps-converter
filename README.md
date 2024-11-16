# GhanaPostGPS to Google Maps Converter 🗺️

A user-friendly Streamlit web application that seamlessly converts GhanaPostGPS digital addresses into Google Maps locations. Get detailed location information and interactive map views for any GhanaPostGPS address.

## ✨ Features

- **Address Conversion**
  - GhanaPostGPS to coordinates transformation
  - High-precision latitude/longitude mapping
  - Robust error handling

- **Location Details**
  - Area name and description
  - District information
  - Regional classification
  - Street identification
  - Postal code lookup

- **Interactive Visualization**
  - Embedded Google Maps view
  - Dynamic map markers
  - Zoom controls
  - Satellite/terrain toggle

- **Convenience Features**
  - One-click Google Maps opening
  - Location sharing capabilities
  - Address validation
  - Search history

## 🛠️ Technical Requirements

### Software Dependencies
- Python 3.10 or higher
- Streamlit
- Requests library

### API Requirements
- GhanaPostGPS API access
- Google Maps API key

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ghanapostgps-converter.git
cd ghanapostgps-converter
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Configure API keys (create a `.env` file):
```env
GHANA_POST_API_KEY=your_api_key_here
GOOGLE_MAPS_API_KEY=your_api_key_here
```

## 💻 Usage

1. Launch the application:
```bash
streamlit run main.py
```

2. Access the web interface:
```
http://localhost:8501
```

3. Enter GhanaPostGPS address:
   - Format: `XX-YYYY-ZZZZ`
   - Example: `GG-935-8464`

4. Click "Show Map" to view:
   - Detailed location information
   - Interactive map
   - Sharing options

## 🗺️ Example Addresses

| Address | Location | Region |
|---------|----------|---------|
| GG-935-8464 | Accra Central | Greater Accra |
| AK-456-7890 | Kumasi | Ashanti |
| NT-234-5678 | Tamale | Northern |

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|-----------|
| GHANA_POST_API_KEY | GhanaPostGPS API key | Yes |
| GOOGLE_MAPS_API_KEY | Google Maps API key | Yes |
| STREAMLIT_SERVER_PORT | Custom port (default: 8501) | No |

### API Configuration
```python
# config.py
GHANA_POST_API_URL = "https://api.ghanapostgps.com/v1"
GOOGLE_MAPS_EMBED_URL = "https://www.google.com/maps/embed/v1/place"
```

## 🔍 Error Handling

| Error | Description | Solution |
|-------|-------------|----------|
| Invalid Address | Malformed GhanaPostGPS code | Check address format |
| API Timeout | Server response delay | Retry request |
| Location Not Found | Address not in database | Verify address |

## 📊 Performance

- Average response time: < 2 seconds
- Supported concurrent users: 100+
- Cache duration: 24 hours

## 🛡️ Security Features

- API key protection
- Input validation
- Rate limiting
- HTTPS enforcement

## 🧪 Testing

Run the test suite:
```bash
poetry run pytest
```

Example test:
```python
def test_address_conversion():
    result = convert_address("GG-935-8464")
    assert result["found"] == True
    assert "latitude" in result
    assert "longitude" in result
```

## 📱 Mobile Support

- Responsive design
- Touch-friendly interface
- Mobile-optimized maps
- Share location feature

## 🔄 Updates

Latest Version: 1.0.0
- Initial release with core functionality
- Google Maps integration
- Basic location details
- Address validation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add tests for new features
- Update documentation
- Maintain type hints

## 📮 Support

For support:
- Open an issue in the GitHub repository
- Check FAQ in Wiki
- Contact maintainers

## 🙏 Acknowledgments

- GhanaPostGPS for API access
- Google Maps Platform
- Streamlit community
- Project contributors
