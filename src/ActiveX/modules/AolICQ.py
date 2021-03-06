# AOL ICQ ActiveX Arbitrary File Download and Execut
# CVE-2006-5650

import hashlib
import logging
log = logging.getLogger("Thug")

def DownloadAgent(self, url):
    log.ThugLogging.add_behavior_warn('[AOL ICQ ActiveX] Arbitrary File Download and Execute', 'CVE-2006-5650')
    log.ThugLogging.add_behavior_warn('[AOL ICQ ActiveX] Fetching from URL: %s' % (url, ))
    
    try:
        response, content = self._window._navigator.fetch(url)
    except:
        log.ThugLogging.add_behavior_warn('[AOL ICQ ActiveX] Fetch failed')
        return

    if response.status == 404:
        log.ThugLogging.add_behavior_warn("[AOL ICQ ActiveX] FileNotFoundError: %s" % (url, ))
        return 
 
    baseDir = log.baseDir

    md5 = hashlib.md5()
    md5.update(content)
    filename = md5.hexdigest()
    log.ThugLogging.add_behavior_warn("[AOL ICQ ActiveX] Saving File: " + filename)    

    with open(os.path.join(baseDir, filename), 'wb') as fd: 
        fd.write(content)

