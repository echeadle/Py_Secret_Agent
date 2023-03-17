import hashlib
md5 = hashlib.new("md5")
with open( "LHD_warship.jpg", "rb" ) as some_file:
    md5.update( some_file.read() )
print( f"MD5 : {md5.hexdigest()}" )

import hmac
with open( "LHD_warship.jpg", "rb" ) as some_file:
    keyed= hmac.new( b"Agent Garbo", some_file.read(), digestmod=hashlib.sha256 )
print(f"\n HMAC :  {keyed.hexdigest()}" )
