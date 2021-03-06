import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    rows = db.execute("SELECT symbol, shares FROM portofolio WHERE user_id = :user",
                          user=session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']
    # create list
    stocks = []
    total = cash
    # iterate each stock
    for row in rows:
        stock = lookup(row['symbol'])
        price = round(stock['price'] * row['shares'], 2)
        # add dict to list
        stocks.append({'symbol': row['symbol'],
                        'name': stock['name'],
                        'shares': row['shares'],
                        'price': round(stock['price'], 2),
                        'total': price})
        total += price
    # render
    return render_template("index.html", stocks=stocks, cash=round(cash, 2), total=round(total, 2))
    # return apology("TODO")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        shares = int(request.form.get("shares"))
        
        if lookup(request.form.get("symbol")) == None:
            return apology("Stock didn't found", 403)
        elif shares < 0:
            return apology("Share must be positive integer", 403)
        
        symbol = lookup(request.form.get("symbol"))
        price = symbol['price']
        cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']
        
        total_cash = cash - (price * shares)

        if total_cash < 0:
            return apology("Your cash didn't enough")
        
        stock = db.execute("SELECT shares FROM portofolio WHERE user_id = :user AND symbol = :symbol",
                          user=session["user_id"], symbol=symbol['symbol'])

        if not stock:
            db.execute("INSERT INTO portofolio(user_id, symbol, shares) VALUES (:user, :symbol, :shares)",
                user=session["user_id"], symbol=symbol['symbol'], shares=shares)
        else:
            # shares += stock[0]['shares']

            db.execute("UPDATE portofolio SET shares = :shares WHERE user_id = :user AND symbol = :symbol",
                user=session["user_id"], symbol=symbol['symbol'], shares=shares + stock[0]['shares'])

        db.execute("UPDATE users SET cash = :cash WHERE id = :user",
                          cash=total_cash, user=session["user_id"])
        
        db.execute("INSERT INTO history(user_id, symbol, shares, prices) VALUES (:user, :symbol, :shares, :prices)",
                user=session["user_id"], symbol=symbol['symbol'], shares=shares, prices=price)

        flash("Bought!")
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # get all the history data
    history = db.execute("SELECT * FROM history WHERE user_id = :user",
                            user=session["user_id"])

    return render_template("history.html", history=history)
    # return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # User click via POST
    if request.method == "POST":
        # gaining stock info
        stock = lookup(request.form.get("symbol"))
        # check if stock exists
        if not stock:
            return apology("Stock didn't found")
        # return 
        return render_template("quoted.html", stock=stock)
    # User click via GET
    else:
        return render_template("quote.html")

    # return apology("TODO")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # render to register if via GET
    if request.method == "GET":
        return render_template("register.html")
    # process data and redirect if via POST
    elif request.method == "POST":
        user = request.form.get("username")
        password = request.form.get("password")
        # Check password same with confirmation
        if password != request.form.get("confirmation"):
            return apology("password and confirmation didn't match", 403)
        # check username in database if already exists
        elif db.execute("SELECT * FROM users WHERE username = :username",
            username=user):
            return apology("Username already taken", 403)
        
        db.execute("INSERT INTO users(username, hash) VALUES (:username, :hash)",
            username=user, hash=generate_password_hash(password))
        
        # insert user in database
        rows = db.execute("SELECT * FROM users WHERE username = :username",
            username=request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("Registered!")
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        # collect informations
        shares = int(request.form.get("shares"))
        symbol = request.form.get("symbol")
        price = lookup(symbol)["price"]
        value = round(price * shares, 2)
        
        # check shares in portofolio stock
        init_share = db.execute("SELECT shares FROM portofolio WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"])[0]['shares']
        final_share = init_share - shares

        # delete all the stock if sell all unit
        if final_share == 0:
            db.execute("DELETE FROM portofolio WHERE user_id = :user AND symbol = :symbol",
                          user=session["user_id"], symbol=symbol)

        # stop the transaction if exceed 
        elif final_share < 0:
            return apology("Exceed stock to sell")

        # update the value
        else:
            db.execute("UPDATE portofolio SET shares = :shares WHERE user_id = :user AND symbol = :symbol",
                          symbol=symbol, user=session["user_id"], shares=final_share)

        # update user cash
        cash = db.execute("SELECT cash FROM users WHERE id = :user",
                          user=session["user_id"])[0]['cash']
        total = cash + value

        db.execute("UPDATE users SET cash = :cash WHERE id = :user",
                          cash=total, user=session["user_id"])

        # Update history table
        db.execute("INSERT INTO history(user_id, symbol, shares, prices) VALUES (:user, :symbol, :shares, :prices)",
                user=session["user_id"], symbol=symbol, shares=-shares, prices=price)
        
        # send success message and redirect
        flash("Sold!")
        return redirect("/")

    elif request.method == "GET":
        # get all the own stock
        stocks = db.execute("SELECT symbol, shares FROM portofolio WHERE user_id = :user",
                          user=session["user_id"])
        
        return render_template("sell.html", stocks=stocks)


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
