from base import *
from devices import *
import time

class XplainedProSamG55(Board):
    ids_vendor = {
        "03EB":frozenset(("2111",))
    }

    @staticmethod
    def match(dev):
        return dev["vid"] in XplainedProSamG55.ids_vendor and dev["pid"] in XplainedProSamG55.ids_vendor[dev["vid"]]

    def reset(self):
        # hack to reset
        proc.runcmd("edbg_l21", "-F", "r,1,1", "-t", "atmel_cm4")

    def burn(self,bin,outfn=None):
        fname = fs.get_tempfile(bin)
        outfn(fname)
        res,out,err= proc.runcmd("edbg", "-ebpv", "-t", "atmel_cm4","-s",self.sid,"-f", fname,outfn=outfn)
        fs.del_tempfile(fname)
        if res:
            return False,out
        return True,out