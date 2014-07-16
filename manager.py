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

@main.command()
@click.option("--display", default="flat", help="the book display form")
@click.option("--path", default="content/", help="the book content path")
def build(path, display):
    import time
    from mkbook.builder import FlatBuilder
    start_time = time.time() # seconds
    if display == "flat":
        builder = FlatBuilder(path)
    else:
        pass

    builder.build()
    hint_text = "Done in %s seconds"%(time.time() - start_time)
    click.echo(click.style(hint_text, fg="red"))


if __name__ == "__main__":
    main()




