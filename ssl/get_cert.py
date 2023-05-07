import subprocess

# Run the OpenSSL command and capture the output
command = 'openssl s_client -showcerts -connect DESKTOP-50I8Q5J:12345 2>nul | openssl x509 -outform PEM'
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()

# Write the output to a file
with open("server.crt", "wb") as f:
    f.write(output)