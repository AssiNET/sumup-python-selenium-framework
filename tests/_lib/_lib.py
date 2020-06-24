import urllib
import os
import datetime
import logging
logging.basicConfig(format='%(message)s',level=logging.INFO)


class UIActions(object):
    @classmethod
    def ClearClipboard(cls):
        from java.awt.datatransfer import StringSelection
        from java.awt import Toolkit
        toolkit = Toolkit.getDefaultToolkit()
        clipboard = toolkit.getSystemClipboard()
        clipboard.setContents(StringSelection(""), None)

class Network(object):
    @classmethod
    def DownloadFile(cls, download_url, destination):
        try:
            if os.path.exists(destination):
                os.remove(destination)

            urllib.urlretrieve(download_url, destination)
        except Exception as ex:
            print("Download failed!")
            print("Exception: " + str(ex))

class String(object):
    @classmethod
    def RemoveNonASCIIchar(cls, text):
        '''Removes chars>128'''
        if isinstance(text, (int, long)):
            text = str(text)
        return "".join(i for i in text if ord(i) < 128)

class Reporting(object):
    @classmethod
    def TestLog(cls, message):
        '''Print info in the Report.html, Console and Jenkins output'''
        label_timestamp = "[" + datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S] TEST_LOG: ')

        # print in console and Jenkins
        message_console_jenkins = str(label_timestamp) + str(message)
        logging.info(message_console_jenkins)
        
        # print in Report.html
        message_report_html = str(label_timestamp) + String.RemoveNonASCIIchar(message)
        print(message_report_html)
