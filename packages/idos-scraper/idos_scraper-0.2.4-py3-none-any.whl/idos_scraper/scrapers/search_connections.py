import requests
from bs4 import BeautifulSoup
import re
import json

from .. import log

# create logger
logger = log.logging.getLogger(__name__)
logger.addHandler(log.ch)

# SearchConnectionsByStation & SearchConnectionsByLocation call SearchConnections
# async_SearchConnectionsByStation & async_SearchConnectionsByLocation call async_SearchConnections
# Both SearchConnections and async_SearchConnections use blocking ParseConnections

def _GetQuerystringByStation(station_from: str = "Horni polanka", station_to: str = "VŠB-TUO", time: str | None = None, date: str | None = None) -> dict:
    querystring = {"f":f"{station_from}","t":f"{station_to}"}
    
    if time is not None:
        querystring["time"] = time

    if date is not None:
        querystring["date"] = date

    return querystring

def SearchConnectionsByStation(station_from: str = "Horni polanka", station_to: str = "VŠB-TUO", time: str | None = None, date: str | None = None) -> dict:
    querystring = _GetQuerystringByStation(station_from, station_to, time, date)

    return SearchConnections(querystring)

def _GetQuerystringByLocation(station_from: str | None = None, station_to: str = "VŠB-TUO", time: str | None = None, date: str | None = None) -> dict:
    querystring = {"f":"Moje poloha","t":f"{station_to}"}
        
    if time is not None:
        querystring["time"] = time

    if date is not None:
        querystring["date"] = date

    if station_from is None:
        station_from = "loc:49.8384522; 18.1538506%myPosition=true"

    querystring["fc"] = station_from

    return querystring

# The same as GetConnectionsByStation, but the station_from can be empty and will be autofilled with your coordinates
# Uses "fc" query parameter! And "f" is "Moje poloha"
def SearchConnectionsByLocation(station_from: str | None = None, station_to: str = "VŠB-TUO", time: str | None = None, date: str | None = None) -> dict:
    logger.warning(f"SearchConnectionsByLocation is not yet fully implemented")
    querystring = _GetQuerystringByLocation(station_from, station_to, time, date)
    
    return SearchConnections(querystring)

def SearchConnections(querystring: dict) -> dict:
    url = "https://idos.idnes.cz/vlakyautobusymhdvse/spojeni/vysledky/"

    # does not work querystring = {"date":"4.11.2023","time":"02:01", "fs":"1", "f":"loc:49,788988@18,169573","t":"VŠB-TUO"}
    # does not work querystring = {"date":"4.11.2023","time":"02:01", "fs":"1", "f":"loc:49°11'28.4\"N@16°36'44.61\"E","t":"VŠB-TUO"}
    # querystring = {"date":"4.11.2023","time":"02:01","f":"H Pola","t":"VŠB-TUO"}
    # querystring = {"f":"VŠB-TUO","t":"Horni polanka"}
    # querystring = {"date":"4.11.2023","time":"13:15", "f":"Moje poloha", "fc":"loc:49.8384522; 18.1538506%myPosition=true","t":"VŠB-TUO"}

    response = requests.request("GET", url, params=querystring)

    return ParseConnections(response.text)

def SearchConnectionsPOST() -> dict:
    url = "https://idos.idnes.cz/vlakyautobusymhdvse/spojeni/"
    #url = "https://idos.idnes.cz/odis/spojeni/"

    payload = {
        "From": "Horni Polanka",    # "Moje poloha"
        "FromHidden": "",           # "loc:48.789;14.1696%myPosition=true"
        "positionACPosition": "",
        "To": "VSB-TUO",
        "ToHidden": "Horni Polanka%303003",
        "positionACPosition": "",
        "AdvancedForm.Via[0]": "",
        "AdvancedForm.ViaHidden[0]": "",
        "Date": "",
        "Time": "",
        "IsArr": "False",
    }

    response = requests.request("POST", url, data=payload)

    return ParseConnections(response.text)

def ParseConnections(response_text: requests.Response) -> dict:
    soup = BeautifulSoup(response_text, 'html.parser')

    conn_result = ParseConnResult(soup)

    connections_query = dict()
    connections_query["connResult"] = conn_result

    # Adds connections_query["connections"]
    connections_query.update(ParseConnectionsDetails(soup))

    logger.debug(connections_query["connections"])

    return connections_query

