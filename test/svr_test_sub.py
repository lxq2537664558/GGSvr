# coding:utf-8
import gnet
import prt_test_game
import time

def init ():
    reg()


def reg():
    gnet.reg(prt_test_game.TEST_SUB, on_test_sub)


def on_test_sub(data):
    print "on_test_sub", data
    
    conn_id = data[0]
    msg = data[1]

    time.sleep(1)
    print "sleep 1"
    time.sleep(1)
    print "sleep 1"
    time.sleep(1)
    print "sleep 1"

    gnet.sendm([prt_test_game.TEST_SUB, "sub -> main"])


def remote_call_test(*arg, **kwds):
    print "svr_test_sub>remote_call_test"
    print "*arg:", arg
    print "**kwds", kwds
    return ["this is test data", 1,2,3,4, [1,2,3,4]]
