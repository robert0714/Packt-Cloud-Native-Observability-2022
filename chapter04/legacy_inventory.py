from flask import Flask, jsonify, request
from opentelemetry import context
from opentelemetry.propagate import extract, set_global_textmap
from opentelemetry.propagators.b3 import B3MultiFormat
from opentelemetry.propagators.composite import CompositePropagator
from opentelemetry.trace import SpanKind, propagation
from opentelemetry.trace.propagation import tracecontext
from common import configure_tracer, set_span_attributes_from_flask

tracer = configure_tracer("legacy-inventory", "0.9.1")
app = Flask(__name__)
# Set the global propagator to a composite propagator that supports both
# TraceContext and B3 formats.
set_global_textmap(CompositePropagator([tracecontext.TraceContextTextMapPropagator(), B3MultiFormat()]))

@app.before_request
def before_request_func():
    token = context.attach(extract(request.headers))
    request.environ["context_token"] = token

@app.teardown_request
def teardown_request_func(err):
    token = request.environ.get("context_token", None)
    if token:
        context.detach(token)

@app.route("/inventory")
@tracer.start_as_current_span("/inventory", kind=SpanKind.SERVER)
def inventory():
    set_span_attributes_from_flask()
    products = [
        {"name": "oranges", "quantity": "10"},
        {"name": "apples", "quantity": "20"},
    ]
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
