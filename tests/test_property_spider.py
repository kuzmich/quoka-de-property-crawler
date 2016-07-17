from . import get_testdata, make_response, items_only, requests_only


def test_extracting_partner_ad_info():
    from quoka_de.spiders.property import PropertyOffersSpider

    spider = PropertyOffersSpider()

    response = make_response(
        'http://www.quoka.de/immobilien/bueros-gewerbeflaechen/',
        'offer-list-page-1.html'
    )
    results = list(spider.parse_list(response))
    items = list(filter(items_only, results))
    print(items)

    assert len(items) == 4

    assert items[0] == {'title': 'HCC - Blick über Dortmund. .. natürlich ...',
                        'price': '9.019,-',
                        'partner_ad': True}

    assert items[1] == {'title': 'Modernes Bürogebäude im schönen Westend',
                        'price': '15.834,-',
                        'partner_ad': True}

    assert items[2] == {'title': 'Praxis- und Büroflächen im Altbau',
                        'price': '825,-',
                        'partner_ad': True}

    assert items[3] == {'title': 'Das etwas andere Büro im charmanten Altb...',
                        'price': '8,-',
                        'partner_ad': True}

