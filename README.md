# graph_recursion

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```


## Run the server

using Bash :

```
$ export FLASK_APP=flask_app
$ flask run
 * Running on http://127.0.0.1:5000/
```

using CMD :

```
> set FLASK_APP=hello
> flask run
 * Running on http://127.0.0.1:5000/
```

using Powershell :

```
> $env:FLASK_APP = "flask_app"
> flask run
 * Running on http://127.0.0.1:5000/
```

## Flask Application Structure 
```
|──────graph_recursion/
| |────templates/
| | |────index.html/
|──────flask_app.py

both uolfp and fpvecalculator are located on flask_app file 
```


## website location on pythoneverywhere 
```
/home/vanavah/mysite
```


## fpvecalculator route   
```
@app.route('/fpvecalculator')
def fpvecalculator():
    return render_template('index.html')
```

## uolfp route   
```
@app.route('/uolfp')
def uolfp():
    return str(floyd(graph))
```

## html/js explanation
Reset button
---
    // we will call this function to clear the inputs and restore the default values
    function clear_data() {
        // we need to get the list of inputs so we can loop and assign the default value 
        inputs = document.getElementsByTagName('input')
        for (var i = 0; i < inputs.length; i++) {
            // assign the default value 
            inputs[i]['value'] = inputs[i].dataset.defaultValue
        }
        // get the textarea and clear the data 
        txtArea = document.getElementsByTagName('textarea')[0]
        txtArea['value'] = ''
    }
---

Print Graph button
---
    // we will use this function to call the api and get the results 
    async function print_graph() {
        inputs = document.getElementsByTagName('input')
        let data = []
        // obj is an object to hold the values
        obj = {}
        // we will loop and get the values from the inputs
        for (var i = 0; i < inputs.length; i++) {
            obj[inputs[i]['name']] = inputs[i]['value']
        }
        txtArea = document.getElementsByTagName('textarea')[0]
        obj['multiline1'] = txtArea['value']
        data.push(obj)
        let res = await fetch('/print_graph', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
        });
        const content = await res.json();
        // we attach the result to textarea .
        txtArea.value = content['res']
    }
---

## pythoneverywhere Config links
flask_app.py
- https://www.pythonanywhere.com/user/vanavah/files/home/vanavah/mysite/flask_app.py?edit

index.py
- https://www.pythonanywhere.com/user/vanavah/files/home/vanavah/mysite/templates/index.html?edit

## Screenshots

- http://vanavah.pythonanywhere.com/uolfp

<kbd> 
<img src="https://user-images.githubusercontent.com/62887129/178048108-c8444af1-de46-41db-8732-2c2550ba4029.png"/>
</kbd>  

- http://vanavah.pythonanywhere.com/fpvecalculator

<kbd> 
<img src="https://user-images.githubusercontent.com/62887129/178048111-f92c897d-9d20-4911-b0be-63c0c849ad73.png"/>
</kbd>  

## Reference

-   Documentation: https://flask.palletsprojects.com/
-   Changes: https://flask.palletsprojects.com/changes/
-   PyPI Releases: https://pypi.org/project/Flask/
-   Source Code: https://github.com/pallets/flask/
-   Issue Tracker: https://github.com/pallets/flask/issues/
-   Website: https://palletsprojects.com/p/flask/
-   Twitter: https://twitter.com/PalletsTeam
-   Chat: https://discord.gg/pallets
