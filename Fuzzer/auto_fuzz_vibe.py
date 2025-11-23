from boofuzz import *
import json

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8000

session = Session(
    target=Target(
        connection=TCPSocketConnection(TARGET_IP, TARGET_PORT)
    )
)

# -------------------------
#  GET /
# -------------------------
s_initialize("fuzz_root")
if s_block_start("request"):
    s_static("GET / HTTP/1.1\r\n")
    s_static("Host: localhost\r\n")
    s_static("User-Agent: boofuzz\r\n")
    s_static("Connection: close\r\n\r\n")
s_block_end("request")
session.connect(s_get("fuzz_root"))


# -------------------------
#  POST /auth/signup
# -------------------------
s_initialize("fuzz_signup")
if s_block_start("signup_request"):
    s_static("POST /auth/signup HTTP/1.1\r\n")
    s_static("Host: localhost\r\n")
    s_static("Content-Type: application/json\r\n")
    s_static("Connection: close\r\n\r\n")

    # JSON Body
    body = {
        "fullname": "FUZZ_FULLNAME",
        "email": "FUZZ_EMAIL",
        "password": "FUZZ_PASSWORD"
    }

    json_template = json.dumps(body)
    s_string(json_template, name="signup_json")
s_block_end("signup_request")
session.connect(s_get("fuzz_signup"))


# -------------------------
#  POST /auth/login
# -------------------------
s_initialize("fuzz_login")
if s_block_start("login_request"):
    s_static("POST /auth/login HTTP/1.1\r\n")
    s_static("Host: localhost\r\n")
    s_static("Content-Type: application/json\r\n")
    s_static("Connection: close\r\n\r\n")

    login_body = {
        "email": "FUZZ_EMAIL",
        "password": "FUZZ_PASSWORD"
    }

    login_json = json.dumps(login_body)
    s_string(login_json, name="login_json")
s_block_end("login_request")
session.connect(s_get("fuzz_login"))


# -------------------------
#  POST /auth/forgot-password
# -------------------------
s_initialize("fuzz_forgot")
if s_block_start("forgot_request"):
    s_static("POST /auth/forgot-password HTTP/1.1\r\n")
    s_static("Host: localhost\r\n")
    s_static("Content-Type: application/json\r\n")
    s_static("Connection: close\r\n\r\n")

    forgot_body = {"email": "FUZZ_EMAIL"}
    forgot_json = json.dumps(forgot_body)
    s_string(forgot_json, name="forgot_json")
s_block_end("forgot_request")
session.connect(s_get("fuzz_forgot"))


# -------------------------
#  GET /users
# -------------------------
s_initialize("fuzz_users")
if s_block_start("users_request"):
    s_static("GET /users/ HTTP/1.1\r\n")
    s_static("Host: localhost\r\n")
    s_static("User-Agent: boofuzz\r\n")
    s_static("Connection: close\r\n\r\n")
s_block_end("users_request")
session.connect(s_get("fuzz_users"))


session.fuzz()