# main.py
from fasthtml import FastHTML, Html, Body, Form, Input, Select, Option, Button, P, Script

app = FastHTML()

@app.get("/")
def home():
    return Html(
        Body(
            Form(
                "你的姓名：", Input(name="name", required=True), "<br>",
                "桌游名称：",
                Select(
                    Option("狼人杀"), Option("阿瓦隆"),
                    Option("UNO"), Option("谁是卧底"),
                    name="game"
                ), "<br>",
                "掌握程度（1~5）：",
                Input(type="number", name="level", min="1", max="5", required=True), "<br>",
                "玩过几次：",
                Input(type="number", name="times", min="1", required=True), "<br>",
                Button("提交", type="submit"),
                id="form"
            ),
            P(id="msg"),
            Script("""
                document.getElementById("form").onsubmit = async (e) => {
                  e.preventDefault();
                  const data = Object.fromEntries(new FormData(e.target));
                  await fetch("https://你的后端地址/submit", {
                    method: "POST",
                    body: JSON.stringify(data),
                    headers: {"Content-Type": "application/json"}
                  });
                  document.getElementById("msg").innerText = "提交成功！";
                };
            """)
        )
    )

# Vercel 需要的入口签名
def handler(req, res):
    return app(req, res)
