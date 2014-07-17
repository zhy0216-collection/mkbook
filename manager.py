import time
import shutil

import click




@click.group()
def main():
    pass

@main.command()
@click.option("--port", default=5000, help="server port")
def server(port):
    import os, threading, SimpleHTTPServer, SocketServer, signal, sys
    from mkbook.config import OUTPUT_PATH
    # minimal web server.  serves files relative to the
    # current directory.
    os.chdir(OUTPUT_PATH)
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    SocketServer.TCPServer.allow_reuse_address = True
    httpd = SocketServer.TCPServer(("", port), Handler)
    thread = threading.Thread(target=httpd.serve_forever)
    thread.deamon = True
    thread.start()
    def stop_handler(signum, frame):
        httpd.shutdown()
        click.echo('exit')
        sys.exit(0)
    click.echo('server running on port {}...'.format(port))
    signal.signal(signal.SIGINT, stop_handler)
    click.echo('press CONTROL-C to stop the server')
    signal.pause()

@main.command()
@click.option("--display", default="flat", help="the book display form")
@click.option("--path", default="content/", help="the book content path")
def build(path, display):
    from mkbook.builder import FlatBuilder
    start_time = time.time() # seconds
    if display == "flat":
        builder = FlatBuilder(path)
    else:
        pass

    builder.build()
    hint_text = "Done in %s seconds"%(time.time() - start_time)
    click.echo(click.style(hint_text, fg="red"))


@main.command()
def dev():
    '''only for development env'''
    from mkbook.builder import FlatBuilder
    from mkbook.utils import force_copy
    start_time = time.time()
    builder = FlatBuilder(".")
    builder.build()

    force_copy("./mkbook/statics/bower_components", "./output/bower_components")
    shutil.copy("./mkbook/statics/mkbook-flat.js", "./output/")

    hint_text = "Done in %s seconds"%(time.time() - start_time)
    click.echo(click.style(hint_text, fg="red"))



if __name__ == "__main__":
    main()




