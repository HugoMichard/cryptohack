import pem
import base64

file = './privacy_enhanced_mail.pem'
parsed = pem.parse_file(file)
print(parsed[0])
file_content = str(parsed[0])
file_content = file_content.replace("-----BEGIN RSA PRIVATE KEY-----", "")
file_content = file_content.replace("-----END RSA PRIVATE KEY-----", "")
file_content = base64.b64decode(file_content.encode("utf-8"))
print(file_content)
file_content = bytes.hex(file_content)
print(file_content)
