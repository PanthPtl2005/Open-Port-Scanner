# 🛰️ Network Monitor — Python Network Connection Logger

A lightweight, cross-platform **Python tool to monitor active TCP/UDP connections**.  
It displays process names, local and remote addresses, and connection status in a neat table — while also logging detailed events to a file for auditing.

---

## 🔧 Features

- Lists all active **TCP** and **UDP** connections.
- Shows **process names**, **local/remote IPs and ports**, and **statuses**.
- Generates detailed **logs** (INFO, DEBUG, CRITICAL, etc.).
- Detects **inaccessible processes** and handles exceptions gracefully.
- Outputs results in a **PrettyTable** for easy reading.
- Works on Windows, Linux, and macOS.

---

## 🧠 How It Works

1. Uses the `psutil` module to read system network connections.  
2. For each connection, it retrieves:
   - Protocol (`TCP` / `UDP`)
   - Local and Remote address pairs
   - Process name and PID (if accessible)
   - Connection status (LISTEN, ESTABLISHED, etc.)
3. Logs all operations to both the console and a file (`network_log.log`).
4. Displays the formatted output table using `PrettyTable`.

---

## 📦 Installation

### 1️⃣ Clone the repository and install the requirements
```bash
git clone https://github.com/PanthPtl2005/open-Port-Scanner.git
cd open-Port-Scanner
```
### 2️⃣ Create venv
```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```
### 3️⃣ Install requirements
```bash
pip install -r requirements.txt
```

### 4️⃣ Run python file using the below given command 
```bash
python open-port-viewer.py
```
### ‼(use sudo if you face any error related to administrative access)
```bash
sudo python open-port-viewer.py
```
---
### Example output
```bash
+-------+----------------+-------------------+-------------------+-------------+------+
| Proto | Process Name   | Local Address     | Remote Address    | Status      | PID  |
+-------+----------------+-------------------+-------------------+-------------+------+
| TCP   | chrome.exe     | 192.168.1.10:52345| 142.250.190.4:443 | ESTABLISHED | 4820 |
| UDP   | svchost.exe    | 0.0.0.0:68        |                   | NONE        | 1092 |
| TCP   | python.exe     | 127.0.0.1:8000    | 127.0.0.1:52544   | LISTEN      | 7180 |
+-------+----------------+-------------------+-------------------+-------------+------+
```
### Logging levels implemented
| Level        | Meaning                | Output             |
| ------------ | ---------------------- | ------------------ |
| **INFO**     | General status updates | Console + Log file |
| **DEBUG**    | Detailed debug info    | Log file only      |
| **WARNING**  | Non-critical errors    | Console + Log file |
| **CRITICAL** | Serious errors / exit  | Console + Log file |

### View your logs in network_log.log
```bash
network_log.log
```

### ⚠️ Disclaimer

This project is for educational and local network monitoring purposes only.
Do not use it to inspect, track, or analyze connections without proper authorization.

### 🧑‍💻 Author
Panth Patel - [GitHub](https://github.com/PanthPtl2005)

💬 Contributions, bug reports, and improvements are welcome!


