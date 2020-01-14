import os
import sys
sys.path.append(os.path.abspath('../FlairTestBed/'))
import module_CommonResource

print "LOG: Start of the test suite"
link = module_CommonResource.selectDevOrProd()
module_CommonResource.openChrome()
module_CommonResource.openFlair3DAndLogin(link)
Debug.log("TEST PASSED!!")