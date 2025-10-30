from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_PAGE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Do You Love Me?</title>
  <style>
    body {
      margin: 0;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #ff9a9e, #fad0c4);
      color: #fff;
      text-align: center;
    }
    .card {
      background: rgba(255, 255, 255, 0.2);
      padding: 40px;
      border-radius: 20px;
      box-shadow: 0 8px 25px rgba(0,0,0,0.2);
      backdrop-filter: blur(10px);
    }
    h1 {
      font-size: 2.5rem;
      margin-bottom: 20px;
    }
    button {
      background: #ff4d6d;
      border: none;
      padding: 12px 25px;
      margin: 10px;
      font-size: 1.2rem;
      border-radius: 30px;
      color: white;
      cursor: pointer;
      transition: 0.3s;
    }
    button:hover {
      background: #e63950;
      transform: scale(1.1);
    }
    .message {
      margin-top: 20px;
      font-size: 1.5rem;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>Do you love me? 💖</h1>
    <form method="post">
      <button name="answer" value="yes">Yes ❤️</button>
      <button name="answer" value="no">No 💔</button>
    </form>
    {% if reply %}
      <div class="message">{{ reply }}</div>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    reply = None
    if request.method == "POST":
        answer = request.form.get("answer")
        if answer == "yes":
            reply = "I love you too rheum💕"
        else:
            reply = "Oh… that hurts 💔"
    return render_template_string(HTML_PAGE, reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
