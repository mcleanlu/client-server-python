# Generating SSL/TLS Certificate and Key Files Using OpenSSL

1. Install OpenSSL on your machine. You can download OpenSSL from the [official website](https://www.openssl.org/source/).

2. Open a command prompt or terminal window and navigate to the directory where you want to generate the files.

3. Generate the private key file using the following command:

   ```bash
   openssl genpkey -algorithm RSA -out server.key

4. Generate the certificate signing request (CSR) file using the following command:

    ```bash
    openssl req -new -key server.key -out server.csr

This command generates a CSR file named server.csr based on the private key file generated in the previous step.

5. Generate the SSL/TLS certificate file using the following command:

    ```bash
    openssl x509 -req -in server.csr -signkey server.key -out server.crt

This command generates an SSL/TLS certificate file named server.crt based on the CSR and private key files generated in the previous steps.


