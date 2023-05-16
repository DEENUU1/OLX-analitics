from flask import Blueprint, render_template, request, redirect, url_for, flash
from data import fetch_data, parser
from operation import operation

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
def results_view():
    url = fetch_data.UrlBuilderHouse().build_url(
        limit="40",
        area_min="25",
        price_min="600",
    )
    x = parser.Parser(fetch_data.FetchData(url).fetch_data())
    d = x.data_parser()

    s = operation.return_newest_offers(d)
    z = operation.return_cheapest_offer(d)
    y = operation.return_average_price(d)
    g = operation.return_cheapest_offer_per_meter(d)
    f = operation.return_average_price_per_meter(d)
    v = operation.return_most_expensive_offer(d)
    i = operation.return_most_expensive_offer_per_meter(d)
    u = operation.return_offer_largest_area_building(d)
    l = operation.return_offer_largest_area_plot(d)

    print(url)
    return render_template(
        "results.html",
        data_list=d,
        newest_offers=s,
        cheapest_offer=z,
        average_price=y,
        cheapest_offer_per_meter=g,
        average_price_per_meter=f,
        most_expensive_offer=v,
        most_expensive_offer_per_meter=i,
        largest_area_building=u,
        largest_area_plot=l,
    )
