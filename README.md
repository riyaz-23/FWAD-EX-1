
EX-1 Developing a Simple Webserver

Date:

AIM:

To develop a simple webserver to serve html pages and display the Windows Specifications of your Laptop.

DESIGN STEPS:

Step 1:
HTML content creation.

Step 2:
Design of webserver workflow.

Step 3:
Implementation using Python code.

Step 4:
Import the necessary modules.

Step 5:
Define a custom request handler.

Step 6:
Start an HTTP server on a specific port.

Step 7:
Run the Python script to serve web pages.

Step 8:
Serve the HTML pages.

Step 9:
Start the server script and check for errors.

Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

PROGRAM:

index.html 


```<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>TCP/IP Explained</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>

  <header class="hero">
    <h1>TCP/IP Explained</h1>
    <p>The rules that let every device on the internet talk to each other.</p>
    <nav>
      <a href="#what">What is it?</a>
      <a href="#layers">Layers</a>
      <a href="#handshake">Handshake</a>
      <a href="#ip">IP Address</a>
      <a href="#compare">TCP vs UDP</a>
    </nav>
  </header>

  <main>

    <section id="what">
      <h2>What is TCP/IP?</h2>
      <p>
        <strong>TCP/IP</strong> is a set of communication rules (a protocol suite) used on the internet.
        <strong>IP</strong> (Internet Protocol) gets data to the right address.
        <strong>TCP</strong> (Transmission Control Protocol) makes sure the data arrives complete and in order.
      </p>
      <div class="note">
        Think of sending a parcel: <b>IP</b> is the address on the box, and <b>TCP</b> is the tracking that
        confirms every box arrived and was opened in the right order.
      </div>
    </section>

    <section id="layers">
      <h2>The 4 Layers</h2>
      <p>Data passes through four layers, from your app down to the cable.</p>
      <div class="stack">
        <div class="layer l4">
          <h3>4. Application</h3>
          <p>What you use: HTTP, HTTPS, DNS, FTP, SMTP</p>
        </div>
        <div class="layer l3">
          <h3>3. Transport</h3>
          <p>Splits data into segments: TCP or UDP, using port numbers</p>
        </div>
        <div class="layer l2">
          <h3>2. Internet</h3>
          <p>Adds IP addresses and finds a route: IP, ICMP</p>
        </div>
        <div class="layer l1">
          <h3>1. Network Access</h3>
          <p>Sends bits over the wire or Wi-Fi: Ethernet, MAC address</p>
        </div>
      </div>
    </section>

    <section id="handshake">
      <h2>TCP Three-Way Handshake</h2>
      <p>Before sending data, TCP sets up a connection in three steps.</p>
      <div class="steps">
        <div class="step">
          <span class="num">1</span>
          <h3>SYN</h3>
          <p>Client: "I want to connect."</p>
        </div>
        <div class="arrow">&rarr;</div>
        <div class="step">
          <span class="num">2</span>
          <h3>SYN-ACK</h3>
          <p>Server: "OK, I'm ready too."</p>
        </div>
        <div class="arrow">&rarr;</div>
        <div class="step">
          <span class="num">3</span>
          <h3>ACK</h3>
          <p>Client: "Great, connected!"</p>
        </div>
      </div>
    </section>

    <section id="ip">
      <h2>IP Addresses</h2>
      <p>Every device on a network needs an IP address, like a house number for data.</p>
      <table>
        <thead>
          <tr><th>Type</th><th>Example</th><th>Notes</th></tr>
        </thead>
        <tbody>
          <tr><td>IPv4</td><td><code>192.168.1.10</code></td><td>32 bits, four numbers from 0 to 255</td></tr>
          <tr><td>IPv6</td><td><code>2001:db8::1</code></td><td>128 bits, far more addresses</td></tr>
          <tr><td>Localhost</td><td><code>127.0.0.1</code></td><td>Your own computer (the address our server uses)</td></tr>
        </tbody>
      </table>
    </section>

    <section id="compare">
      <h2>TCP vs UDP</h2>
      <div class="cards">
        <div class="card">
          <h3>TCP</h3>
          <ul>
            <li>Connection-based</li>
            <li>Reliable, ordered delivery</li>
            <li>Slower, with more overhead</li>
            <li>Used for web pages, email, file transfer</li>
          </ul>
        </div>
        <div class="card">
          <h3>UDP</h3>
          <ul>
            <li>Connectionless</li>
            <li>No delivery guarantee</li>
            <li>Faster, with less overhead</li>
            <li>Used for video calls, gaming, streaming</li>
          </ul>
        </div>
      </div>
    </section>

  </main>

  <footer>
    <p>Served by a Python web server &middot; HTML + CSS + Python</p>
  </footer>

</body>
</html>
```
server.py


