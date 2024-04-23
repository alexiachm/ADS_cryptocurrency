
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cryptocurrency Search</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f6f6f6;
            margin: 0;
            padding: 0;
        }
        .header-container {
            background-color: black;
            color: white;
            padding: 20px;
            text-align: center;
        }
        h1, h2 {
            color: #fff; /* White text color */
        }
        .title-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 20px;
            position: relative;
            background-color: #f6f6f6;
            padding: 20px;
        }
        .crypto-img {
            max-width: 100px; /* Set maximum width */
            height: auto; /* Maintain aspect ratio */
            margin-right: 10px; /* Adjust spacing as needed */
        }
        form {
            text-align: center;
            margin-top: 20px;
        }
        input[type="text"] {
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button[type="submit"] {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .results-container {
            margin: 0 auto;
            width: 80%; /* Adjust width as needed */
            background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white background */
            padding: 20px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        .list-item {
            color: black; /* Set list item text color to black */
        }
        a {
            color: #4CAF50;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        p {
            text-align: center;
            margin-top: 20px;
        }
        .title {
            color: black; /* Set title color to black */
        }
    </style>
</head>
<body>
    <div class="header-container">
        <form action="/" method="post">
            <input type="text" name="search_input" placeholder="Enter name or NIF">
            <button type="submit">Search</button>
        </form>
        {% if currency %}
        <div class="results-container">
            <h2 class="title">Search Results</h2>
            <ul>
                {% for currency_data in currency %}
                <li class="list-item">Name: {{ currency_data.name }}</li>
                <li class="list-item">NIF: {{ currency_data.NIF }}</li>
                <li class="list-item">Founder: {{ currency_data.Founder }}</li>
                <li class="list-item">Date Founded: {{ currency_data.Date_Founded }}</li>
                <li class="list-item">Consensus Mechanism: {{ currency_data.Consensus_Mechanism }}</li>
                <li class="list-item">Max Supply: {{ currency_data.Max_Supply }}</li>
                <li class="list-item">Circulating Supply: {{ currency_data.Circulating_Supply }}</li>
                <li class="list-item">Total Supply: {{ currency_data.Total_Supply }}</li>
                <li class="list-item">Market Cap: {{ currency_data.Market_Cap }}</li>
                <li class="list-item">Website: <a href="{{ currency_data.Website }}" target="_blank">{{ currency_data.name }}</a></li>
                <li class="list-item">Whitepaper: <a href="{{ currency_data.Whitepaper }}" target="_blank">Link</a></li>
                <li class="list-item">Github: <a href="{{ currency_data.Github }}" target="_blank">Link</a></li>
                <li class="list-item">Reddit: <a href="{{ currency_data.Reddit }}" target="_blank">Link</a></li>
                <!-- Add other fields as needed -->
                {% endfor %}
            </ul>
        </div>
        {% endif %}
    </div>
    <div class="title-container">
        <img class="crypto-img" src="static/crypto.jpg" alt="Cryptocurrency Image">
        <h1 class="title">Search for Cryptocurrency</h1>
    </div>
    {% if message %}
    <p>{{ message }}</p>
    {% endif %}
</body>
</html>


