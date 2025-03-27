# Example 77 - Weather API app

import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter a city: ", self)
        self.city_input = QLineEdit(self)
        self.submit_button = QPushButton("Submit", self)
        self.temperature_label = QLabel(self)
        self.weather_icon_label = QLabel(self)
        self.description_label = QLabel(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.weather_icon_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.weather_icon_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.submit_button.setObjectName("submit_button")
        self.temperature_label.setObjectName("temperature_label")
        self.weather_icon_label.setObjectName("weather_icon_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton{                          
                font-size: 24px;
                font-family: calibri;                            
                padding: 4;                                                                    
            }
            QLabel#city_label{                        
                font-weight: bold;                
            }       
            QLineEdit#city_input{
                font-size: 36px;  
                padding: 8;              
            }
            QPushButton#submit_button{
                font-weight: bold;
                background-color: hsl(84, 100%, 63%);
                border: 3px solid;
                border-radius: 20px;
            }
            QPushButton#submit_button:hover{     
                background-color: hsl(84, 100%, 82%);                
            }
            QLabel#temperature_label{    
                font-size: 24px;            
                font-weight: bold;
                background-color: white;   
                border: 1px solid;
                border-radius: 4;    
                margin: 20;                                
            }
            QLabel#weather_icon_label{
                font-size: 50px;
                font-family: Segoe UI Emoji;
            }        
            QLabel#description_label{                                
                font-style: italic;                
            }
        """)

        self.submit_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "e24cf58eb9116258c14fe0e552ad7660"
        country_code = "pl"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status() # Throws an exception if data is invalid
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized\nInvalid API key")
                case 403:
                    self.display_error("Forbidden\nAccess denied")
                case 404:
                    self.display_error("Not found\nCity was not found")
                case 500:
                    self.display_error("Internal server error\nPlease try again later")
                case 502:
                    self.display_error("Bad gateway\nInvalid response from a server")
                case 503:
                    self.display_error("Service unavailable\nServer is down")
                case 504:
                    self.display_error("Gateway timeout\nNo response from server")
                case _:
                    self.display_error(f"HTTP error occurred\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection error\nCheck your Internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout error\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setText(message)
        self.weather_icon_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        temperature = data["main"]["temp"] - 273.15
        icon_id = data["weather"][0]["id"]
        description = data["weather"][0]["description"]

        self.temperature_label.setText(f"{temperature:.1f}°C")
        self.weather_icon_label.setText(self.get_weather_icon(icon_id))
        self.description_label.setText(description.capitalize())

    @staticmethod
    def get_weather_icon(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌨"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return ""


def weather_app():
    app = QApplication(sys.argv)
    app_window = WeatherApp()
    app_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    weather_app()
