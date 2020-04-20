# If you don't close, you can lose data!
#
# f = open(...)
# working
# f.close()
#
#
# with-block
#
# - Control flow structure for managing resources
# - Can be used with any objects - such as files - which
#   supper the context-manager protocol

# Using with in read_series()

def read_series(filename):
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]
##########################
#
#
# Expansion of the with-block
#
# with EXPR as VAR:
#    BLOCK
#
#
# mgr = (EXPR)
#    exit = type(mgr).__exit__
#    value = type(mgr).__enter__(mgr)
#    exc = True
#    try:
#        try:
#            VAR = value
#            BLOCK
#        except:
#            exc = False
#            if not exit(mgr, *sys.exc_info()):
#                raise
#        finally:
#            if exc:
#                exit(mgr, None, None, None)
##################################
