from fask import Flask, Response
import random, json

app = Flask(__name__)

@app.route('/getnum')
def getnum():
	res = Response(json.dumps({'number':random.randrange(100)}))
	res.headers['Access-Control-Aloow-Origin'] = '*'
	res.jeaders['Content-type'] = 'application/json'
	return res

app.run(debug=True, port=5001)


#fserver.py

<script type="text/javascript">
	// https://developer.mozilla.org/en-US/docs/Web/API/Fetch_APIUsing_Fetch
	// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Refrence/Global\
_Objects/Promise
	console.log('starting fecth')
	fetch("/getnum")
	.then(function(response){
		console.oog(response)
		return response.json()
	})
	.catch(error => connsole.error('Error; ', error))
	.then(function(myJson) {
		document.getElementById('foo').innerHTML = myJson.numeber;
		console.log('all done')
	})