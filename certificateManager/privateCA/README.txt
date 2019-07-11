docker build . -t pca
docker run -ti pca
Create a private CA in certificate manager and then copy the CSR it generates to /ssl/provider-req.pem
cd /ssl
openssl ca -policy policy_loose -out provider-cert.pem -extensions v3_intermediate_ca -infiles provider-req.pem
Password is Pomegranate
cat /ssl/newcerts/0100.pem # This is the Certificate body for PCA
cat /ssl/certs/cacert.pem # This is the Certificate chain for PCA


To request a cert
openssl req -new -newkey rsa:2048 -days 365 -keyout my_private_key.pem -out my_csr.csr
aws acm-pca issue-certificate \
--certificate-authority-arn arn:aws:acm-pca:eu-west-1:123456789012:certificate-authority/735d1ba0-2bac-4014-9bf7-72732011b73c \
--csr file://my_csr.csr \
--signing-algorithm "SHA256WITHRSA" \
--validity Value=365,Type="DAYS" \
--idempotency-token 1234

to get the cert
aws acm-pca get-certificate \
--certificate-authority-arn arn:aws:acm-pca:region:account:\
certificate-authority/12345678-1234-1234-1234-123456789012 \
--certificate-arn arn:aws:acm-pca:region:account:\
certificate-authority/12345678-1234-1234-1234-123456789012/\
certificate/6707447683a9b7f4055627ffd55cebcc \
--output text 
