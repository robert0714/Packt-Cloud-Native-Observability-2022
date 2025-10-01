from opentelemetry.metrics import get_meter_provider, set_meter_provider, Observation
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.metrics.export import (
    ConsoleMetricExporter,
    PeriodicExportingMetricReader,
)
import time
import resource
from opentelemetry.sdk.metrics import View
from opentelemetry.metrics import Counter
from opentelemetry.sdk.metrics.aggregation import LastValueAggregation


def async_gauge_callback(options):
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    yield Observation(rss, {})


def async_counter_callback(options):
    yield Observation(10)


def async_updowncounter_callback(options):
    yield Observation(20, {"locale": "en-US"})
    yield Observation(10, {"locale": "fr-CA"})


def configure_meter_provider():
    exporter = ConsoleMetricExporter()
    reader = PeriodicExportingMetricReader(exporter, export_interval_millis=5000)
    view = View(
        instrument_type=Counter,
        attribute_keys=[],
        name="sold",
        description="total items sold",
        aggregation=LastValueAggregation(),
    )
    provider = MeterProvider(
        metric_readers=[reader],
        resource=Resource.create(),
        views=[view],
        enable_default_view=False,
    )
    set_meter_provider(provider)


if __name__ == "__main__":
    configure_meter_provider()
    meter = get_meter_provider().get_meter(
        name="metric-example",
        version="0.1.2",
        schema_url=" https://opentelemetry.io/schemas/1.9.0",
    )
    counter = meter.create_counter(
        "items_sold", unit="items", description="Total items sold"
    )
    counter.add(6, {"locale": "fr-FR", "country": "CA"})
    counter.add(1, {"locale": "es-ES"})

    meter.create_observable_counter(
        name="major_page_faults",
        description="page faults requiring I/O",
        unit="fault",
        callbacks=[async_counter_callback],
    )
    # time.sleep(10)
    inventory_counter = meter.create_up_down_counter(
        name="inventory",
        unit="items",
        description="Number of items in inventory",
    )
    inventory_counter.add(20)
    inventory_counter.add(-5)

    upcounter_counter = meter.create_observable_up_down_counter(
        name="customer_in_store",
        unit="persons",
        description="Keeps a count of customers in the store",
        callbacks=[async_updowncounter_callback],
    )
    # time.sleep(10)
    histogram = meter.create_histogram(
        "response_times",
        unit="ms",
        description="Response times for all requests",
    )
    histogram.record(96)
    histogram.record(9)
    meter.create_observable_gauge(
        name="maxrss",
        unit="bytes",
        description="Max resident set size",
        callbacks=[async_gauge_callback],
    )
    # time.sleep(10)
