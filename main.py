from socket import *

serverPort = 2144  # server port number, student ID=1222144 the port number =2144
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('', serverPort))  # now the socket is specified with a specific network interface and port number. (port and ip)
server_socket.listen(1)  # 1 connection can be queued before the server starts refusing new connections.
print("Server is ready")  # the server now starts to listen  for any requests!

while True:
    print("Waiting to connect")
    connection_socket, address = server_socket.accept()  # when the client sends a tcp connection, request created "connection_socket"
    print(f"HTTP request from: {address}")
    try:
        message = connection_socket.recv(1024).decode()  # receive and decode data
        client_ip = address[0]
        client_port = address[1]

        lines = message.split('\n')
        object = lines[0].split()[1]

        print("\nHTTP REQUEST IS:\n", message)

        # when user searches localhost:2144/ or localhost:2144/index.html or localhost:2144/en or localhost:2144/main_en.html
        # I have to display him/her the english version site

        if object in ['/', '/index.html', '/main_en.html', '/en']:
            connection_socket.send("HTTP/1.1 200 OK\r\n".encode())
            connection_socket.send("Content-Type: text/html;charset=UTF-8\r\n".encode())
            connection_socket.send("\r\n".encode())
            with open("main_en.html", "rb") as file1:
                connection_socket.send(file1.read())

        elif object == '/ar':  # if user searched localhost:2144/ar
            connection_socket.send("HTTP/1.1 200 OK\r\n".encode())
            connection_socket.send("Content-Type: text/html;charset=UTF-8\r\n".encode())
            connection_socket.send("\r\n".encode())
            with open("main_ar.html", "rb") as file2:
                connection_socket.send(file2.read())

        elif object.endswith(".html"):
            connection_socket.send("HTTP/1.1 200 OK\r\n".encode())
            connection_socket.send("Content-Type: text/html;charset=UTF-8\r\n".encode())
            connection_socket.send("\r\n".encode())
            with open("mysite0515.html", "rb") as s:
                connection_socket.send(s.read())

        elif object.endswith(".css"):
            connection_socket.send("HTTP/1.1 200 OK\r\n".encode())
            connection_socket.send("Content-Type: text/css;charset=UTF-8\r\n".encode())
            connection_socket.send("\r\n".encode())
            with open("CSS/main.css", "rb") as f:
                connection_socket.send(f.read())

        elif object.endswith(
                '.jpg'):  # if user searched for an image ends with .jpg i will response with young_Raheeq.jpg
            # note: i just have one jpg pictures
            connection_socket.send("HTTP/1.1 200 OK\r\n".encode())
            connection_socket.send("Content-Type: image/jpeg\r\n".encode())
            connection_socket.send("\r\n".encode())
            with open("Images/young_Raheeq.jpg", "rb") as f3:
                connection_socket.send(f3.read())

        elif object.endswith('.png'):
            # if user searched for an image ends with .png i will response with Birzeit_University_logo.png
            # note: i just have one png pictures
            connection_socket.send("HTTP/1.1 200 OK\r\n".encode())
            connection_socket.send("Content-Type: image/png\r\n".encode())
            connection_socket.send("\r\n".encode())
            with open("Images/Bizeit_University_logo.png", "rb") as f3:
                connection_socket.send(f3.read())

        elif object == '/so':  # if user searched for localhost:2144/so  i will open stackoverflow for him on his webpage
            connection_socket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            connection_socket.send("Location: https://stackoverflow.com\r\n".encode())
            connection_socket.send("\r\n".encode())

        elif object == '/itc' or object == '/itc/':  # if user searched for localhost:2144/itc or localhost:2144/itc/
            connection_socket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
            connection_socket.send("Location: https://itc.birzeit.edu\r\n".encode())
            connection_socket.send("\r\n".encode())

        else:  # if the user searched for a file that is not found
            connection_socket.send("HTTP/1.1 404 Not Found\r\n".encode())
            connection_socket.send("Content-Type: text/html;charset=UTF-8\r\n".encode())
            connection_socket.send("\r\n".encode())
            not_found = f"""<html>
                                <head><title>Error 404</title></head>
                                <body>
                                    <h2 style="color:blue;">The file is not found</h2>
                                    <p style="font-weight:bold;">Raheeq Mousa, ID: 1220515</p>
                                    <p style="font-weight:bold;">Aya Assi, ID: 1220794</p>
                                    <p style="font-weight:bold;">Sadeel Nidal, ID: 1222144</p>
                                    <p>IP Address: {client_ip}</p>
                                    <p>Port Number: {client_port}</p>
                                </body>
                            </html>"""
            connection_socket.send(not_found.encode())

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection_socket.close()