def ParseConnResult(soup: BeautifulSoup) -> dict | None:
    connection_result_js = soup.find_all("script", type="text/javascript", string=re.compile("^var params = new Conn\.ConnFormParams"))

    if len(connection_result_js) == 0:
        return None

    result_js = connection_result_js[0].contents[0]

    logger.debug(result_js)

    re_connResult_match = re.compile("var connResult = new Conn\.ConnResult\(params, null, (\{.*?\})\);").search(result_js)
    if re_connResult_match is None:
        return None

    #connResult = chompjs.parse_js_object(re_connResult_match.group(1))
    connResult = json.loads(re_connResult_match.group(1))

    keys = ["handle", "connData", "searchItem", "legend", "absCombId", "arrivalThere"]
    pruned_connResult = {key: connResult[key] for key in keys}
    pruned_connResult["searchDate"] = pruned_connResult["searchItem"]["oConn"]["oUserInput"]["dtSearchDate"]

    # ?: connResult might have interesting data left

    return pruned_connResult

def ParseConnectionsDetails(soup: BeautifulSoup) -> dict:
    connection_query = dict()
    connection_query["connections"] = list()

    connection_details = soup.find_all("div", class_="connection-details")

    # Scraping single connection with possibly more than 2 transfers (non direct connections)
    for html_connection in connection_details:
        logger.debug(f"Connection:")
        html_single_connections = html_connection.find_all("div", class_="outside-of-popup")

        conn = dict()
        conn["single_connections"] = list()

        # Fill ID of connection
        re_id_match = re.compile("^connectionBox-(\d*)$").match(html_connection.parent["id"])
        if re_id_match is None:
            logger.critical("Unable to find connection ID in html <div>'s 'id' attribute")
            raise Exception("Unable to find connection ID in html <div>'s 'id' attribute")

        conn["id"] = re_id_match.group(1)

        for html_single in html_single_connections:
            conn_single = {}

            # Fill delay
            try:
                conn_single["delay"] = ParseDelay(html_single)
            except Exception as e:
                logger.error("Unable to parse time delay")
                raise e

            # Fill icon
            try:
                conn_single["icon"] = ParseIcon(html_single)
            except Exception as e:
                logger.error("Unable to parse icon")
                raise e

            # Fill connection type and number
            # conn_single["type"] = ""
            # conn_single["number"] = ""
            try:
                conn_single.update(ParseTypeAndNumber(html_single))
                logger.debug(f"\tA {conn_single['type']} {conn_single['number']}:")
            except Exception as e:
                logger.error("Unable to parse type and number")
                raise e

            # Fill stations and departure/arrival times
            # conn_single["times"] = list()
            # conn_single["stations"] = list()
            # conn_single["platforms"] = list()
            try:
                conn_single.update(ParseSingleConnectionDetail(html_single))
                logger.debug(
                    f"\t\tDeparture at {conn_single['times'][0]} from {conn_single['stations'][0]}."
                    f" Arrival at {conn_single['times'][1]} at {conn_single['stations'][1]}."
                    )
            except Exception as e:
                logger.error("Unable to parse connection details")
                raise e

            conn["single_connections"].append(conn_single)

        connection_query["connections"].append(conn)

    return connection_query

def ParseDelay(html_single) -> str | None:
    conn_delay = html_single.find("span", class_=re.compile("^conn-result-delay-bubble-"))

    if len(conn_delay.contents) != 3 or conn_delay.contents[1].text is None:
        return None

    return conn_delay.contents[1].text.replace("\\r\\n", "").rstrip()

def ParseIcon(html_single) -> str | None:
    html_connection_string_container = html_single.find("div", class_="title-container")
    html_connection_string = html_connection_string_container.find("span").next

    # Legacy icon names before they changed <img> to <span> without img -_-
    # (I actually do not know how they draw the image instead of a single char in span)
    icon = None
    if html_connection_string == "÷":
        icon = "2.svg"
    elif html_connection_string == "ü":
        icon = "3.svg"

    return icon

def ParseTypeAndNumber(html_single) -> dict:
    html_connection_string_container = html_single.find("div", class_="title-container")
    connection_num = html_single.find("h3").contents[0].contents[0]

    connection_string = html_connection_string_container.find("h3").contents[0].contents[0]

    conn_single = dict()
    conn_single["type"] = None
    conn_single["number"] = None

    re_match = re.compile("(Bus|Tram) (\d*)").search(connection_string)
    if re_match is not None:
        conn_single["type"] = re_match.group(1)
        conn_single["number"] = re_match.group(2)

    return conn_single

def ParseSingleConnectionDetail(html_single) -> dict:
    station_times = html_single.find_all("li", class_="item")

    conn_single = dict()
    conn_single["times"] = list()
    conn_single["stations"] = list()
    conn_single["platforms"] = list()

    for station_and_time in station_times:
        conn_single["times"].append(station_and_time.find("p", class_="time").next_element)
        conn_single["stations"].append(station_and_time.find("p", class_="station").next_element.next_element)
        conn_single["platforms"].append(station_and_time.find("span", title=["nástupiště","stanoviště"]).contents[0])

    return conn_single
