#!/bin/python

from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .mbio import MBIO

# import time
import time
import threading
import hashlib
import os
import pickle
from io import BytesIO

from prettytable import PrettyTable

from .items import Items
from .value import MBIOValues
from .config import MBIOConfig
from .xmlconfig import XMLConfig

from .value import MBIOValue, MBIOValueWritable, MBIOValueTrigger
from .value import MBIOValueDigital, MBIOValueDigitalWritable
from .value import MBIOValueMultistate, MBIOValueMultistateWritable


class MBIOTask(object):
    STATE_HALT = 0
    STATE_POWERON = 1
    STATE_RUN = 2
    STATE_POWEROFF = 3
    STATE_ERROR = 4

    def initName(self):
        return 'task%d' % self._parent.tasks.count()

    def __init__(self, parent: MBIO, name, xml: XMLConfig = None):
        self._parent=parent
        if not name:
            name=self.initName()
        self._name=str(name).lower()
        self._key='%s' % self._name
        self._state=self.STATE_HALT
        self._error=False
        self._timeoutState=0
        self._values=MBIOValues(self, self._key, self.logger)
        self._eventReset=threading.Event()
        self._eventStop=threading.Event()
        self._eventHalt=threading.Event()
        self._eventWakeup=threading.Event()
        self._parent.declareTask(self)
        # FIXME: daemon=True ?
        self._thread=threading.Thread(target=self.manager)
        self.logger.info("Starting TASK:%s" % self._key)

        self._config=MBIOConfig()

        self.onInit()
        self.load(xml)

        self._thread.start()

    @property
    def parent(self) -> MBIO:
        return self._parent

    def getMBIO(self) -> MBIO:
        return self._parent

    @property
    def config(self) -> MBIOConfig:
        return self._config

    @property
    def logger(self):
        return self._parent.logger

    @property
    def key(self):
        return self._key

    @property
    def name(self):
        return self._name

    @property
    def values(self):
        return self._values

    def value(self, name, unit=None, default=None, writable=False, resolution=0.1, commissionable=False):
        key=self.values.computeValueKeyFromName(name)
        value=self.values.item(key)
        if not value:
            if writable:
                value=MBIOValueWritable(self.values, name, unit=unit, default=default, resolution=resolution, commissionable=commissionable)
            else:
                value=MBIOValue(self.values, name, unit=unit, default=default, resolution=resolution, commissionable=commissionable)
        return value

    def valueDigital(self, name, default=None, writable=False, commissionable=False):
        key=self.values.computeValueKeyFromName(name)
        value=self.values.item(key)
        if not value:
            if writable:
                value=MBIOValueDigitalWritable(self.values, name, default=default, commissionable=commissionable)
            else:
                value=MBIOValueDigital(self.values, name, default=default, commissionable=commissionable)
        return value

    def valueMultistate(self, name, vmax, vmin=0, default=None, writable=False, commissionable=False):
        key=self.values.computeValueKeyFromName(name)
        value=self.values.item(key)
        if not value:
            if writable:
                value=MBIOValueMultistateWritable(self.values, name, vmax, vmin, default=default, commissionable=commissionable)
            else:
                value=MBIOValueMultistate(self.values, name, vmax, vmin, default=default, commissionable=commissionable)
        return value

    def valueTrigger(self, name, delay=5, commissionable=False):
        key=self.values.computeValueKeyFromName(name)
        value=self.values.item(key)
        if not value:
            value=MBIOValueTrigger(self.values, name, delay, commissionable=commissionable)
        return value

    def onInit(self):
        pass

    def onLoad(self, xml: XMLConfig):
        pass

    def load(self, xml: XMLConfig):
        if xml:
            try:
                self.onLoad(xml)
            except:
                self.logger.exception('Task %s:load()' % self.name)

    def isHalted(self):
        if self.state==self.STATE_HALT:
            return True
        return False

    def isError(self):
        if self._error:
            return True
        return False

    def stop(self):
        self._eventStop.set()
        self._eventWakeup.set()

    def halt(self):
        self._eventHalt.set()
        self._eventWakeup.set()

    def reset(self):
        self._eventHalt.clear()
        self._eventReset.set()
        self._eventWakeup.set()

    def waitForThreadTermination(self):
        self.stop()
        self._thread.join()

    def sleep(self, delay=1):
        try:
            if self._eventStop.is_set():
                return True
            return self._eventWakeup.wait(delay)
        except:
            pass

    def microsleep(self):
        self.sleep(0.001)

    def poweron(self) -> bool:
        # to be overriden
        return True

    def poweroff(self) -> bool:
        # to be overriden
        return True

    def run(self) -> float:
        # to be overriden
        return 5.0

    @property
    def state(self):
        return self._state

    def statestr(self):
        states=['HALT', 'POWERON', 'RUN', 'POWEROFF', 'ERROR']
        try:
            return states[self.state]
        except:
            pass
        return 'UNKNOWN:%d' % self._state

    def timeout(self, delay):
        return time.time()+delay

    def isTimeout(self, t):
        if time.time()>=t:
            return True
        return False

    def timeToTimeout(self, timeout):
        return max(0, timeout-time.time())

    def manager(self):
        while not self._eventStop.is_set():
            try:
                self._state=self.STATE_HALT
                if self._eventHalt.is_set():
                    self.sleep(0.5)
                    continue
                self._eventReset.clear()
                self.logger.info("TASK:%s poweron()" % self._key)
                self._state=self.STATE_POWERON
                if self.poweron():
                    self._state=self.STATE_RUN
                    timeout=0.1
                    while True:
                        if timeout is None:
                            timeout=5.0
                        self._eventWakeup.clear()
                        self.sleep(timeout)
                        # self.logger.warning('%s:run()' % self.key)
                        timeout=self.run()

                        if self._eventStop.is_set() or self._eventHalt.is_set():
                            self.logger.info("TASK:%s poweroff()" % self._key)
                            self._state=self.STATE_POWEROFF
                            self.poweroff()
                            break
                        elif self._eventReset.is_set():
                            break
                        self._error=False
                else:
                    self._state=self.STATE_ERROR
            except:
                self.logger.exception("TASK:%s manager()" % self._key)
                self._state=self.STATE_ERROR

            if self._state==self.STATE_ERROR:
                self._error=True
                timeout=self.timeout(15)
                while not self._eventStop.is_set():
                    if self._eventReset.is_set() or self.isTimeout(timeout):
                        break
                    if self._eventHalt.is_set():
                        break
                    self.sleep(0.5)

        self.logger.info("TASK:%s done" % self._key)

    def __repr__(self):
        return '%s(%s, %s)' % (self.__class__.__name__, self.key, self.statestr())

    def registerValue(self, value):
        self.parent.registerValue(value)

    def signalSync(self):
        # to be overriden
        self._eventWakeup.set()

    def getLocalDataStorageFilePath(self, dataname):
        fname='%s.%s.dat' % (dataname, self.name)
        return os.path.join(self.getMBIO().rootPath() or '.', fname)

    def computeDataHashCodeForFile(self, f):
        try:
            return hashlib.file_digest(f, 'sha256').hexdigest()
        except:
            pass

    def getLocalDataStorageHashCode(self, dataname):
        try:
            fpath=self.getLocalDataStorageFilePath(dataname)
            with open(fpath, 'rb', buffering=0) as f:
                return self.computeDataHashCodeForFile(f)
        except:
            pass

    def checkLocalDataStorageHashCode(self, dataname, hcode):
        if hcode:
            if hcode==self.getLocalDataStorageHashCode(dataname):
                return True
        return False

    def updateLocalDataStorage(self, dataname, data):
        try:
            fpath=self.getLocalDataStorageFilePath(dataname)
            self.logger.warning('%s(%s)->updateLocalDataStorage(%s)' % (self.__class__.__name__, self.name, fpath))
            with open(fpath, 'wb') as f:
                f.write(data)
                return True
        except:
            pass

    def getLocalDataStorageContent(self, dataname, binary=True):
        try:
            mode='r'
            if binary:
                mode='rb'
            with open(self.getLocalDataStorageFilePath(dataname), mode) as f:
                data=f.read()
                return data
        except:
            pass

    def pickleWrite(self, dataname, data):
        if dataname and data:
            buf=BytesIO()
            try:
                pickle.dump(data, buf)
                buf.seek(0)
                hcode=self.computeDataHashCodeForFile(buf)
                if not self.checkLocalDataStorageHashCode(dataname, hcode):
                    self.logger.info('%s(%s) updating localDataStorage %s' % (self.__class__.__name__, self.name, dataname))
                    buf.seek(0)
                    with open(self.getLocalDataStorageFilePath(dataname), 'wb') as f:
                        f.write(buf.read())
                buf.close()
                return True
            except:
                self.logger.exception('x')
                pass
        return False

    def pickleRead(self, dataname):
        try:
            with open(self.getLocalDataStorageFilePath(dataname), 'rb') as f:
                return pickle.load(f)
        except:
            pass

    def dump(self):
        t=PrettyTable()
        t.field_names=['Property', 'Value']
        t.align='l'

        t.add_row(['key', self.key])
        t.add_row(['state', self.statestr()])

        for value in self.values:
            t.add_row([value.key, str(value)])

        print(t.get_string())


class MBIOTasks(Items):
    def __init__(self, logger):
        super().__init__(logger)
        self._items: list[MBIOTask]=[]
        self._itemByKey={}
        self._itemByName={}

    def item(self, key):
        item=super().item(key)
        if item:
            return item

        item=self.getByKey(key)
        if item:
            return item

        item=self.getByName(key)
        if item:
            return item

    def countByType(self, ref):
        count=0
        for task in self._items:
            if isinstance(task, ref):
                count+=1
        return count

    def add(self, item: MBIOTask) -> MBIOTask:
        if isinstance(item, MBIOTask):
            super().add(item)
            self._itemByName[item.name]=item
            self._itemByKey[item.key]=item

    def getByName(self, name):
        try:
            return self._itemByName[name]
        except:
            pass

    def getByKey(self, key):
        try:
            return self._itemByKey[key]
        except:
            pass

    def stop(self):
        for item in self._items:
            item.stop()

    def reset(self):
        for item in self._items:
            item.reset()

    def halt(self):
        for item in self._items:
            item.halt()

    def resetHalted(self):
        for item in self._items:
            if item.isHalted():
                item.reset()

    def waitForThreadTermination(self):
        for item in self._items:
            item.waitForThreadTermination()


if __name__=='__main__':
    pass
