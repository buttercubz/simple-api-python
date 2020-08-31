from server import Server

api = Server(debug=True, port=4000)

if __name__ == "__main__":
    api.start()
