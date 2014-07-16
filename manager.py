import click




@click.group()
def main():
    pass

@main.command()
@click.option("--port", default=5000, help="server port")
def server(port):
    import threading, SimpleHTTPServer, SocketServer, signal
    # minimal web server.  serves files relative to the
    # current directory.
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", port), Handler)
    thread = threading.Thread(target=httpd.serve_forever)
    thread.deamon = True
    thread.start()
    def stop_handler(signum, frame):
        httpd.shutdown()
        click.echo('exit')
    click.echo('server running on port {}...'.format(port))
    signal.signal(signal.SIGINT, stop_handler)
    click.echo('press CONTROL-C to stop the server')
    signal.pause()





if __name__ == "__main__":
    main()
