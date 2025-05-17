from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

KEY_PREFIX = "longma"

def generate_daily_key():
    return f"{KEY_PREFIX}-{datetime.utcnow().strftime('%Y%m%d')}"

def get_time_left():
    now = datetime.utcnow()
    tomorrow = datetime(now.year, now.month, now.day) + timedelta(days=1)
    time_left = tomorrow - now
    hours, remainder = divmod(int(time_left.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours} giờ {minutes} phút {seconds} giây"

# Giao diện chính hiển thị key đẹp
@app.route("/")
def home():
    key = generate_daily_key()
    return f"""
    <html>
        <head>
            <title>Daily Key</title>
            <style>
                body {{
                    font-family: 'Segoe UI', sans-serif;
                    background-color: #f4f4f4;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .container {{
                    background-color: white;
                    padding: 30px 40px;
                    border-radius: 12px;
                    box-shadow: 0 0 20px rgba(0,0,0,0.1);
                    text-align: center;
                }}
                h1 {{
                    color: #333;
                }}
                .key {{
                    margin-top: 15px;
                    font-size: 24px;
                    font-weight: bold;
                    color: #007acc;
                    letter-spacing: 1px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Today's Key</h1>
                <div class="key">{key}</div>
            </div>
        </body>
    </html>
    """

# Trả về key dạng text đơn giản
@app.route("/api")
def api_key():
    return generate_daily_key(), 200, {'Content-Type': 'text/plain'}

# Trả về thời gian còn lại dạng văn bản
@app.route("/info")
def key_info():
    time_left = get_time_left()
    return f"Thời gian còn lại của key hôm nay: {time_left}", 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
