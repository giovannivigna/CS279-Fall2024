curl -X GET ${CTF_URL}/api/v1/configs \
--header "Authorization: Token ${CTF_TOKEN}" \
--header "Content-Type: application/json" \
--header "Cookie: site_password=${CTF_SITEPWD}" 
