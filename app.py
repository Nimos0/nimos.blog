from flask import Flask, render_template_string, url_for

app = Flask(__name__)
application = app

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nimos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            border: 1px solid #ccc;
            position: relative;
        }
        .profile-image {
            display: inline-block;
            vertical-align: middle;
            margin-left: 20ch; /* 20 spaces */
        }
        a {
            color: green;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        h2 {
            color: green;
        }
        pre {
            background: #f8f8f8;
            padding: 10px;
            border: 1px solid #ccc;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <nav>
            <a href="#">home</a> | 
            <a href="#">posts</a> | 
            <a href="#">log</a>
        </nav>
        <h1>Nimos</h1>
        <p>independent researcher learning to program<span class="profile-image"><img src="{{ url_for('static', filename='nimos.pfp.png') }}"></span></p>
        <h2>about</h2>
        <p>this blog is an experiment to push myself to write more. my hope is that sharing my work publically will lead to more interesting discussions. if you're reading this and i have less posts/github commits than you have fingers - i'm failing at this goal.</p>
        <h2>who am i?</h2>
        <p><span style="background-color: #e0ffe0;">anime pfp with a few brain cells and an internet connection</span></p>
        <p>i'm a <strong>mid-20-something-year-old based in New York</strong>. it seems to me like one of the most important things i can do with my time is build better economic models/simulations using recent advancements in technology.</p>
        <p>you can reach me via Twitter DMs.</p>
        <h2>recent work/writing</h2>
        <ul>
            <li>whisper (<a href="https://whispersite.notion.site/dd58f25569b84c8ca417450811a4ac18">link</a>)</li>
            <li>building simulations of real-time economic activity (<a href="https://smiling-knight-f53.notion.site/Building-simulations-of-real-time-economic-activity-0dc4008564374b2187491f21802a1dc6">link</a>)</li>
            <li>first project coming soon</li>
        </ul>
        <footer>
            <a href="https://x.com/Nimos0">twitter</a>
        </footer>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=8080)  # Change 8080 to your desired port