curl -X POST "https://your-cloud-run-url.run.app/api/v1/sync/bulk-products" \
     -H "Authorization: Bearer YOUR_GATEWAY_API_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "source": "base44",
       "channels": ["walmart", "amazon"],
       "items": [
         { "sku": "OTV-BEANIE-01", "title": "Old-Time Vibes Embroidered Beanie", "price": 18.00, "inventory": 100 },
         { "sku": "OTV-ALBUM-CD", "title": "Physical CD Album - Limited Edition", "price": 15.00, "inventory": 50 }
       ]
     }'