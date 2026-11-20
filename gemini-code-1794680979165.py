import os
import stripe
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize Stripe with live secret key from secure environment / Secret Manager
stripe.api_key = os.getenv("STRIPE_SECRET_KEY", "sk_live_placeholder")
ENDPOINT_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "whsec_placeholder")

@app.route("/api/v1/stripe/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.get_data()
    sig_header = request.headers.get("Stripe-Signature")

    try:
        # Cryptographically verify the webhook event against Stripe's signing secret
        event = stripe.Webhook.construct_event(
            payload, sig_header, ENDPOINT_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return jsonify({"error": "Invalid payload"}), 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return jsonify({"error": "Invalid signature"}), 400

    # Handle the completed checkout session event
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        
        # Extract metadata and UCP routing parameters from the session
        customer_email = session.get("customer_details", {}).get("email")
        metadata = session.get("metadata", {})
        channel = metadata.get("fulfillment_channel", "printful")
        line_items_data = session.get("line_items", {})

        order_record = {
            "session_id": session.get("id"),
            "payment_intent": session.get("payment_intent"),
            "customer_email": customer_email,
            "amount_total": session.get("amount_total"),
            "currency": session.get("currency"),
            "fulfillment_channel": channel,
            "items": metadata.get("items_json", "[]"),
            "status": "paid_and_routed"
        }

        # Idempotent local database logging and downstream fulfillment trigger
        success = persist_order_and_dispatch(order_record)
        if not success:
            return jsonify({"error": "Database persistence or routing failed"}), 500

    return jsonify({"status": "success", "received": True}), 200

def persist_order_and_dispatch(order):
    """Logs the transaction locally and pushes payload to fulfillment engine."""
    # Insert order into local database table with unique session constraint (idempotency)
    print(f"[OTV-GATEWAY] Processing paid UCP order {order['session_id']} for {order['customer_email']}")
    # Dispatch to Printful/Printify API endpoint or local queue here...
    return True

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)