import os, sys
from twisted.web import static, server
# from multi_remote.gpio import GPIOHandler
# from multi_remote.service import Service

from twisted.python import log
from twisted.internet import reactor
from multi_remote.service import Service
from multi_remote.socket_server import ServerFactory, ServerProtocol

log.startLogging(sys.stdout)

Service(80).startService()

reactor.run()
