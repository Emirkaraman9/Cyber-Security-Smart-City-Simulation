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

<img width="1377" height="801" alt="Ana Giriş Ekranı" src="https://github.com/user-attachments/assets/50d4bc4b-4815-4261-a34d-e27e9bc00a80" />
<img width="876" height="602" alt="Kullanıcı Giriş Ekranı" src="https://github.com/user-attachments/assets/e442002e-f40c-430b-bf37-a4ef3fedf77b" />
<img width="1882" height="812" alt="Kullanıcı Panel Ekranı" src="https://github.com/user-attachments/assets/4fa33c0c-e257-4121-a309-54c1da0294fb" />
<img width="426" height="283" alt="Üye Arama Ekranı" src="https://github.com/user-attachments/assets/4f161b09-7385-452e-a523-ae02921b46c9" />
<img width="520" height="427" alt="Üye Ekleme Ekranı" src="https://github.com/user-attachments/assets/cf54a458-2101-4c32-8bef-b95efe31d10a" />
<img width="1197" height="831" alt="Yönetici giriş ekranı " src="https://github.com/user-attachments/assets/64f13a20-f424-416e-a27f-609c6ea5e52b" />
<img width="430" height="518" alt="Yönetici Giriş Ekranı 1" src="https://github.com/user-attachments/assets/3cc978fd-a302-4d42-8327-544c7f348407" />
<img width="1880" height="851" alt="Yönetici Paneli 2" src="https://github.com/user-attachments/assets/fb297a5e-e51a-43d3-b8b7-dfdfd58e8582" />



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
