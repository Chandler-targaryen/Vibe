from boofuzz import *
import json
import time

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8000


session = Session(
    target=Target(
        connection=TCPSocketConnection(TARGET_IP, TARGET_PORT)
    ),
    sleep_time=0.5 
)

# -------------------------
# CONFIG: Large payload generator 
# -------------------------

LARGE = "A" * 5000   # 5KB fuzz seed
HUGE = "B" * 10000   # 10KB fuzz seed

# -------------------------
#  GET /
# -------------------------
s_initialize("GET_root")
if s_block_start("req"):
    s_static("GET / HTTP/1.1\r\n")
    s_static("Host: localhost\r\n")
    s_static("User-Agent: fuzzclient\r\n")
    s_static("Connection: close\r\n\r\n")
s_block_end("req")
session.connect(s_get("GET_root"))


# -------------------------
#  POST /auth/signup (Sequence step 1)
# -------------------------
s_initialize("POST_signup")
if s_block_start("signup_req"):
    s_static("POST /auth/signup HTTP/1.1\r\n")
    s_static("Host: localhost\r\n")
    s_static("Content-Type: application/json\r\n")
    s_static("Connection: close\r\n\r\n")

    body = {
        "fullname": LARGE,
        "email": f"user_{LARGE}@example.com",
        "password": HUGE
    }
    s_string(json.dumps(body), name="signup_body")
s_block_end("signup_req")
session.connect(s_get("POST_signup"))


# -------------------------
#  POST /auth/login (Sequence step 2)
# -------------------------
s_initialize("POST_login")
if s_block_start("login_req"):
    s_static("POST /auth/login HTTP/1.1\r\n")
    s_static("Host: localhost\r\n")
    s_static("Content-Type: application/json\r\n")
    s_static("Connection: close\r\n\r\n")

    login_body = {
        "email": f"email_{LARGE}@test.com",
        "password": HUGE
    }
    s_string(json.dumps(login_body), name="login_body")
s_block_end("login_req")
session.connect(s_get("POST_login"))


# -------------------------
#  POST /auth/forgot-password (Sequence step 3)
# -------------------------
s_initialize("POST_forgot")
if s_block_start("forgot_req"):
    s_static("POST /auth/forgot-password HTTP/1.1\r\n")
    s_static("Host: localhost\r\n")
    s_static("Content-Type: application/json\r\n")
    s_static("Connection: close\r\n\r\n")

    forgot_body = {"email": f"fuzz_{HUGE}@gmail.com"}
    s_string(json.dumps(forgot_body), name="forgot_body")
s_block_end("forgot_req")
session.connect(s_get("POST_forgot"))


# -------------------------
#  GET /users/ (Sequence step 4)
# -------------------------
s_initialize("GET_users")
if s_block_start("users_req"):
    s_static("GET /users/ HTTP/1.1\r\n")
    s_static("Host: localhost\r\n")
    s_static("User-Agent: fuzzclient\r\n")
    s_static("Connection: close\r\n\r\n")
s_block_end("users_req")
session.connect(s_get("GET_users"))

print("Dashboard: http://localhost:26000")

session.fuzz()