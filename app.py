from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Custom Text App</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: {{ background }};
            overflow: hidden;
        }
        .controls {
            position: fixed;
            top: 0;
            width: 100%;
            padding: 14px;
            background: rgba(255,255,255,0.96);
            z-index: 10;
            font-family: Arial, sans-serif;
        }
        .controls input,
        .controls select {
            margin: 4px;
        }
        .main-text {
            margin-top: 190px;
            text-align: {{ align }};
            font-family: {{ font }};
            font-size: {{ size }}px;
            font-weight: {{ weight }};
            color: {{ text_color }};
            text-shadow: {{ shadow }};
            animation: {{ animation }} {{ speed }}s linear infinite;
        }
        @keyframes none { from { transform:none; } to { transform:none; } }
        @keyframes rain { 0%{transform:translateY(-30px);}100%{transform:translateY(30px);} }
        @keyframes snow { 0%{transform:translateY(-10px);}100%{transform:translateY(10px);} }
        @keyframes hail { 0%{transform:translateY(-50px);}100%{transform:translateY(50px);} }
        @keyframes wind { 0%{transform:translateX(-40px);}100%{transform:translateX(40px);} }
        @keyframes confetti { 0%{transform:rotate(0deg);}100%{transform:rotate(360deg);} }
        @keyframes tornado { 0%{transform:rotate(0deg) scale(1);}100%{transform:rotate(720deg) scale(1.2);} }
    </style>
</head>
<body>
<div class="controls">
<form method="POST">
Main Text: <input name="main_text" value="{{ main_text }}" size="14">
Name: <input name="name" value="{{ name }}" size="10">
Emoji: <input name="emoji" value="{{ emoji }}" size="4"><br><br>
Font:
<select name="font">
{% for f in fonts %}<option value="{{ f }}" {% if f==font %}selected{% endif %}>{{ f }}</option>{% endfor %}
</select>
Size:
<select name="size">
{% for s in sizes %}<option value="{{ s }}" {% if s==size %}selected{% endif %}>{{ s }}</option>{% endfor %}
</select>
Weight:
<select name="weight">
<option value="normal">Normal</option>
<option value="bold" {% if weight=='bold' %}selected{% endif %}>Bold</option>
</select>
Align:
<select name="align">
<option value="center">Center</option>
<option value="left" {% if align=='left' %}selected{% endif %}>Left</option>
<option value="right" {% if align=='right' %}selected{% endif %}>Right</option>
</select><br><br>
Text Color: <input type="color" name="text_color" value="{{ text_color }}">
Background: <input type="color" name="bg_color" value="{{ bg_color }}">
Gradient:
<select name="gradient">
<option value="off">Off</option>
<option value="on" {% if gradient=='on' %}selected{% endif %}>On</option>
</select>
Shadow:
<select name="shadow_on">
<option value="off">Off</option>
<option value="on" {% if shadow_on=='on' %}selected{% endif %}>On</option>
</select><br><br>
Effect:
<select name="animation">
{% for a in animations %}<option value="{{ a }}" {% if a==animation %}selected{% endif %}>{{ a }}</option>{% endfor %}
</select>
Speed:
<select name="speed">
{% for sp in speeds %}<option value="{{ sp }}" {% if sp==speed %}selected{% endif %}>{{ sp }}s</option>{% endfor %}
</select>
<button type="submit">Update</button>
</form>
</div>
<div class="main-text">
{{ main_text }} {{ name }} {{ emoji }}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def index():
    data = {
        "main_text":"Hello",
        "name":"World",
        "emoji":"🌍",
        "font":"Arial",
        "size":48,
        "weight":"normal",
        "align":"center",
        "text_color":"#000000",
        "bg_color":"#ffffff",
        "gradient":"off",
        "shadow_on":"off",
        "animation":"none",
        "speed":4
    }
    if request.method=="POST":
        for k in data:
            if k in request.form:
                data[k]=request.form[k]
        data["size"]=int(data["size"])
        data["speed"]=int(data["speed"])

    background = f"linear-gradient(135deg,{data['bg_color']},#00000022)" if data["gradient"]=="on" else data["bg_color"]
    shadow = "2px 2px 6px rgba(0,0,0,0.4)" if data["shadow_on"]=="on" else "none"

    return render_template_string(
        HTML,
        **data,
        background=background,
        shadow=shadow,
        fonts=["Arial","Courier New","Georgia","Times New Roman","Comic Sans MS"],
        sizes=[24,32,40,48,60,72,96],
        animations=["none","rain","snow","hail","wind","confetti","tornado"],
        speeds=[2,4,6,8,10]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
