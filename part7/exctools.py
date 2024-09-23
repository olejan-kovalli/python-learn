import sys 
import traceback

def safe(func, *pargs, **kargs):
    try: 
        func(*pargs, **kargs)
    except Exception:        
        print(sys.exc_info())
        traceback.print_exc()