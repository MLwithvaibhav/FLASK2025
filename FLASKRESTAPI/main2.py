from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/armstrong/<int:n>')
def armstrong(n):
    total = 0
    order = len(str(n))
    copy_n = n

    while n > 0:
        digit = n % 10
        total += digit ** order
        n //= 10

    if total == copy_n:
        print(f"{copy_n} is an Armstrong number ✅") 
        result = {
            "Number": copy_n,
            "Armstrong": True,
            "Server IP": "122.345.33.12 "
        }

    else:
        print(f"{copy_n} is not an Armstrong number ❌") 
        result = {
            "Number": copy_n,
            "Armstrong": False,
            "Server IP": "122.345.33.12 "
        }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)