```
"""A tiny web server that serves the files in this folder.

Run it with:   python server.py
Then open:     http://localhost:8000
Stop it with:  Ctrl + C
"""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HOST = "127.0.0.1"   # localhost: only this computer can connect
PORT = 8000          # the "door number" the server listens on


class MyHandler(SimpleHTTPRequestHandler):
    """Handles each browser request. Serves index.html for '/'."""

    def log_message(self, format, *args):
        # Print a short line for every request so you can watch the traffic
        print(f"Request from {self.client_address[0]}: {self.path}")


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), MyHandler)
    print(f"Server running at http://localhost:{PORT}  (Ctrl + C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()
```

style.css

```
/* ---------- Basics ---------- */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: "Segoe UI", Arial, sans-serif;
  line-height: 1.6;
  color: #1f2937;
  background: #f3f4f6;
}

/* ---------- Header ---------- */
.hero {
  background: linear-gradient(135deg, #1e3a8a, #2563eb);
  color: white;
  text-align: center;
  padding: 60px 20px 30px;
}

.hero h1 {
  font-size: 2.6rem;
  margin-bottom: 10px;
}

.hero p {
  font-size: 1.1rem;
  opacity: 0.9;
}

nav {
  margin-top: 28px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
}

nav a {
  color: white;
  text-decoration: none;
  padding: 8px 16px;
  border: 1px solid rgba(255, 255, 255, 0.5);
  border-radius: 20px;
  transition: background 0.2s;
}

nav a:hover {
  background: rgba(255, 255, 255, 0.2);
}

/* ---------- Sections ---------- */
main {
  max-width: 900px;
  margin: 30px auto;
  padding: 0 20px;
}

section {
  background: white;
  padding: 28px;
  margin-bottom: 24px;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.07);
}

section h2 {
  color: #1e3a8a;
  margin-bottom: 12px;
}

.note {
  margin-top: 14px;
  padding: 14px;
  background: #eff6ff;
  border-left: 4px solid #2563eb;
  border-radius: 6px;
}

/* ---------- Layers ---------- */
.stack {
  margin-top: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.layer {
  padding: 14px 18px;
  border-radius: 8px;
  color: white;
}

.layer h3 {
  font-size: 1.05rem;
}

.l4 { background: #2563eb; }
.l3 { background: #7c3aed; }
.l2 { background: #db2777; }
.l1 { background: #ea580c; }

/* ---------- Handshake ---------- */
.steps {
  margin-top: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
}

.step {
  flex: 1;
  min-width: 150px;
  text-align: center;
  padding: 16px;
  border: 2px solid #2563eb;
  border-radius: 10px;
}

.num {
  display: inline-block;
  width: 30px;
  height: 30px;
  line-height: 30px;
  border-radius: 50%;
  background: #2563eb;
  color: white;
  font-weight: bold;
  margin-bottom: 6px;
}

.arrow {
  font-size: 1.8rem;
  color: #2563eb;
}

/* ---------- Table ---------- */
table {
  width: 100%;
  margin-top: 14px;
  border-collapse: collapse;
}

th, td {
  text-align: left;
  padding: 10px 12px;
  border-bottom: 1px solid #e5e7eb;
}

th {
  background: #eff6ff;
  color: #1e3a8a;
}

code {
  background: #f3f4f6;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: Consolas, monospace;
}

/* ---------- Cards ---------- */
.cards {
  margin-top: 14px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
}

.card {
  padding: 18px;
  border: 1px solid #e5e7eb;
  border-radius: 10px;
}

.card h3 {
  color: #2563eb;
  margin-bottom: 8px;
}

.card ul {
  padding-left: 20px;
}

/* ---------- Footer ---------- */
footer {
  text-align: center;
  padding: 24px;
  color: #6b7280;
}
```



"""A tiny web server that serves the files in this folder.

Run it with:   python server.py
Then open:     http://localhost:8000
Stop it with:  Ctrl + C
"""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HOST = "127.0.0.1"   # localhost: only this computer can connect
PORT = 8000          # the "door number" the server listens on


class MyHandler(SimpleHTTPRequestHandler):
    """Handles each browser request. Serves index.html for '/'."""

    def log_message(self, format, *args):
        # Print a short line for every request so you can watch the traffic
        print(f"Request from {self.client_address[0]}: {self.path}")


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), MyHandler)
    print(f"Server running at http://localhost:{PORT}  (Ctrl + C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        server.server_close()

style.css















OUTPUT:
<img width="1917" height="938" alt="Screenshot 2026-11-24 084321" src="https://github.com/user-attachments/assets/f04397df-3634-45c8-bbe6-00c77c5bae2e" />

RESULT:

The program for implementing simple webserver is executed successfully.
