<html>
    <head>
        <link rel="stylesheet" type="text/css" href="Semantic/semantic.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
        <script src="Semantic/semantic.min.js"></script>
        <script src="js/manager.js"></script>
    </head>
    <body onload="getTokenTable()">
        <table class="ui selectable inverted grey table">
            <thead><tr>
                <th>Name</th>
                <th>Access Token</th>
                <th>Refresh</th></tr>
            </thead>
            <tbody id="tokenContent">
            </tbody>
        </table>
    </body>
</html>
