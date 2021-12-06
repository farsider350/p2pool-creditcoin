import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f1c117dc'.decode('hex')
P2P_PORT = 6666
ADDRESS_VERSION = 28
RPC_PORT = 9332
RPC_CHECK =RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
#            'creditcoin' in (yield bitcoind.rpc_help()) 
            (yield helper.check_block_header(bitcoind, 'd3602f1423e127f8f1755de875f48edb6bbf5c4b1306dd4c6df85af344def718')) and
                          (yield bitcoind.rpc_getblockchaininfo())['chain'] == 'main'
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'CRED'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'credits') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/credits/') if platform.system() == 'Darwin' else os.path.expanduser('~/.credits'), 'credits.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://'
ADDRESS_EXPLORER_URL_PREFIX = 'https://'
TX_EXPLORER_URL_PREFIX = 'https://'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
