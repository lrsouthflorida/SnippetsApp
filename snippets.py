import logging 

# Set the log output file, the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name, snipett):
    """
    Store a snipett with an associated name.
    
    Returns the name and the snipett
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet
    
def get(name):
    """Retrieve the snippet with a given name.
    
    If there is no such snippet, return '404: Snippet Not Found'.
    
    Returns the snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""
    
    
    
    