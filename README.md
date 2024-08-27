# JSC-STS-referal


Script to get container-id
```
docker ps
```

Export backup on db (ONLY SERVER DATABASE)
```
docker exec -it <container-id> /bin/bash -c "/scripts/create_backup.sh"  
```

Import from recent backup/dump (ONLY SERVER DATABSE)
```
docker exec -it <container-id> /bin/bash -c "/scripts/restore_from_backup.sh" 
```

Export realms and users Keycloak (ONLY KEYCLOAK CONTAINER)
```
docker exec it <container-id> /bin/bash -c "/opt/keycloak/bin/kc.sh export --dir /opt/keycloak/data/import --users realm_file --realm kinetic"
```

Generate CRT and KEY for SSL/TLS ceritificate 
```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./nginx/ssl/localhost.key -out ./nginx/ssl/localhost.crt -subj "/CN=localhost"
```