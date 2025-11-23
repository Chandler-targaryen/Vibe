from boofuzz import *

def main():
    session = Session(
        target=Target(
            connection=TCPSocketConnection("127.0.0.1", 8000)
        )
    )

    s_initialize("simple_fuzz")

    if s_block_start("req"):
        s_static("GET /", name="method")
        s_string("FUZZ", name="path", fuzzable=True)
        s_static(" HTTP/1.1\r\nHost: localhost\r\n\r\n")
    s_block_end("req")

    session.connect(s_get("simple_fuzz"))
    session.fuzz()

if __name__ == "__main__":
    main()