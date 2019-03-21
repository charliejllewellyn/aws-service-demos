docker build . -t pca
docker run -ti pca
Create a private CA in certificate manager and then copy the CSR it generates to /ssl/provider-req.pem
cd /ssl
openssl ca -policy policy_loose -out provider-cert.pem -extensions v3_intermediate_ca -infiles provider-req.pem
Password is Pomegranate
cat /ssl/newcerts/0100.pem # This is the Certificate body for PCA
cat /ssl/certs/cacert.pem # This is the Certificate chain for PCA
