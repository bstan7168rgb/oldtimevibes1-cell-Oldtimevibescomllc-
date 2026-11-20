curl -X PUT "https://api.cloudflare.com/client/v4/accounts/YOUR_ACCOUNT_ID/workers/domains" \
     -H "Authorization: Bearer YOUR_API_TOKEN" \
     -H "Content-Type: application/json" \
     --data '{
       "service": "workflows-starter-template",
       "environment": "production",
       "hostname": "genxnext.online"
     }'