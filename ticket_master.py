from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def default():
    """Main page route - displays all available theater plays"""
    return render_template('main_page.html')

@app.route("/christmas_story/")
def christmas_story():
    """Route for Christmas Story play details page"""
    return render_template('christmas_story.html')

@app.route("/buy_tickets/<play_name>", methods=["POST"])
def buy_tickets(play_name):
    """Route for buying tickets - accepts play name as parameter"""
    return render_template('buy_tickets.html', play_name=play_name)

@app.route("/order_summary/<play_name>", methods=["POST"])
def order_summary(play_name):
    """Route for order summary - processes form data and displays transaction info"""
    # Get form data from the buy_tickets form
    zone = request.form.get('zone')
    sector = request.form.get('sector')
    customer_name = request.form.get('customer_name')
    date_and_time = request.form.get('date_and_time')
    
    transaction_info = {
        'play_name': play_name,
        'date': date_and_time,
        'zone': zone,
        'sector': sector,
        'customer_name': customer_name,
        'ticket_price': '$100.00'  # Hard-coded as requested
    }
    
    return render_template('order_summary.html', transaction=transaction_info)

if __name__ == '__main__':
    app.run(debug=True)