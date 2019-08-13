import logging
from tornado.ioloop import IOLoop
from tornado import gen
from tornado.iostream import StreamClosedError
from tornado.tcpserver import TCPServer
from tornado.options import options, define

define("port", default=9888, help="TCP port to listen on")
logger = logging.getLogger(__name__)

class EchoServer(TCPServer):
    @gen.coroutine
    def handle_stream(self, steam, address):
        while True:
            try:
                data = yield steam.read_until(b"\n")
                logger.info("Received bytes: %s", data)
                if not data.endswith(b"\n"):
                    data = data + b'\n'
                yield steam.write(data)
            except StreamClosedError:
                logger.warning("Lost Client at host %s", address[0])
                break
            except Exception as e:
                print(e)

if __name__ == '__main__':
    options.parse_command_line()
    server = EchoServer()
    server.listen(options.port)
    logger.info("Listening on TCP port %d", options.port)
    IOLoop.current().start()
