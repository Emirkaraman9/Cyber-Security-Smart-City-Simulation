# 🏦 DigiBank – Smart City & Digital Banking Automation

DigiBank is a hybrid simulation platform that integrates **Digital Banking Systems** with **Smart City Infrastructure Management**.  
The project demonstrates how urban automation (IoT simulation) can coexist with secure financial transactions (Fiat & Crypto) in a monitored and protected environment.

Developed as a university project for **Cyber Security & Big Data**, focusing on:

- Secure software architecture  
- Object-Oriented Design  
- Design Patterns  
- Real-time system monitoring  
- Attack & defense simulations  

---

## 🚀 Features

### 🔐 1. Admin Panel – City Controller

**System Monitoring**
- Real-time CPU & RAM usage tracking (Simulated Server Health)

**Cyber Security Module**
- 🚨 Attack Simulation  
  - “Cyber Attack Alarm” triggers threaded email alerts  
  - Automatic logging system  
- 🛡 Defense Mechanism  
  - “System Restore” to normalize operations  

**User Management**
- Add / Remove / Search users  
- TXT file + Database integration  

**Smart City Automation**
- Control city infrastructure  
  - Street lights  
  - Traffic signals  

---

### 👤 2. User Panel – Resident

**Secure Authentication**
- Credential verification system

**Digital Wallet**
- View balance  
- Money transfer  
  - Fiat via IBAN  
  - Cryptocurrency (BTC / ETH simulation)

**Smart City Services**
- Pay utility bills  
  - Electricity  
  - Water  
  - Parking  
- Smart Home automation  
  - Example: “Night Mode”

**Transaction History**
- Personal logs  
- Past activities  

---

## 🛠 Technical Architecture

The project is developed with **Python** following strict **Object-Oriented Programming (OOP)** principles and modular architecture.

### 🧩 Design Patterns Implemented

- **Singleton Pattern**  
  - Ensures a single database connection instance throughout the lifecycle

- **Factory Pattern**  
  - Efficient creation of User and Admin objects based on login type

- **Observer Pattern**  
  - Logging system notifies Admin and writes to logs.txt upon critical events (Security Alarms)

---

## 💻 Tech Stack

- **Language:** Python 3.x  
- **GUI:** CustomTkinter / Tkinter  
- **Database:** SQLite  
- **Monitoring:** psutil  
- **Multithreading:** threading  
- **Email Alerts:** smtplib  

---

## 📸 Screenshots
<img width="550" height="542" alt="DigiBank Giriş Ekranı" src="https://github.com/user-attachments/assets/87e25d8f-555e-471f-92ec-f37189657944" />
<img width="487" height="641" alt="DigiBank Yönetici Giriş Ekranı" src="https://github.com/user-attachments/assets/989fe471-f4a7-46a2-99b5-78a3171aa097" />
<img width="1427" height="901" alt="Üye Arama Ekranı" src="https://github.com/user-attachments/assets/f6389251-e4f1-4cd8-a4e6-7faf171a8eeb" />
<img width="1210" height="901" alt="Üye Ekleme Ekranı" src="https://github.com/user-attachments/assets/5836d18c-21c1-467b-8698-c168805ec79d" />
<img width="1201" height="890" alt="Yönetici Ekranı" src="https://github.com/user-attachments/assets/8b40d8dd-21e0-42e5-b04f-3b402cd45a5b" />
<img width="488" height="577" alt="Kullanıcı Giriş Ekranı" src="https://github.com/user-attachments/assets/366f0ba3-8a6a-412d-952c-5e43e2aedc6d" />
<img width="753" height="847" alt="kullanıcıgiriş" src="https://github.com/user-attachments/assets/58e658d1-4ecd-4378-81ae-bbe3162c8fed" />



---

## ⚙ Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/Emirkaraman9/digibank-smart-city.git
cd digibank-smart-city
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Required libraries:
- customtkinter  
- psutil  

### 3. Run the application

```bash
python main.py
```

---

## 🛡 Security & Simulation Notes

This project includes a **Defense Simulation Module**.

- The “Cyber Attack” button simulates a breach scenario  
- Used to test:
  - Logging system  
  - Notification threads  
  - System resilience  

### 🧪 Stress Testing

- A separate **Java Attack Bot** is included in `/tools`  
- Performs HTTP Flood simulation  
- Used to observe:
  - Load handling  
  - Thread stability  
  - Monitoring behavior  

---

## 🧠 Project Goals

- Demonstrate secure software design  
- Combine Smart City + FinTech concepts  
- Implement design patterns in real scenario  
- Build cyber-attack awareness  
- Practice multi-threaded architecture  

---

## 📝 License

This project was developed for **educational purposes only**.
