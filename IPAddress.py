class IPAddress:
  # Construct a new IP Address from the provided bytes
  def __init__(self, bytes):
    pass
  
  def getByte(self, index):
    return 1

  # determine if this IP Address is equal to another
  # Return false (don't raise an exception) if the other
  # value is not an IP Address
  def __eq__(self, other):
    return False 

  # Compare this IP Address to another IP Address.  Raise
  # An exception if the other value is not an IP Address
  def __cmp__(self, other):
    return -1

if __name__ == "__main__":
  ip = IPAddress([1,2,3]);
  print(ip)
 
