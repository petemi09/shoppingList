'use strict'
var ViewThing = require('./view')

class Subject {

	Constructor() {
		this.handlers = []
	}

	subscribe(fn) {
		this.handlers.push(fn);
	}

	unsubscribe(fn) {
		this.handlers = this.handlers.filter(
			function(item) {
				if (item !== fn) {
					return item;
				}
			}


		);
	}

	publish(msg, someobj) {
		var sccope = someobj || window;
		for (let fn of this.handlers) {
			fn(sccope, msg)
		}
	}
}