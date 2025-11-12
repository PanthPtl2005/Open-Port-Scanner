import psutil
import socket
import logging
from prettytable import PrettyTable

logger = logging.getLogger("NetworkMonitor")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("network_log.log")
file_handler.setLevel(logging.DEBUG)   # Log everything to file

file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  #to prevent showing DEBUG in console

console_format = logging.Formatter('%(levelname)s: %(message)s')
console_handler.setFormatter(console_format)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Network Monitor started.")

table = PrettyTable()
table.field_names = ["Proto", "Process Name", "Local Address", "Remote Address", "Status", "PID"]

try:
    logger.debug("Attempting to fetch active network connections using psutil.")
    
    connections = psutil.net_connections(kind='inet')
    
    #triggering critical logging level
    # connections = psutil.net_connections = lambda kind=None: (_ for _ in ()).throw(RuntimeError("Simulated critical failure"))

    if not connections:
        logger.critical("No active network connections found. Critical failure for network monitoring.")
        raise SystemExit("Exiting due to critical error: No active connections.")
    logger.info(f"Fetched {len(connections)} active connections successfully.")
except Exception as e:
    logger.critical(f"Failed to fetch network connections: {e}")
    raise SystemExit("Exiting due to critical error during initialization.")

for idx, conn in enumerate(connections, start=1):
    try:
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else ""
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else ""
        proto = "TCP" if conn.type == socket.SOCK_STREAM else "UDP"
        pid = conn.pid if conn.pid else "-"

        logger.debug(f"[{idx}] Proto={proto}, Local={laddr}, Remote={raddr}, PID={pid}")

        if pid != "-":
            try:
                pname = psutil.Process(pid).name()
            except (psutil.AccessDenied, psutil.NoSuchProcess) as ex:
                pname = "Access Denied"
                logger.warning(f"Could not access process name for PID {pid}: {ex}")
        else:
            pname = "-"

        table.add_row([proto, pname, laddr, raddr, conn.status, pid])

    except Exception as loop_error:
        logger.error(f"Error while processing connection #{idx}: {loop_error}")

logger.info("All connections processed successfully. Printing table below.")
print(table)
logger.info("Network Monitor finished execution.")



